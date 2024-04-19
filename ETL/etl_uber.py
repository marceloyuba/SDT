import pandas as pd

#scrapeamos los datasets
url_1_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-01.parquet"
fh_1_22 = pd.read_parquet(url_1_22)
url_2_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-02.parquet"
fh_2_22 = pd.read_parquet(url_2_22)
url_3_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-03.parquet"
fh_3_22 = pd.read_parquet(url_3_22)
url_4_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-04.parquet"
fh_4_22 = pd.read_parquet(url_4_22)
url_5_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-05.parquet"
fh_5_22 = pd.read_parquet(url_5_22)
url_6_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-06.parquet"
fh_6_22 = pd.read_parquet(url_6_22)
url_7_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-07.parquet"
fh_7_22 = pd.read_parquet(url_7_22)
url_8_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-08.parquet"
fh_8_22 = pd.read_parquet(url_8_22)
url_9_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-09.parquet"
fh_9_22 = pd.read_parquet(url_9_22)
url_10_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-10.parquet"
fh_10_22 = pd.read_parquet(url_10_22)
url_11_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-11.parquet"
fh_11_22 = pd.read_parquet(url_11_22)
url_12_22 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-12.parquet"
fh_12_22 = pd.read_parquet(url_12_22)
url_1_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-01.parquet"
fh_1_23 = pd.read_parquet(url_1_23)
url_2_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-02.parquet"
fh_2_23 = pd.read_parquet(url_2_23)
url_3_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-03.parquet"
fh_3_23 = pd.read_parquet(url_3_23)
url_4_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-04.parquet"
fh_4_23 = pd.read_parquet(url_4_23)
url_5_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-05.parquet"
fh_5_23 = pd.read_parquet(url_5_23)
url_6_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-06.parquet"
fh_6_23 = pd.read_parquet(url_6_23)
url_7_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-07.parquet"
fh_7_23 = pd.read_parquet(url_7_23)
url_8_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-08.parquet"
fh_8_23 = pd.read_parquet(url_8_23)
url_9_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-09.parquet"
fh_9_23 = pd.read_parquet(url_9_23)
url_10_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-10.parquet"
fh_10_23 = pd.read_parquet(url_10_23)
url_11_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-11.parquet"
fh_11_23 = pd.read_parquet(url_11_23)
url_12_23 = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2023-12.parquet"
fh_12_23 = pd.read_parquet(url_12_23)

#concatenamos los datasets

df_2022_fh = pd.concat([fh_1_22, fh_2_22, fh_3_22, fh_4_22, fh_5_22, fh_6_22, fh_7_22, fh_8_22, fh_9_22, fh_10_22, fh_11_22, fh_12_22], ignore_index=True)
df_2023_fh = pd.concat([fh_1_23, fh_2_23, fh_3_23, fh_4_23, fh_5_23, fh_6_23, fh_7_23, fh_8_23, fh_9_23, fh_10_23, fh_11_23, fh_12_23], ignore_index=True)

#liberamos memoria
del fh_1_22, fh_2_22, fh_3_22, fh_4_22, fh_5_22, fh_6_22, fh_7_22, fh_8_22, fh_9_22, fh_10_22, fh_11_22, fh_12_22
del fh_1_23, fh_2_23, fh_3_23, fh_4_23, fh_5_23, fh_6_23, fh_7_23, fh_8_23, fh_9_23, fh_10_23, fh_11_23, fh_12_23

#filtramos las columnas que necesitamos
df_2022_fh = df_2023_fh[['hvfhs_license_num','request_datetime','on_scene_datetime','pickup_datetime','dropoff_datetime','PULocationID', 'DOLocationID','trip_miles','trip_time','congestion_surcharge','driver_pay','shared_request_flag','shared_match_flag','wav_request_flag','wav_match_flag']]
df_2023_fh = df_2022_fh[['hvfhs_license_num','request_datetime','on_scene_datetime','pickup_datetime','dropoff_datetime','PULocationID', 'DOLocationID','trip_miles','trip_time','congestion_surcharge','driver_pay','shared_request_flag','shared_match_flag','wav_request_flag','wav_match_flag']]

#verificamos duplicados
df_2022_fh.duplicated().sum()
df_2023_fh.duplicated().sum()

#eliminamos duplicados
df_2022_fh.drop_duplicates(inplace=True)
df_2022_fh.reset_index(drop=True, inplace=True)
df_2023_fh.drop_duplicates(inplace=True)
df_2023_fh.reset_index(drop=True, inplace=True)


#agregamos la columna que identifica el tipo de color 
def asignar_color(df_viajes,color):
    def asignar_color_por_location(location):
        if location  in ['HV0003']:
            return color
        else:
            return 'Lyft'

    df_viajes['tipo_color'] = df_viajes['hvfhs_license_num'].apply(asignar_color_por_location)
    return df_viajes

df_2022_fh= asignar_color(df_2022_fh,'Uber')
df_2023_fh= asignar_color(df_2023_fh,'Uber')

#eliminamos la columna 'hvfhs_license_num'
df_2022_fh.drop(columns='hvfhs_license_num',inplace=True)
df_2023_fh.drop(columns='hvfhs_license_num',inplace=True)

