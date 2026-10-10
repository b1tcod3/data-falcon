# repositorio de investigacion en programacion-general, ciencia-de-datos e inteligencia-artificial

este repositorio contiene una coleccion de codigo, tutoriales, cursos y proyectos relacionados con programacion general, ciencia de datos, inteligencia artificial, estadisticas y metodologias relacionadas. sirve como recurso de investigacion y aprendizaje, organizado por area y **ordenado por complejidad**: desde los fundamentos de programacion hasta las redes neuronales.

## orden de estudio sugerido

recorrido recomendado de menor a mayor complejidad:

1. **fundamentos de programacion** — [condicionales, bucles y casting (python)](./programacion-general/tutorials/fundamentos/) y [gestion de memoria (c)](./programacion-general/tutorials/memoria/)
2. **programacion aplicada** — [manejo de archivos](./programacion-general/code/file-handling/python/archivos/), [sql](./programacion-general/code/sql/), [excel](./programacion-general/code/excel/python/excel/) e [interfaces graficas](./programacion-general/code/gui/python/)
3. **algoritmos y estructuras de datos** — [tutorial de estructura de datos (go)](./programacion-general/tutorials/estructura-de-datos/) y [codigo](./programacion-general/code/estructura-datos/)
4. **analisis de datos** — [introduccion a la ciencia de datos](./ciencia-de-datos/tutorials/intro-ciencia-datos/), [manipulacion con pandas](./ciencia-de-datos/code/data-manipulation/python/pandas/), [visualizacion](./ciencia-de-datos/code/visualization/python/) y [estadistica descriptiva](./ciencia-de-datos/code/statistics/python/stat/)
5. **estadistica inferencial y matematicas** — [probabilidad](./ciencia-de-datos/code/statistics/python/probabilidad/), [muestreo](./ciencia-de-datos/code/statistics/python/stat/muestreo/), [algebra lineal](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/), [pca](./ciencia-de-datos/code/pca/python/pca/) y [modelos avanzados](./ciencia-de-datos/code/statistics/python/stat/)
6. **aprendizaje automatico** — [machine learning](./inteligencia-artificial/code/machine-learning/python/machine-learning/), [pytorch](./inteligencia-artificial/code/ai/python/ai/pytorch/) y [redes neuronales](./inteligencia-artificial/code/neural-networks/python/ia/)
7. **practica** — [proyectos completos](./programacion-general/code/projects/)

## contenido ordenado por complejidad

### programacion-general

**fundamentos (basico)**
- condicionales: [simples](./programacion-general/tutorials/fundamentos/condicionales.py), [multiples](./programacion-general/tutorials/fundamentos/condicionales-multiples.py) y [en linea](./programacion-general/tutorials/fundamentos/condicionales-en-linea.py)
- bucles: [for sobre secuencias](./programacion-general/tutorials/fundamentos/bucles.py)
- tipos y operaciones: [casting](./programacion-general/tutorials/fundamentos/casting.py)
- practica: [calculadora](./programacion-general/tutorials/fundamentos/calculadora-casting.py) y [calculadora con menu](./programacion-general/tutorials/fundamentos/calculador.py)
- memoria (c): [fuga de memoria](./programacion-general/tutorials/memoria/memoria-leak.c)

**manejo de archivos (basico)**
- [lectura](./programacion-general/code/file-handling/python/archivos/lectura.py), [escritura](./programacion-general/code/file-handling/python/archivos/escritura.py) y [lectura completa](./programacion-general/code/file-handling/python/archivos/manejo-archivo-lectura.py) de archivos
- [manejo de errores](./programacion-general/code/file-handling/python/archivos/manejo-errores.py)

