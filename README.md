# FinalProject
![rendered image description](Imagenes/NYC.jpg)

<details>
  <summary>diagram source</summary>
  This details block is collapsed by default when viewed in GitHub. This hides the mermaid graph definition, while the rendered image
  linked above is shown. The details tag has to follow the image tag. (newlines allowed)

```mermaid
gantt
    title Semana 1

  section Elizabeth
    ETL           :a1, 2024-04-01, 4d
    ETL Doc    :after a1, 2024-04-03, 3d

    section Marcelo
    EDA           :a2, 2024-04-01, 4d
    EDA Doc       :2024-04-03, 3d

    section Cristian
     ETL           :a3, 2024-04-10, 4d
    Task Cristian    :after a3 + 2d, 20d
    Final Cristian    : 2024-05-22  , 12d

    section Josue
     ETL           :a4, 2024-04-15, 4d
    Task Josue    :after a4 + 2d, 20d
    Final Josue    : 2024-05-27  , 12d

    section Ingrid
    KPI's          :a5, 2024-04-01, 4d
    Doc KPI's       :2024-04-03, 3d
    Final Ingrid    : 2024-06-01  , 12d


```
</details>
