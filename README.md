
![rendered image description](imagenes/SDTLogo.png)

### Diccionarios de datos

| Nombre de la columna    | Descripción                                            | Tipo de dato | Tipo de variable |
|-------------------------|--------------------------------------------------------|--------------|------------------|
| Vendor ID               | Identificador de proveedor                             | int          | Cualitativa      |
| tpep_pickup_datetime    | Fecha inicio del viaje                                 | datetime     | Cuantitativa     |
| tpep_dropoff_datetime   | Fecha fin del viaje                                    | datetime     | Cuantitativa     |
| Passenger_count         | Número de pasajeros                                    | float        | Cuantitativa     |
| Trip_distance           | Distancia del viaje                                    | float        | Cuantitativa     |
| PULocationID            | Identificador de la ubicación de inicio                | int          | Cualitativa      |
| DOLocationID            | Identificador de la ubicación final                    | int          | Cualitativa      |
| RateCodeID              | Identificador de tarifa final vigente al finalizar el viaje | float   | Cualitativa      |
| Store_and_fwd_flag      | Marca de almacenamiento y reenvío                      | object       | Cualitativa      |
| Payment_type            | Forma de pago                                          | float        | Cualitativa      |
| Fare_amount             | Tarifa de tiempo y distancia calculada                 | float        | Cuantitativa     |
| Extra                   | Recargos por hora pico y por noche                    | float        | Cuantitativa     |
| MTA_tax                 | Impuesto MTA que se cobra según la tarifa              | float        | Cuantitativa     |
| Improvement_surcharge   | Recargo por mejora                                     | float        | Cuantitativa     |
| Tip_amount              | Propinas                                               | float        | Cuantitativa     |
| Tolls_amount            | Importe total de todos los peajes                      | float        | Cuantitativa     |
| Total_amount            | Importe total cobrado a los pasajeros                  | float        | Cuantitativa     |
| Trip_type               | Identifica si el viaje fue en calle o asignado         | float        | Cualitativa      |
| Congestion_Surcharge    | Monto total cobrado por congestión en NY               | float        | Cuantitativa     |



### Diagrama de gantt / organizacion de tareas
```mermaid
gantt
   
    dateFormat  YYYY-MM-DD
    excludes     saturday sunday
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section Tareas semana 1
    ETL                       :done,    des1, 2024-04-01, 3d
    EDA                       :done,  des2, 2024-04-01, 3d
    KPI's                     :done,   des3,  2024-04-01, 3d
    Data warehouse            :done,   des4, 2024-04-01, 3d
    ML                        :done, des5, 2024-04-01, 3d               

    section Tareas semana 2            
    ETL completo               :active,    des6, 2024-04-08, 4d
    Implementacion DW         :active,    des7, 2024-04-08, 4d
    Pipeline ETL               :active,    des8, 2024-04-08, 4d
    Diseño Modelo ER           :active,    des8, 2024-04-08, 4d 
    Pipeline Alimentar DW       :active,    des9, 2024-04-08, 4d
    DW                          :active,    des10, 2024-04-08, 4d
    Automatización             :active,    des11, 2024-04-08, 4d
    Validación de datos         :active,    des12, 2024-04-08, 4d
    Diagrama ER Detallado       :active,    des13, 2024-04-08, 4d
    Diccionario de datos        :active,    des14, 2024-04-08, 4d
    Workflow detallando tecnologías :active,    des15, 2024-04-08, 4d
    Análisis de datos de muestra   :active,    des16, 2024-04-08, 4d
    Concepto del Proyecto         :active,    des17, 2024-04-08, 4d
    Steamlit                     :active,    des18, 2024-04-08, 4d
    Implementacion de los endpoints     :active,    des19, 2024-04-08, 4d

    section Tareas semana 3           
    Diseño Dashboards              :active,    des20, 2024-04-15, 3d
    KPIs                           :active,    des21, 2024-04-15, 3d
    Modelos de ML                   :active,    des22, 2024-04-15, 3d
    Modelo de ML en producción      :active,    des23, 2024-04-15, 3d
    Selección del modelo         :active,    des24, 2024-04-15, 3d
    Informe de análisis               :active,    des25, 2024-04-15, 3d
    Guion del video                  :active,    des26, 2024-04-15, 3d
    Video del proyecto              :active,    des27, 2024-04-15, 3d
    Streamlit                       :active, des28, 2024-04-15, 3d

    section Hitos
    PPT D1                              :crit,  2024-04-05,24h
    PPT D2                              :crit,  2024-04-11,24h
    Precentacion Final                          :crit,  2024-04-19,24h
    Definir roles                       :milestone, isadded, 2024-04-01, 0d
    Descarga datasets                   :milestone, isadded, 2024-04-01, 24h
    Definir DataWarehouse               :milestone,isadded, 2024-04-01, 24h
    Subir datasets                      :milestone,isadded 2024-04-04, 2d

    section Documentación
    Documentacion ETL               :active, a1, after des1, 10d
    Documentacion EDA              :active, a1, after des1, 10d
    Documentacion KPI's              :active, a1, after des1, 10d
    Documentacion DataWarehouse       :active, a1, after des1, 10d
    Documentacion ML                   :active, a1, after des1, 10d
    
    section Ensayo DEMO
    Ensayo DEMO 1                       :active, 2024-04-05, 5h
    Ensayo DEMO 2                       :active, 2024-04-11, 5h
    Ensayo DEMO Final                  :active, 2024-04-18, 5h

    section Daily
    Meet                               :active,a2, 2024-04-01, 2024-04-18
    DEMO 1                             :active, 2024-04-05, 1h
    DEMO 2                             :active, 2024-04-12, 1h
    DEMO Final                             :active, 2024-04-19, 1h
   
```



 