**sql (basico-intermedio)**
- python: [conexion](./programacion-general/code/sql/python/sql/basico/connection.py), [select](./programacion-general/code/sql/python/sql/basico/select.py), [where](./programacion-general/code/sql/python/sql/basico/where.py), [order](./programacion-general/code/sql/python/sql/basico/order.py), [insert](./programacion-general/code/sql/python/sql/basico/insert.py), [update](./programacion-general/code/sql/python/sql/basico/update.py), [delete](./programacion-general/code/sql/python/sql/basico/delete.py) y [drop](./programacion-general/code/sql/python/sql/basico/drop.py)
- [creacion de tablas](./programacion-general/code/sql/python/sql/create-table/create-table.py), [insercion masiva](./programacion-general/code/sql/python/sql/insert/insert.py) y [consultas](./programacion-general/code/sql/python/sql/query/query.py)
- postgresql: [analisis de ventas](./programacion-general/code/sql/postgre/basico/analisis_venta.sql), [crecimiento de ventas](./programacion-general/code/sql/postgre/basico/crecimiento_ventas.sql), [prediccion de ventas](./programacion-general/code/sql/postgre/basico/prediccion_ventas.py) y [procesamiento por lotes](./programacion-general/code/sql/postgre/basico/chunking-ventas.py)
- bases de prueba: [employees](./programacion-general/code/sql/python/sql/tests_db/) y [sakila](./programacion-general/code/sql/python/sql/tests_db/sakila/)

**excel (basico-intermedio)**
- [estilos con openpyxl](./programacion-general/code/excel/python/excel/style-excel.py)

**interfaces graficas (intermedio)**
- [tkinter: registro](./programacion-general/code/gui/python/tkinter/registro/registro.py)
- [pyside6: registro](./programacion-general/code/gui/python/pyside6/registro/registro.py) y [pruebas](./programacion-general/code/gui/python/pyside6/testing.py)

**estructura de datos y algoritmos (intermedio-avanzado)**
- tutorial completo: [estructura de datos y algoritmos](./programacion-general/tutorials/estructura-de-datos/) — [notacion o](./programacion-general/tutorials/estructura-de-datos/01-introduccion-y-notacion-o.md), [bubble sort](./programacion-general/tutorials/estructura-de-datos/02-bubble-sort.md), [selection sort](./programacion-general/tutorials/estructura-de-datos/03-selection-sort.md), [insertion sort](./programacion-general/tutorials/estructura-de-datos/04-insertion-sort.md), [quick sort](./programacion-general/tutorials/estructura-de-datos/05-quick-sort.md), [benchmark](./programacion-general/tutorials/estructura-de-datos/06-benchmark-de-ordenamientos.md), [colas y pilas](./programacion-general/tutorials/estructura-de-datos/07-colas-y-pilas.md), [listas enlazadas](./programacion-general/tutorials/estructura-de-datos/08-listas-enlazadas.md), [arboles binarios](./programacion-general/tutorials/estructura-de-datos/09-arboles-binarios-de-busqueda.md) y [grafos](./programacion-general/tutorials/estructura-de-datos/10-grafos.md)
- ordenamientos (go): [sorts](./programacion-general/code/estructura-datos/sorts/) y [benchmark](./programacion-general/code/estructura-datos/benchmark/)
- estructuras lineales (go): [cola](./programacion-general/code/estructura-datos/cola/), [pila](./programacion-general/code/estructura-datos/pila/), [lista enlazada](./programacion-general/code/estructura-datos/listas-enlazadas/) y [lista doble](./programacion-general/code/estructura-datos/doubly-linked-list/)
- arboles (go): [arbol binario de busqueda](./programacion-general/code/estructura-datos/arbol-binario/)
- grafos (go): [red social](./programacion-general/code/estructura-datos/grafo/social-graph/), [bfs](./programacion-general/code/estructura-datos/grafo/bfs-graph/), [dijkstra](./programacion-general/code/estructura-datos/grafo/dijkstra/) y [mapas ordenados](./programacion-general/code/estructura-datos/grafo/mapas-ordenados/)

**cursos (intermedio-avanzado)**
- [conceptos basicos](./programacion-general/code/courses/conceptos-basico/)
- [rust: fundamentos](./programacion-general/code/courses/rust/basic/), [proyectos](./programacion-general/code/courses/rust/projects/) y [tui](./programacion-general/code/courses/rust/tui-tut/)
- [dart](./programacion-general/code/courses/dart/)
- [polars](./programacion-general/code/courses/polars/practices/series/basico.py)
- [django: recetas](./programacion-general/code/courses/django/testing-project/)
- [advanced python: optimizacion](./programacion-general/code/courses/advance-python/pure-optimization/) y [benchmarking y profiling](./programacion-general/code/courses/advance-python/benchmarking-profiling/)

