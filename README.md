# repositorio de investigacion en programacion-general, ciencia-de-datos e inteligencia-artificial

este repositorio contiene una coleccion de codigo, tutoriales, cursos y proyectos relacionados con programacion general, ciencia de datos, inteligencia artificial, estadisticas y metodologias relacionadas. sirve como recurso de investigacion y aprendizaje, organizado por area y lenguaje de programacion.

## areas del repositorio

- **programacion-general**: manejo de archivos, interfaces graficas, sql, excel, cursos, proyectos
- **ciencia-de-datos**: estadisticas, probabilidad, prediccion, manipulacion de datos, visualizacion, algebra-lineal, aprendizaje automatico
- **inteligencia-artificial**: clasificacion binaria, regresion polinomial, redes neuronales

## estructura del repositorio

```
data-falcon/
├── ciencia-de-datos/
│   ├── code/                # codigo fuente organizado por metodologia
│   │   ├── statistics/      # analisis estadistico (python y r)
│   │   ├── visualization/   # visualizacion de datos
│   │   ├── data-manipulation/ # procesamiento de datos (pandas)
│   │   ├── linear-algebra/  # operaciones de algebra lineal
│   │   ├── pca/            # analisis de componentes principales
│   │   └── sampling/       # tecnicas de muestreo
│   ├── data/                # conjuntos de datos y modelos
│   │   ├── models/         # modelos entrenados
│   │   ├── assets/         # imagenes y otros recursos
│   │   ├── fashionmnist/    # conjunto fashion mnist
│   │   └── mnist/          # conjunto mnist
│   ├── notas/               # notas y documentacion
│   ├── recursos/            # libros y materiales de lectura
│   │   ├── algebra-lineal/
│   │   ├── ciencia-datos/
│   │   └── estadistica/
│   ├── software/             # herramientas de software
│   └── tutorials/           # tutoriales
│
├── inteligencia-artificial/
│   ├── code/                # codigo fuente
│   │   ├── ai/             # inteligencia artificial
│   │   ├── machine-learning/ # algoritmos de ml
│   │   ├── neural-networks/ # implementaciones de redes neuronales
│   │   └── gradient-descent/ # algoritmos de optimizacion
│   ├── notas/               # notas y documentacion
│   ├── recursos/            # libros y materiales
│   └── tutorials/           # tutoriales
│
└── programacion-general/
    ├── code/                # codigo fuente
    │   ├── courses/         # materiales de cursos
    │   ├── excel/           # manejo de archivos excel
    │   ├── file-handling/   # operaciones de archivos
    │   ├── gui/             # interfaces graficas
    │   ├── projects/        # proyectos completos
    │   └── sql/             # operaciones de base de datos
    ├── notas/               # notas y documentacion
    ├── recursos/            # libros y materiales
    │   ├── bases-datos/
    │   └── python/
    ├── software/             # herramientas de software
    └── tutorials/           # tutoriales
        ├── c/
        └── python/
```

## contenido de programacion

### programacion-general

**manejo de archivos (python)**
- lectura y escritura de archivos csv, txt
- manejo de errores

**interfaces graficas (python)**
- pyside6
- tkinter

**sql (python)**
- operaciones de base de datos
- conexiones y consultas

**excel (python)**
- automatizacion con openpyxl

**cursos**
- advanced python
- conceptos-basico
- dart
- django
- polars
- rust

**proyectos**
- bodex (sistema de gestion de inventario)
- mapa (proyectos de mapeo geografico)
- juegos (juegos y simulaciones)
- react-native (proyectos de apps moviles)
- resultados-electorales

---

### ciencia-de-datos

**estadisticas (python y r)**

*medidas de tendencia central y dispersion*
- media, mediana, moda
- varianza y desviacion estandar
- rango e rango intercuartil
- cuantiles

*distribuciones*
- distribucion normal
- distribucion binomial
- distribucion acumulada
- transformacion inversa normal cdf

*analisis de correlacion*
- correlacion simple y avanzada
- covarianza
- diagramas de correlacion

*regresion*
- regresion lineal simple y multiple
- valores ajustados y residuales
- calculo de rmse

*muestreo y bootstrap*
- distribuciones normales
- histogramas
- remuestreo (bootstrap)
- permutaciones
- remuestreo con media, boxplot

*graficos estadisticos*
- histogramas
- diagramas de cajas (boxplot)
- diagramas de violin
- diagramas de dispersion
- graficos hexagonales
- facetas
- barplots
- tablas de frecuencias

*analisis avanzado*
- pruebas de hipotesis
- poder estadistico
- analisis de supervivencia
- modelos de efectos mixtos
- agrupamiento jerarquico
- series temporales (arima)
- validacion cruzada e hiperparametros
- tablas de contingencia y divergencias

*inferencia estadistica*
- inferencia binomial

**probabilidad**
- simulacion de dados
- distribuciones bivariante normal
- distribuciones acumuladas

**prediccion**
- prediccion de partidos por fecha de liga
- modelos predictivos

**manipulacion de datos (python)**
- operaciones con pandas
- lectura y escritura de archivos
- manejo de errores
- limpieza y transformacion de datos

**visualizacion de datos (python)**
- matplotlib (barras, dispersion, histogramas)
- seaborn
- graficos 3d

**algebra lineal (python)**
- operaciones matriciales
- vectores propios
- matrices de covarianza

**aprendizaje automatico (python)**
- clasificacion y regresion
- ingenieria de caracteristicas
- evaluacion de modelos

---

### inteligencia-artificial

- clasificacion binaria con pytorch
- regresion polinomial
- redes neuronales
- descenso de gradiente

## conjuntos de datos

el directorio `data/` contiene varios conjuntos de datos utilizados en los ejemplos:
- fashion mnist y mnist para clasificacion de imagenes
- archivos csv personalizados para diversos analisis

## como empezar

1. clona el repositorio
2. navega a los directorios de metodologias especificas
3. sigue los archivos en subdirectorios para instrucciones de configuracion
4. ejecuta scripts de python con las dependencias requeridas

## dependencias

dependencias comunes incluyen:
- python 3.x
- pytorch
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- r con paquetes estadisticos

## contribuyendo

este es un repositorio de investigacion personal. para sugerencias o mejoras, crea un issue.

## licencia

este repositorio es para fines educativos e investigativos.
