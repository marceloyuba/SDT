from google.cloud import storage
import pandas as pd
import pyarrow
import warnings
warnings.filterwarnings("ignore")


def verificar_archivo_existente_2(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    for blob in bucket.list_blobs():
        if blob.name.endswith(file_name):
            return True
    return False

def revision_duplicados(data:pd.DataFrame) -> None:
    print()
    print('Duplicados')
    print()
    duplicados = data.duplicated().sum()
    total = len(data)
    porcentaje = round(duplicados/total*100,2)
    print()
    print(f'Cantidad de duplicados: {duplicados:<7}      Porcentaje de duplicados: {str(porcentaje) + " %":<8}')
    print()
    if duplicados > 0:
        data = data.drop_duplicates()
        print()
        print()
        print(f'Se eliminaron {duplicados} registros duplicados.')
        print()
        print()

def asignar_color(df,color):
    def asignar_color_por_location(location):
        if location not in [264, 265]:
            return color
        else:
            return 'ND'

    df['tipo_color'] = df['PULocationID'].apply(asignar_color_por_location)
    return df

def ajuste_anio(df,year,col_prefix):
    # Obtiene todas las columnas que comienzan con el prefijo dado
    pickup_col = [col for col in df.columns if col.startswith(col_prefix + 'pickup_datetime')]
    dropoff_col = [col for col in df.columns if col.startswith(col_prefix + 'dropoff_datetime')]
            
    #year = int(archivo.split('_')[2])
    # Filtra las filas donde las fechas no coinciden con el año del df
    df = df[(df[pickup_col[0]].dt.year == year) & (df[dropoff_col[0]].dt.year == year)]
        # Separar las columnas de fecha y hora en componentes individuales
    df['anio'] = df[col_prefix + 'pickup_datetime'].dt.year
    df['mes'] = df[col_prefix + 'pickup_datetime'].dt.month
    df['dia_inicio'] = df[col_prefix + 'pickup_datetime'].dt.day
    df['hora_inicio'] = df[col_prefix + 'pickup_datetime'].dt.time
        
    df['dia_fin'] = df[col_prefix + 'pickup_datetime'].dt.day
    df['hora_fin'] = df[col_prefix + 'dropoff_datetime'].dt.time

    # Calcula la diferencia entre la columna de dropoff y pickup para obtener el tiempo de viaje
    df['tiempo'] = df[col_prefix + 'dropoff_datetime'] - df[col_prefix + 'pickup_datetime']
        
    # Extrae los componentes de tiempo: horas, minutos y segundos
    df['horas'] = df['tiempo'].dt.components['hours']
    df['minutos'] = df['tiempo'].dt.components['minutes']
    df['segundos'] = df['tiempo'].dt.components['seconds']
    # Combina las columnas de horas, minutos y segundos en una sola columna
    df['total_tiempo'] = df['horas'].astype(str).str.zfill(2) + ':' + df['minutos'].astype(str).str.zfill(2) + ':' + df['segundos'].astype(str).str.zfill(2)
        
    df.drop(columns=['tiempo','horas','minutos', 'segundos',col_prefix + 'dropoff_datetime',col_prefix + 'pickup_datetime'],inplace= True)
        # Reestablece los índices
    df.reset_index(drop=True, inplace=True)
    
    return df

#FUNCION PARA AGREGAR COLUMNA DE IDENTIFICADOR UNICO 'viaje_Id' (CLAVE SUBRROGADA)
def generar_id(row):
    fila = row.name + 1  # Obtener el número de fila
    mes = row['mes']  # Obtener el mes actual de la columna 'mes'
    return f"{fila:013}{mes:02}"  # Formar el ID sin guion y con ceros a la izquierda

def borrar_columnas(df,archivo):

    if 'yellow' in archivo:
        df.drop(columns=['fare_amount', 'extra','mta_tax', 'tip_amount', 'tolls_amount', 
                        'improvement_surcharge','airport_fee','VendorID'],inplace=True)
    else:
        df.drop(columns=['fare_amount', 'extra','mta_tax', 'tip_amount', 'tolls_amount', 
                        'improvement_surcharge','VendorID','ehail_fee','trip_type'],inplace=True)
    return df

def etl_taxis(event, context):
    # Crea una instancia del cliente de Cloud Storage
    client = storage.Client()
    bucket = event['bucket']
    archivo = event['name']
    nombre_nuevo = f'{archivo[:-8]}_limpio.parquet'
    print()
    print()
    print(f'Archivo: {archivo}')

    if verificar_archivo_existente_2('procesados_sdt', nombre_nuevo):
        print()
        print()
        print(f'El archivo {nombre_nuevo} ya existe en el bucket "procesados_sdt". No se realizará el procesamiento.')
        print()
        print()
        return


    df = pd.read_parquet(f'gs://{bucket}/{archivo}', engine='pyarrow')
    
    shape_inicio = df.shape

    df = borrar_columnas(df,archivo)

    if 'yellow' in archivo:
        color = 'yellow'
        df= asignar_color(df,color)
    else: 
        color = 'green'
        df=asignar_color(df,color)

    year = int(archivo.split('_')[2].split('-')[0])


    if 'yellow' in archivo:
    
        df = ajuste_anio(df,year,'tpep_',)
    else:
        
        df = ajuste_anio(df,year,'lpep_',)
    
    
    df.insert(0,'viaje_Id', df.apply(generar_id,axis=1))

    revision_duplicados(df)


    #se tomó la decisión de eliminar las filas con negativos en esta columna ya que son devoluciones
    df.drop(df.loc[df['total_amount'] <0].index, inplace= True)
    # Reiniciar los índices del DataFrame después de eliminar filas
    df.reset_index(drop=True, inplace=True)

    # Calcular la mediana de la columna 'congestion_surcharge'
    mediana_congestion_surcharge = df['congestion_surcharge'].median()

    # Rellenar los valores nulos en 'congestion_surcharge' con la mediana calculada
    df['congestion_surcharge'].fillna(mediana_congestion_surcharge, inplace=True)
    
    #LLENAMOS LOS NULOS CON CEROS O EL DATO NECESARIO
    #cero se tomará como NA
    df['passenger_count'].fillna(0, inplace=True)
    df['RatecodeID'].fillna(0, inplace=True)
    df['payment_type'].fillna(0,inplace=True)
    #llenamos con N ya que no se tienen registros
    df['store_and_fwd_flag'].fillna('N',inplace=True)
    #cambiamos tipo de datos
    df['passenger_count'] = df['passenger_count'].astype(int)
    df['RatecodeID'] = df['RatecodeID'].astype(int)
    df['payment_type'] = df['payment_type'].astype(int)

    nuevos_nombres = {
    'PULocationID':'ubicacion_inicio',
    'DOLocationID':'ubicacion_fin',
    'RatecodeID': 'tipo_tarifa',
    'store_and_fwd_flag': 'conexion_servidor',
    'passenger_count':'pax',
    'trip_distance':'distancia_viaje',
    'total_amount': 'monto_total',
    'payment_type':'forma_pago',
    'congestion_surcharge':'cargo_congestion'
    }
    df.rename(columns=nuevos_nombres, inplace=True)

    
                     
    shape_final = df.shape
    print()
    print()
    print('Shape:')
    print()
    print()
    print(f'Inicio: {shape_inicio}   Final: {shape_final}')
    print()
    print()

    ruta = 'gs://procesados_sdt/'
    df.to_parquet(f'{ruta}{archivo[:-8]}_limpio.parquet')