**proyectos (avanzado)**
- [bodex: gestion de inventario](./programacion-general/code/projects/bodex/almacen/)
- [juego de la vida de conway](./programacion-general/code/projects/juegos/juego-vida-conway/conway_game_of_life.py)
- [mapas estadisticos](./programacion-general/code/projects/mapa/falcon/)
- [react native: curso](./programacion-general/code/projects/react-native/testing/curso-midu/)
- [resultados electorales](./programacion-general/code/projects/resultados-electorales/)

---

### ciencia-de-datos

**introduccion (basico)**
- [¿que es la ciencia de datos?](./ciencia-de-datos/tutorials/intro-ciencia-datos/01-que-es-la-ciencia-de-datos.md)
- [el proceso de ciencia de datos](./ciencia-de-datos/tutorials/intro-ciencia-datos/02-el-proceso-de-ciencia-de-datos.md)
- [tipos de datos](./ciencia-de-datos/tutorials/intro-ciencia-datos/03-tipos-de-datos.md)
- [estadistica descriptiva fundamental](./ciencia-de-datos/tutorials/intro-ciencia-datos/04-estadistica-descriptiva-fundamental.md)
- [visualizacion y comunicacion](./ciencia-de-datos/tutorials/intro-ciencia-datos/05-visualizacion-y-comunicacion.md)
- [herramientas del cientifico de datos](./ciencia-de-datos/tutorials/intro-ciencia-datos/06-herramientas-del-cientifico-de-datos.md)

**manipulacion de datos (basico)**
- pandas: [estadisticas resumen](./ciencia-de-datos/code/data-manipulation/python/pandas/summary-stats.py), [tablas resumen](./ciencia-de-datos/code/data-manipulation/python/pandas/summary-tables.py), [crosstab](./ciencia-de-datos/code/data-manipulation/python/pandas/crosstab.py) y [reestructurar tablas](./ciencia-de-datos/code/data-manipulation/python/pandas/reestructurar-table.py)
- [codificacion de variables ordinales](./ciencia-de-datos/code/data-manipulation/python/tipos_datos/OrdinalEncoder.py)

**visualizacion (basico-intermedio)**
- matplotlib: [galeria de graficos](./ciencia-de-datos/code/visualization/python/matplolib/) — lineas, barras, dispersion, histogramas, pie, boxplot, heatmap, contour, 3d, espirales y solidos de revolucion
- seaborn: [facetgrid](./ciencia-de-datos/code/visualization/python/seaborn/facetgrid.py), [mapa de calor](./ciencia-de-datos/code/visualization/python/seaborn/mapa-calor.py), [pair plot](./ciencia-de-datos/code/visualization/python/seaborn/pair-plot.py), [regresion](./ciencia-de-datos/code/visualization/python/seaborn/regresion-lineal.py) y [violin](./ciencia-de-datos/code/visualization/python/seaborn/violin-plot.py)
- [graficos agrupados por categoria](./ciencia-de-datos/code/visualization/python/plots/)

**estadistica descriptiva (basico-intermedio)**
- tendencia central: [medidas](./ciencia-de-datos/code/statistics/python/stat/medidas-tendencia-central.py), [mediana](./ciencia-de-datos/code/statistics/python/stat/median.py) y [moda](./ciencia-de-datos/code/statistics/python/stat/mode.py)
- dispersion: [medidas](./ciencia-de-datos/code/statistics/python/stat/medidas-dispersion.py), [varianza](./ciencia-de-datos/code/statistics/python/stat/varianza.py) y [rango](./ciencia-de-datos/code/statistics/python/stat/range.py)
- posicion: [cuantiles](./ciencia-de-datos/code/statistics/python/stat/quatile.py), [rango intercuartil](./ciencia-de-datos/code/statistics/python/stat/intercuartil.py) e [histogramas](./ciencia-de-datos/code/statistics/python/stat/histograma.py)
- r: [tendencia central](./ciencia-de-datos/code/statistics/r/stastics/central/medidas-tendencia-central.R), [dispersion](./ciencia-de-datos/code/statistics/r/stastics/central/medidas-dispersion.R), [mediana](./ciencia-de-datos/code/statistics/r/stastics/central/median.R), [variabilidad](./ciencia-de-datos/code/statistics/r/stastics/central/variabilidad.R) y [exploracion categorica](./ciencia-de-datos/code/statistics/r/stastics/exploracion-binaria/data-categical.R)