#FUNCION PARA VALIDAR SI EL AÑO ES CORRECTO DE LO CONTRARIO ELIMINARLO y SEPARAR LA COLUMNA DE LA FECHA
def ajuste_anio(df,year,col_prefix,col_prefix2,col_prefix3,col_prefix4):
    # Obtiene todas las columnas que comienzan con el prefijo dado
    pickup_col = [col for col in df.columns if col.startswith(col_prefix2 + 'datetime')]
    dropoff_col = [col for col in df.columns if col.startswith(col_prefix3 + 'datetime')]

    # Filtra las filas donde las fechas no coinciden con el año del df
    df = df[(df[pickup_col[0]].dt.year == year) & (df[dropoff_col[0]].dt.year == year)]
    # Separar las columnas de fecha y hora en componentes individuales
    df['anio'] = df[col_prefix + 'datetime'].dt.year
    df['mes'] = df[col_prefix + 'datetime'].dt.month
    df['dia'] = df[col_prefix + 'datetime'].dt.day
    df['hora_pedido'] = df[col_prefix + 'datetime'].dt.time
    
    df['hora_encuentro'] = df[col_prefix2 + 'datetime'].dt.time
    df['hora_inicio'] = df[col_prefix3 + 'datetime'].dt.time
    df['hora_fin'] = df[col_prefix4 + 'datetime'].dt.time
    
    
    df.drop(columns=[col_prefix +'datetime',col_prefix2 + 'datetime', col_prefix3 + 'datetime', col_prefix4 + 'datetime'],inplace= True)
    # Reestablece los índices
    df.reset_index(drop=True, inplace=True)
   
    return df

#llamamos a la funcion 
df_2022_fh = ajuste_anio(df_2022_fh,2022,'request_','on_scene_','pickup_','dropoff_')
df_2023_fh = ajuste_anio(df_2023_fh,2023,'request_','on_scene_','pickup_','dropoff_')

#se tomó la decisión de eliminar las filas con negativos en esta columna ya que son devoluciones
df_2022_fh.drop(df_2022_fh.loc[df_2022_fh['driver_pay'] <0].index, inplace= True)
df_2023_fh.drop(df_2023_fh.loc[df_2023_fh['driver_pay'] <0].index, inplace= True)
# Reiniciar los índices del DataFrame después de eliminar filas
df_2022_fh.reset_index(drop=True, inplace=True)
df_2023_fh.reset_index(drop=True, inplace=True)

# Calcular la mediana de la columna 'congestion_surcharge'
mediana_congestion_surcharge = df_2022_fh['congestion_surcharge'].median()
mediana_congestion_surcharge = df_2023_fh['congestion_surcharge'].median()
# Rellenar los valores nulos en 'congestion_surcharge' con la mediana calculada
df_2022_fh['congestion_surcharge'].fillna(mediana_congestion_surcharge, inplace=True)
df_2023_fh['congestion_surcharge'].fillna(mediana_congestion_surcharge, inplace=True)


#LLENAMOS LOS NULOS CON CEROS O EL DATO NECESARIO
#cero se tomará como NA
df_2022_fh['driver_pay'].fillna(0, inplace=True)
df_2022_fh['trip_miles'].fillna(0, inplace=True)

#llenamos con N ya que no se tienen registros
df_2022_fh['shared_request_flag'].fillna('N',inplace=True)
df_2022_fh['shared_match_flag'].fillna('N',inplace=True)
df_2022_fh['wav_request_flag'].fillna('N',inplace=True)
df_2022_fh['wav_match_flag'].fillna('N',inplace=True)

#LLENAMOS LOS NULOS CON CEROS O EL DATO NECESARIO
#cero se tomará como NA
df_2023_fh['driver_pay'].fillna(0, inplace=True)
df_2023_fh['trip_miles'].fillna(0, inplace=True)

#llenamos con N ya que no se tienen registros
df_2023_fh['shared_request_flag'].fillna('N',inplace=True)
df_2023_fh['shared_match_flag'].fillna('N',inplace=True)
df_2023_fh['wav_request_flag'].fillna('N',inplace=True)
df_2023_fh['wav_match_flag'].fillna('N',inplace=True)

def generar_id_hora(row):
    fila = row.name + 1  # Obtener el número de fila
    hora_inicio = str(row['hora_inicio'])[-2:].zfill(2)  # Obtener la hora de inicio y rellenar con ceros a la izquierda si es necesario
    return f"{fila:013}{hora_inicio:02}"  # Formar el ID sin guion y con ceros a la izquierda

df_2022_fh.insert(0,'viaje_Id', df_2022_fh.apply(generar_id_hora,axis=1))
df_2023_fh.insert(0,'viaje_Id', df_2023_fh.apply(generar_id_hora,axis=1))

#Renombramos columnas
nuevos_nombres = {
    'PULocationID':'ubicacion_inicio',
    'DOLocationID':'ubicacion_fin',
    'trip_miles':'distancia_viaje',
    'trip_time':'tiempo_viaje',
    'congestion_surcharge':'cargo_congestion',
    'driver_pay': 'pago_total',
    'shared_request_flag': 'viaje_compartido_pedido',
    'shared_match_flag':  'viaje_compartido_encontrado',
    'wav_request_flag': 'accesibilidad_requerida',
    'wav_match_flag': 'accesibilidad_espontanea'
}

df_2022_fh.rename(columns=nuevos_nombres, inplace=True)
df_2023_fh.rename(columns=nuevos_nombres, inplace=True)