
![rendered image description](imagenes/SDTLogo.png)

# <h1 align="center"> **NYC Autos Greyhound** <br> Proyecto Final </h1>

## ¿Quiénes Somos?

Somos **Strategic Data Transform**, una consultora empresarial, que presta servicios de consultoría tecnológica en el área de Data Science a empresas que quieran cumplir sus objetivos de éxito a partir de los datos.

## Objetivo del Proyecto 

El proyecto esta orientado a realizar un estudio de viabilidad para nuestro cliente Greyhound, quién se encuentra laborando en el sector del transporte con micros de media y larga distancia, y ahora quiere incursionar en el sector de trasnporte de pasajeros en la ciudad de Nueva York con autos que tengan un bajo impacto ambietal.


<div align="center">

![Logo_Greyhound](imagenes/logo_greyhound.png)
</div>

Greyhound quiere determinar que tipo de vehículo es el más óptimo para cada destino de viaje y asimismo contar con un estudio que le muestre si la viabilidad de realizar el proyecto con sus requerimientos es positiva, lo que conlleva a que nosotros como consultora hagamos diversos análisis de rentabilidad, impacto ambiental y viabilidad en el mercado de diferentes formas. 
En este proyecto también se analizará el comportamiento frente a sus competidores directos (Taxis, Uber y Lyft) en la ciudad, lo cual brindará un contexto de análisis mucho más completo y amplio. 