**probabilidad (intermedio)**
- [simulacion de dados](./ciencia-de-datos/code/statistics/python/probabilidad/dice.py)
- [distribucion normal](./ciencia-de-datos/code/statistics/python/probabilidad/normal-distribution.py)
- [distribucion acumulada](./ciencia-de-datos/code/statistics/python/probabilidad/distribucion-accumaltiva.py) e [inversa normal cdf](./ciencia-de-datos/code/statistics/python/probabilidad/inversa-normal-cdf.py)
- [distribucion binomial](./ciencia-de-datos/code/statistics/python/stat/distribucion-binomial/distribucion-binomial.py) y [en r](./ciencia-de-datos/code/statistics/r/stastics/distribucion-binomial/distribucion-binomial.R)
- [bivariante normal (monte carlo)](./ciencia-de-datos/code/statistics/python/montercarlo/distribucion-bivariante-normal/bvnormal.py)

**muestreo y bootstrap (intermedio)**
- [bootstrap](./ciencia-de-datos/code/statistics/python/stat/muestreo/boostrap.py), [remuestreo](./ciencia-de-datos/code/statistics/python/stat/muestreo/remuestreo.py), [media](./ciencia-de-datos/code/statistics/python/stat/muestreo/remuestreo-media.py), [boxplot](./ciencia-de-datos/code/statistics/python/stat/muestreo/remuestreo-boxplot.py) y [permutaciones](./ciencia-de-datos/code/statistics/python/stat/muestreo/remuestreo-pemutaciones.py)
- [distribucion normal](./ciencia-de-datos/code/statistics/python/stat/muestreo/distribucion-normal.py) e [histogramas](./ciencia-de-datos/code/statistics/python/stat/muestreo/histogramas.py)
- [funcion de distribucion empirica acumulada](./ciencia-de-datos/code/sampling/python/muestreo/funcion-distribucion-empirica-acumulada.py)
- r: [bootstrap](./ciencia-de-datos/code/statistics/r/stastics/muestreo/bootstrap.R), [distribucion normal](./ciencia-de-datos/code/statistics/r/stastics/muestreo/distribucion-normal.R) y [permutaciones](./ciencia-de-datos/code/statistics/r/stastics/muestreo/permutacion/)

**correlacion y regresion (intermedio)**
- correlacion: [simple](./ciencia-de-datos/code/statistics/python/stat/correlation.py), [avanzada](./ciencia-de-datos/code/statistics/python/stat/correlacion/correlacion-avanzada.py) y [covarianza](./ciencia-de-datos/code/statistics/python/stat/covarianza.py)
- regresion: [lineal simple](./ciencia-de-datos/code/statistics/python/stat/regresion-lineal/regresion-lineal.py), [multiple](./ciencia-de-datos/code/statistics/python/stat/regresion-lineal/regresion-lineal-multiples.py), [valores ajustados y residuales](./ciencia-de-datos/code/statistics/python/stat/regresion-lineal/regresion-lineal-ajustados-residuales.py) y [rmse](./ciencia-de-datos/code/statistics/python/stat/regresion-lineal/RMSE.py)
- r: [regresion lineal](./ciencia-de-datos/code/statistics/r/stastics/regresion-lineal/), [residuos](./ciencia-de-datos/code/statistics/r/residuos.R), [apply](./ciencia-de-datos/code/statistics/r/apply.R), [lapply](./ciencia-de-datos/code/statistics/r/lapply.R), [mapply](./ciencia-de-datos/code/statistics/r/mapply.R), [fapply](./ciencia-de-datos/code/statistics/r/fapply.R), [subset](./ciencia-de-datos/code/statistics/r/subset.R) y [test](./ciencia-de-datos/code/statistics/r/test.R)

