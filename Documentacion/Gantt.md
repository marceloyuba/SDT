### Diagrama de gantt / organizacion de tareas
```mermaid
gantt
   
    dateFormat  YYYY-MM-DD
    excludes     saturday sunday
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section Cristian
    
    Data warehouse            :  des4, 2024-04-01, 3d
    Automatización             :    des11, 2024-04-08, 4d
    Documentacion DataWarehouse       : a1, after des4, 5d
    Implementacion DW         :    des7, 2024-04-08, 4d
    DW                          :    des10, 2024-04-08, 4d
    Informe de análisis               :    des25, 2024-04-15, 3d
    Workflow detallando tecnologías :    des15, 2024-04-08, 4d
    Migración de datos a git        :    des12, 2024-04-08, 4d

   section Elizabeth

    ETL                       :    des1, 2024-04-01, 3d 
    ETL completo               :    des6, 2024-04-08, 4d
    Documentacion ETL               :active, a1, after des1, 5d
    Diccionarios de datos             : a1, after des1, 5d
    Pipeline ETL               :    des8, 2024-04-08, 4d
    Diseño Modelo ER           :    des8, 2024-04-08, 4d 
    Pipeline Alimentar DW       :    des9, 2024-04-08, 4d
    Validación de datos         :    des12, 2024-04-08, 4d
    Informe de análisis               :   des25, 2024-04-15, 3d
    Análisis de datos de muestra   :   des16, 2024-04-08, 4d
    creacion github         :    des1, 2024-04-01, 3d 
   
    
    

    section Ingrid
    KPI's                     :   des3,  2024-04-01, 3d
    Diseño Dashboards              :    des20, 2024-04-15, 3d
    KPIs                           :   des21, 2024-04-15, 3d
    Documentacion KPI's              : a1, after des1, 5d
    Github                          : 2024-04-15, 3d
    Informe de análisis               :   des25, 2024-04-15, 3d
    Guion del video                  :    des26, 2024-04-15, 3d
    Video del proyecto              :  des27, 2024-04-15, 3d
    


    section Marcelo
    EDA                          :  des2, 2024-04-01, 3d
    Documentacion EDA              : a1, after des1, 5d
    Diseño Modelo ER           :    des8, 2024-04-08, 4d
    Validación de datos         :    des12, 2024-04-08, 4d
    Diagrama ER Detallado       :    des13, 2024-04-08, 4d
    Steamlit                     :    des18, 2024-04-08, 4d
    Informe de análisis               :    des25, 2024-04-15, 3d
    Análisis de datos de muestra   :   des16, 2024-04-08, 4d
    Github                          : 2024-04-15, 3d

    section Josue
    ML                           : des5, 2024-04-01, 3d
    Documentacion ML                   : a1, after des1, 5d
    Selección del modelo         :    des24, 2024-04-15, 3d
    Modelos de ML                   :    des22, 2024-04-15, 3d
    Modelo de ML en producción      :    des23, 2024-04-15, 3d
    Implementacion de los endpoints     :    des19, 2024-04-08, 4d
    Informe de análisis               :    des25, 2024-04-15, 3d

    section Hitos
    PPT D1                              :crit,  2024-04-05,24h
    PPT D2                              :crit,  2024-04-11,24h
    Precentacion Final                          :crit,  2024-04-19,24h
    Definir roles                       :milestone, isadded, 2024-04-01, 0d
    Descarga datasets                   :milestone, isadded, 2024-04-01, 24h
    Definir DataWarehouse               :milestone,isadded, 2024-04-01, 24h
    Subir datasets                      :milestone,isadded 2024-04-04, 2d

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