Para poder realizar el estudio se tomo como fuente de datos la siguiente página web: [Taxi & Limousine Commission](https://www.nyc.gov/site/tlc/index.page)

Este proyecto consta de tres fases principales que se realizan implementando métodologías ágiles como Scrum, realizando reuniones diarias con el Product Manager para debatir los avances y reuniones semanales con el Product Owner para mostrar los entregables a cada fecha. Estas fases se cumplen gracias al equipo de trabajo conformado en los siguientes roles por:

- Cristian Fontanilla - Data Engineer
- Elizabeth Torres - Data Engineer
- Ingrid Barrios - Data Analyst
- Marcelo Yuba - Data Analyst
- Josue Mora - Data Scientist

Así que a continuación se explicará que conlleva cada fase de este proyecto, que métodos y herramientas se usaron, y asimismo que análisis se realizaron.

<div align="center">

![Taxis](imagenes/taxis-nueva-york.jpeg)
</div>

## **Sprint 1**

En este primer sprint se hace el planteamiento del proyecto entendiendo la situación actual realizando un EDA preliminar, se plantean los obejtivos general y específicos, el alcance del proyecto, se determianan los KPIs y las métricas a utilizar. 

También se plantea el [*Stack Tecnológico*](https://github.com/micjb/FinalProject/blob/main/imagenes/Stack_tecnologico.jpg) a utilizar a lo largo del proyecto, con el debido cronograma en un [*diagrama de Gantt*](https://github.com/micjb/FinalProject/blob/main/Documentacion/Gantt.md) y las tareas delegadas para los diferentes roles y sus metodologías.


### Objetivo General del Proyecto
Estudiar la viabilidad de incorporar vehículos eléctricos de transporte de pasajeros en la ciudad de Nueva York, con el fin de reducir la contaminación, de manera que sea rentable para la empresa, precisando la concentración en la demanda de los tipos de vehículos en las diferentes áreas de la ciudad.

Y asimismo planteamos estos objetivos especificos como pilares para el desarrollo del mismo:

- Analizar la viabilidad del proyecto teniendo en cuenta métricas de la demanda del mercado, para determinar cuáles serían los autos más recomendados para incursionar en este sector del transporte. 

- Analizar los factores ambientales, ya que se quiere incursionar con vehículos que no generen tanta contaminación, teniendo en cuenta el tiempo de pre, durante y post pandemia como referencia del impacto ambiental en términos de calidad del aire. 

- Evaluar el comportamiento del mercado con la nueva inversión de autos, con métricas relacionadas al número de viajes realizados, distancias recorridas por zonas, viajes entre las distintas zonas, estudio de tiempos de más alta demanda, entre otras. 

### Indicadores Clave de Desempeño (KPIs)
 
**Para la viabilidad se propone:**

**- Eficiencia operativa: Distancia recorrida por periodo de tiempo**

Midiendo la distancia recorrida por los autos estudiados, podremos ver el comportamiento operativo, si aumenta o reduce la operación, así como también se puede ver que tanta es la acogida en el mercado.
Este KPI es un indicativo de la viabilidad del proyecto, ya que a más distancia de actividad va a ser más sostenible el negocio en el tiempo.

**Para el impacto ambiental se propone:**

**- Emisiones de CO2**

Podemos medir el impacto en la calidad del aire de los autos con los que operará Greyhound midiendo las emisiones de CO2, donde se pueden hacer análisis comparando las emisiones de los vehículos tradicionales de combustión interna, en periodos de tiempo diferentes.
Este KPI se formula alineado con las prioridades del cliente de querer tener un menor impacto ambiental.

Para poder formular este KPI se hizo una revisión de la data de los gases de efecto invernadero que deja el sector del transporte en la ciudad de Nueva York, tomada de [NYC Greenhouse Gas Inventories](https://climate.cityofnewyork.us/initiatives/nyc-greenhouse-gas-inventories/), de donde se calcula una tasa de emisiones de CO2 generada por unidad de energía consumida en BUT, la cual se toma de la distancia recorrida por los autos. 

**Para la aceptación en el mercado se propone medir:**

**- Ingresos en viajes por periodo de tiempo**

Con este KPI se quiere medir si los ingresos de dinero por cada viaje aumentan con el pasar del tiempo, para este caso se planea un análisis con un aumento del 15% de ingresos para el año siguiente, teniendo en cuenta las demás cifras económicas de la ciudad. Con esta metríca podremos analizar si aumentan los ingresos junto con la cantidad de viajes. 

Los detalles de los KPIs formulados se pueden ver [aquí.](https://github.com/micjb/FinalProject/blob/main/KPIs)

## **Sprint 2**

En esta segunda fase se organiza la infraestructura del proyecto con almacenamiento en la nube, desarrollando el pipeline completo para realizar el proceso de ETL automatizado, mediante **Google Cloud Plataform**.
También se hizo un proceso de ETL local, el cual contribuyó en el desarrollo posterior del ETL automatizado, junto con el desarrollo de las funciones que desplegarían todo el proceso. La información más detallada de este proceso se puede ver en la carpeta de la documentación que está [aquí.](https://github.com/micjb/FinalProject/tree/main/Documentacion)
Asimismo, la información más detallada del código del ETL la encuentras en la carpeta de este repositorio llamada [ETL.](https://github.com/micjb/FinalProject/tree/main/ETL)

Para lograr esto, se plantea un workflow desde el almacenamiento de los datos en el storage, creando un *bucket* de almacenamiento que reciban los datos cargados mediante *webscrapping*.
Más detalles de la forma en como se hizo el scrapping está en el repositprio y se pude ver aquí: [**Scrapping.**](https://github.com/micjb/FinalProject/tree/main/Scraping)

Seguido del esto, se crean [**Cloud Functions**](https://github.com/micjb/FinalProject/tree/main/ETL/Functions%20GCP) con los scripts que hacen el ETL, para que cada vez que se cargue un archivo en el storage se active la cloud function para que realice el proceso de ETL automatizado, y una vez hecho el ETL se activa otra cloud function para enviar el dataset ya transformado y limpio a **BigQuery**.

Una vez esté almacenado el dataset limpio en BigQuery, estará disponible para hacer las consultas que se requieran, y también para poderse conectar con las demás herramientas para el proceso de análisis posterior. 

## **Sprint 3**

En esta última fase se tienen como actividades principales la realización del Dashboard interactivo, la realización de un EDA profundo junto con sus respectivos análisis y conclusiones y la realización del modelo de machine learning deployado. 

El dashborad fue realizado en *Power BI*, mostrando de manera interactiva el relacionamiento de los datos de los Taxis de NYC, datos de Uber y de Lyft, con el fin de realizar análisis de competidores. También se encuentran los KPIs debidamente representados para medir los ítems principales del proyecto. 


### Streamlit 




 