**graficos estadisticos (intermedio)**
- [histogramas](./ciencia-de-datos/code/statistics/python/stat/graficos/histograma.py), [boxplot](./ciencia-de-datos/code/statistics/python/stat/graficos/diagrama-cajas.py), [violin](./ciencia-de-datos/code/statistics/python/stat/graficos/diagrama-violin.py) y [dispersion](./ciencia-de-datos/code/statistics/python/stat/graficos/dispersion.py)
- [hexagonales](./ciencia-de-datos/code/statistics/python/stat/graficos/hexagonal.py) y [densidad hexagonal](./ciencia-de-datos/code/statistics/python/stat/graficos/hexagonal-density.py)
- [facetas](./ciencia-de-datos/code/statistics/python/stat/graficos/facetas.py), [barplot](./ciencia-de-datos/code/statistics/python/stat/graficos/barplot.py) y [tabla de frecuencias](./ciencia-de-datos/code/statistics/python/stat/graficos/tabla-frecuencias.py)
- r: [graficos](./ciencia-de-datos/code/statistics/r/stastics/graficos/) y [varias variables](./ciencia-de-datos/code/statistics/r/stastics/varias-variables/)

**algebra lineal y pca (intermedio-avanzado)**
- operaciones: [suma](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/operacion-suma.py), [producto](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/operacion-producto.py), [transpuesta e inversa](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/operacion-trans-inver.py), [combinacion lineal](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/combinacion-lineal.py) y [sistema de ecuaciones](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/sistema-ecuaciones/sistema-ecuaciones.py)
- aplicaciones: [matriz de covarianza](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/matriz-covarianza.py), [matriz de rotacion](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/matriz-rotacion.py), [valores y vectores propios](./ciencia-de-datos/code/linear-algebra/python/algebra-lineal/valores-vectore-propios.py)
- [algebra con python puro](./ciencia-de-datos/code/linear-algebra/python/math/algebra-linear/) — fracciones, matrices, vectores y operaciones reducidas
- pca: [introduccion](./ciencia-de-datos/code/pca/python/pca/pca-2.py), [script](./ciencia-de-datos/code/pca/python/pca/pca-script.py) y [rotado de imagenes](./ciencia-de-datos/code/pca/python/pca/rotando-imagenes.py)

**inferencia y modelos avanzados (avanzado)**
- [inferencia binomial](./ciencia-de-datos/code/statistics/python/inferencia/inferencia-binomial.py)
- [pruebas de hipotesis y poder estadistico](./ciencia-de-datos/code/statistics/python/stat/poder-estadistico.py)
- [analisis de supervivencia](./ciencia-de-datos/code/statistics/python/stat/analisis/analisis-supervivencia.py)
- [modelos de efectos mixtos](./ciencia-de-datos/code/statistics/python/stat/mixed-effects-model.py)
- [agrupamiento jerarquico](./ciencia-de-datos/code/statistics/python/stat/cluster-jerarquico.py)
- [series temporales (arima)](./ciencia-de-datos/code/statistics/python/stat/arima.py)
- [validacion cruzada e hiperparametros](./ciencia-de-datos/code/statistics/python/stat/hiperparamatros-validacion-cruzada.py)
- [tablas de contingencia y divergencias](./ciencia-de-datos/code/statistics/python/stat/tablas-divergencias.py)

**mineria de datos (intermedio-avanzado)**
- [¿que es la mineria de datos?](./ciencia-de-datos/tutorials/mineria-de-datos/01-que-es-la-mineria-de-datos.md), [vs tecnologias vecinas](./ciencia-de-datos/tutorials/mineria-de-datos/02-mineria-de-datos-vs-tecnologias-vecinas.md), [vs ciencia de datos](./ciencia-de-datos/tutorials/mineria-de-datos/03-ciencia-de-datos-vs-mineria.md), [las 9 tareas canonicas](./ciencia-de-datos/tutorials/mineria-de-datos/04-las-9-tareas-canonicas.md) y [recomendaciones clave](./ciencia-de-datos/tutorials/mineria-de-datos/05-recomendaciones-clave.md)
- crisp-dm: [comprension del negocio](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-1-comprension-del-negocio/), [comprension de los datos](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-2-comprension-de-los-datos/), [preparacion de datos](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-3-preparacion-de-datos/), [modelado](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-4-modelado/), [evaluacion](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-5-evaluacion/), [despliegue](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/fase-6-despliegue/) y [cierre del ciclo](./ciencia-de-datos/tutorials/mineria-de-datos/CRISP-DM/cierre-del-ciclo/)

