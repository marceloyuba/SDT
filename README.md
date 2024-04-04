# FinalProject
![rendered image description](Imagenes/NYC.jpg)

<details>
  <summary>diagram source</summary>
  This details block is collapsed by default when viewed in GitHub. This hides the mermaid graph definition, while the rendered image
  linked above is shown. The details tag has to follow the image tag. (newlines allowed)

```mermaid
gantt
    title Diagrama de Gantt

  section Elizabeth
    ETL           :a1, 2024-04-01, 4d
    ETL Doc    :after a1, 2024-04-03, 3d

    section Marcelo
    EDA           :a2, 2024-04-01, 4d
    EDA Doc       :2024-04-03, 3d

    section Cristian
    DataWarehouse      :a3, 2024-04-01, 4d
    Docs               :2024-04-03, 3d
    
    section Josue
     ML           :a4, 2024-04-01, 4d
    ML Doc        :2024-04-03, 3d
    

    section Ingrid
    KPI's          :a5, 2024-04-01, 4d
    Doc KPI's       :2024-04-03, 3d
   

```
</details>
