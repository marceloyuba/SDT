
![rendered image description](imagenes/SDTLogo.png)

<details>
 

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Diagrama de Gantt del Proyecto Final
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2024-04-06,2024-04-08
    Active task               :active,  des2, 2024-04-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Hitos
    PPT DEMO 1                          :crit, done, 2024-04-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :until isadded
    Subir datasets                      :milestone, isadded, 2024-04-04, 0d

    section Documentación
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Ensayo DEMO
    Ensayo DEMO 1                       :done, after 2024-04-05, 0d

    section Daily
    Meet                               :active, a1, 2024-04-01, 25d
    DEMO 1                             :after a1, 2024-04-05, 0d
    DEMO 2                             :after Meet, 2024-04-12, 0d
    DEMO 3                             :after DEMO 2, 2024-04-19, 0d

```
</details>


<details>
 

```mermaid
gantt
    apple :a, 2017-07-20, 1w
    banana :crit, b, 2017-07-23, 1d
    cherry :active, c, after b a, 1d
    kiwi   :d, 2017-07-20, until b c

```
</details>