**data-driven decision making (avanzado)**
- [¿que es ddd?](./ciencia-de-datos/tutorials/data-driven-decision-making/01-que-es-ddd.md)
- [tipos de problemas de negocio](./ciencia-de-datos/tutorials/data-driven-decision-making/02-los-dos-tipos-de-problemas-de-negocio.md)
- [decisiones automatizadas](./ciencia-de-datos/tutorials/data-driven-decision-making/03-la-revolucion-de-las-decisiones-automatizadas.md)
- [big data y productividad](./ciencia-de-datos/tutorials/data-driven-decision-making/04-impacto-del-big-data-en-la-productividad.md)

**prediccion (avanzado)**
- [prediccion de partidos por fecha de liga](./ciencia-de-datos/code/statistics/python/stat/prediction/partidos-fecha-liga.py)
- [prediccion de partidos](./ciencia-de-datos/code/statistics/python/stat/prediction/prediction-match.py)
- [mostrar datos](./ciencia-de-datos/code/statistics/python/stat/prediction/mostrar-datos.py)

---

### inteligencia-artificial

**descenso de gradiente (intermedio)**
- [descenso de gradiente](./inteligencia-artificial/code/gradient-descent/python/descenso-gradiente/gradient_descent.py)
- [algebra lineal auxiliar](./inteligencia-artificial/code/gradient-descent/python/descenso-gradiente/linear_algebra.py)
- [funcion de costo](./inteligencia-artificial/code/machine-learning/python/machine-learning/descenso-gradiente/funcion-costo.py)

**regresion (intermedio)**
- [regresion lineal simple](./inteligencia-artificial/code/ai/python/ai/regresion-lineal-simple/linear-regression-model.py)
- regresion polinomial: [grado 1](./inteligencia-artificial/code/ai/python/ai/regresion/polinomial/polyreg1.py), [grado 2](./inteligencia-artificial/code/ai/python/ai/regresion/polinomial/polyreg2.py), [grado 3](./inteligencia-artificial/code/ai/python/ai/regresion/polinomial/polyreg3.py) y [validacion cruzada](./inteligencia-artificial/code/ai/python/ai/regresion/polinomial/polyregCV.py)

**clustering (intermedio-avanzado)**
- [ejemplo de clustering](./inteligencia-artificial/code/machine-learning/python/machine-learning/clusters/example-cluster.py)

**pytorch (avanzado)**
- pipeline completo: [dataset](./inteligencia-artificial/code/ai/python/ai/pytorch/test/dataset.py), [dataloader](./inteligencia-artificial/code/ai/python/ai/pytorch/test/dataloader.py), [modelo](./inteligencia-artificial/code/ai/python/ai/pytorch/test/model.py), [optimizador](./inteligencia-artificial/code/ai/python/ai/pytorch/test/optimizador.py), [evaluacion](./inteligencia-artificial/code/ai/python/ai/pytorch/test/eval.py), [pipeline](./inteligencia-artificial/code/ai/python/ai/pytorch/test/ml_pipeline.py) y [ejecucion](./inteligencia-artificial/code/ai/python/ai/pytorch/test/run_pipeline.py)
- [dropout bayesiano](./inteligencia-artificial/code/ai/python/ai/pytorch/dropout-bayesiano/main.py)
- [regresion lineal bayesiana](./inteligencia-artificial/code/ai/python/ai/pytorch/regresion-lineal-bayesiana/main.py)

**redes neuronales (avanzado)**
- [practica 1](./inteligencia-artificial/code/neural-networks/python/ia/practica-1.py), [practica 2](./inteligencia-artificial/code/neural-networks/python/ia/practica_2.py) y [practica 3](./inteligencia-artificial/code/neural-networks/python/ia/practica-3.py)
- [tensores](./inteligencia-artificial/code/neural-networks/python/ia/Tensor.py) y [tensores avanzado](./inteligencia-artificial/code/neural-networks/python/ia/Tensor-2.py)

---

## estructura del repositorio

```
data-falcon/
├── programacion-general/
│   ├── code/
│   │   ├── courses/           # cursos (advanced python, dart, django, polars, rust)
│   │   ├── estructura-datos/  # estructuras de datos y algoritmos (go)
│   │   ├── excel/             # excel (python)
│   │   ├── file-handling/     # manejo de archivos (python)
│   │   ├── gui/               # interfaces graficas (python)
│   │   ├── projects/          # proyectos completos
│   │   └── sql/               # sql (python y postgresql)
│   ├── notas/                 # notas y documentacion
│   ├── recursos/              # libros (algoritmos, fundamentos, python, bases de datos)
│   ├── software/              # herramientas de software
│   └── tutorials/
│       ├── estructura-de-datos/
│       ├── fundamentos/
│       └── memoria/
├── ciencia-de-datos/
│   ├── code/
│   │   ├── data-manipulation/ # manipulacion de datos (pandas)
│   │   ├── linear-algebra/    # algebra lineal (numpy)
│   │   ├── pca/               # analisis de componentes principales
│   │   ├── sampling/          # tecnicas de muestreo
│   │   ├── statistics/        # estadistica (python y r)
│   │   └── visualization/     # visualizacion (matplotlib y seaborn)
│   ├── data/                  # conjuntos de datos y modelos
│   ├── notas/                 # notas y documentacion
│   ├── recursos/              # libros (algebra, ciencia de datos, estadistica)
│   ├── software/              # herramientas de software
│   └── tutorials/             # cursos y tutoriales
├── inteligencia-artificial/
│   ├── code/
│   │   ├── ai/                # pytorch y regresion
│   │   ├── gradient-descent/  # descenso de gradiente
│   │   ├── machine-learning/  # algoritmos de ml
│   │   └── neural-networks/   # redes neuronales
│   ├── notas/                 # notas y documentacion
│   ├── recursos/              # libros y materiales
│   └── tutorials/             # tutoriales
```

## conjuntos de datos

el directorio [data/](./ciencia-de-datos/data/) contiene los conjuntos de datos utilizados en los ejemplos:

- [mnist](./ciencia-de-datos/data/mnist/) y [fashion mnist](./ciencia-de-datos/data/fashionmnist/) para clasificacion de imagenes
- [modelos entrenados](./ciencia-de-datos/data/models/)
- archivos csv personalizados para los analisis (ventas, prestamos, vivienda, salud, etc.)

## recursos (libros y materiales)

- programacion-general: [algoritmos](./programacion-general/recursos/algoritmos/), [fundamentos](./programacion-general/recursos/fundamentos/), [python](./programacion-general/recursos/python/) y [bases de datos](./programacion-general/recursos/bases-datos/)
- ciencia-de-datos: [algebra lineal](./ciencia-de-datos/recursos/algebra-lineal/), [ciencia de datos](./ciencia-de-datos/recursos/ciencia-datos/) y [estadistica](./ciencia-de-datos/recursos/estadistica/)
- inteligencia-artificial: [machine learning (mlbook)](./inteligencia-artificial/recursos/MLBOOK.pdf)

## como empezar

1. clona el repositorio
2. sigue el [orden de estudio sugerido](#orden-de-estudio-sugerido), de los fundamentos a la inteligencia artificial
3. navega al directorio de cada tema y sigue los archivos de instrucciones o el readme del tutorial
4. ejecuta los scripts con las dependencias requeridas

## dependencias

- lenguajes: python 3.x, go, r, c, rust y dart
- analisis y visualizacion: pandas, numpy, matplotlib, seaborn y scikit-learn
- machine learning: pytorch
- aplicaciones: openpyxl, tkinter, pyside6 y django
- bases de datos: postgresql y sqlite

## contribuyendo

este es un repositorio de investigacion personal. para sugerencias o mejoras, crea un issue.

## licencia

este repositorio es para fines educativos e investigativos.
