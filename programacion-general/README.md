# Repositorio de Investigación en Programación General, Ciencia de Datos e IA

Este repositorio contiene una colección de código, tutoriales, cursos y proyectos relacionados con programación general, ciencia de datos, inteligencia artificial, estadísticas y metodologías relacionadas. Sirve como recurso de investigación y aprendizaje, organizado por área y lenguaje de programación.

## Áreas del Repositorio

- **Programación General**: Manejo de archivos, Interfaces gráficas, SQL, Excel
- **Ciencia de Datos**: Estadísticas, Probabilidad, Predicción, Manipulación de datos, Visualización, Álgebra lineal, Aprendizaje automático
- **Inteligencia Artificial**: Clasificación binaria, Regresión polinomial, Redes neuronales

## Estructura del Repositorio

```
data-falcon/
├── README.md                 # Este archivo
├── .gitignore               # Reglas de ignorar para Git
├── data/                    # Conjuntos de datos y modelos
│   ├── models/              # Modelos entrenados (.pth)
│   ├── assets/              # Imágenes y otros recursos
│   ├── nutri.csv            # Conjunto de datos de nutrición
│   ├── FashionMNIST/        # Conjunto Fashion MNIST
│   └── MNIST/               # Conjunto MNIST
├── code/                    # Código fuente organizado por metodología
│   ├── ai/                  # Inteligencia Artificial
│   │   ├── python/
│   │   └── r/
│   ├── statistics/          # Análisis estadístico
│   │   ├── python/
│   │   └── r/
│   ├── linear-algebra/      # Operaciones de álgebra lineal
│   │   └── python/
│   ├── visualization/       # Visualización de datos
│   │   └── python/
│   ├── data-manipulation/   # Procesamiento de datos (Pandas, etc.)
│   │   └── python/
│   ├── machine-learning/    # Algoritmos de ML
│   │   └── python/
│   ├── file-handling/       # Operaciones de archivos
│   │   └── python/
│   ├── gui/                 # Interfaces gráficas
│   │   └── python/
│   ├── pca/                 # Análisis de Componentes Principales
│   │   └── python/
│   ├── sampling/            # Técnicas de muestreo
│   │   └── python/
│   ├── gradient-descent/    # Algoritmos de optimización
│   │   └── python/
│   ├── excel/               # Manejo de archivos Excel
│   │   └── python/
│   ├── sql/                 # Operaciones de base de datos
│   │   └── python/
│   └── neural-networks/     # Implementaciones de redes neuronales
│       └── python/
├── tutorials/               # Tutoriales para principiantes
│   └── python/
├── courses/                 # Materiales de cursos
│   ├── conceptos-basico/    # Conceptos básicos
│   └── ...
├── projects/                # Proyectos completos
│   ├── bodex/               # Sistema de gestión de inventario
│   ├── mapa/                # Proyectos de mapeo geográfico
│   ├── juegos/              # Juegos y simulaciones
│   └── react-native/        # Proyectos de apps móviles
└── software/                # Herramientas de software
```

## Contenido de Programación

### Programación General

**Manejo de Archivos (Python)**
- Lectura y escritura de archivos CSV, TXT
- Manejo de errores

**Interfaces Gráficas (Python)**
- PySide6

**SQL (Python)**
- Operaciones de base de datos

**Excel (Python)**
- Automatización con openpyxl

---

### Ciencia de Datos

**Estadísticas (Python y R)**

*Medidas de Tendencia Central y Dispersión*
- Media, mediana, moda
- Varianza y desviación estándar
- Rango e rango intercuartil
- Cuantiles

*Distribuciones*
- Distribución normal
- Distribución binomial
- Distribución acumulada
- Transformación inversa normal CDF

*Análisis de Correlación*
- Correlación simple y avanzada
- Covarianza
- Diagramas de correlación

*Regresión*
- Regresión lineal simple y múltiple
- Valores ajustados y residuales
- Cálculo de RMSE

*Muestreo y Bootstrap*
- Distribuciones normales
- Histogramas
- Remuestreo (bootstrap)
- Permutaciones
- Remuestreo con media, boxplot

*Gráficos Estadísticos*
- Histogramas
- Diagramas de cajas (boxplot)
- Diagramas de violín
- Diagramas de dispersión
- Gráficos hexagonales
- Facetas
- Barplots
- Tablas de frecuencias

*Análisis Avanzado*
- Pruebas de hipótesis
- Poder estadístico
- Análisis de supervivencia
- Modelos de efectos mixtos
- Agrupamiento jerárquico
- Series temporales (ARIMA)
- Validación cruzada e hiperparámetros
- Tablas de contingencia y divergencias

*Inferencia Estadística*
- Inferencia binomial

**Probabilidad**
- Simulación de dados
- Distribuciones bivariante normal
- Distribuciones acumuladas

**Predicción**
- Predicción de partidos por fecha de liga
- Modelos predictivos

**Manipulación de Datos (Python)**
- Operaciones con Pandas
- Lectura y escritura de archivos
- Manejo de errores
- Limpieza y transformación de datos

**Visualización de Datos (Python)**
- Matplotlib (barras, dispersión, histogramas)
- Seaborn
- Gráficos 3D

**Álgebra Lineal (Python)**
- Operaciones matriciales

**Aprendizaje Automático (Python)**
- Clasificación y regresión
- Ingeniería de características
- Evaluación de modelos

---

### Inteligencia Artificial

- Clasificación binaria con PyTorch
- Regresión polinomial
- Redes neuronales

## Conjuntos de Datos

El directorio `data/` contiene varios conjuntos de datos utilizados en los ejemplos:
- Conjunto de datos de diabetes de los indios Pima
- Fashion MNIST y MNIST para clasificación de imágenes
- Archivos CSV personalizados para diversos análisis

## Cómo Empezar

1. Clona el repositorio
2. Navega a los directorios de metodologías específicas
3. Sigue los archivos README en subdirectorios para instrucciones de configuración
4. Ejecuta scripts de Python con las dependencias requeridas (ver READMEs individuales)

## Dependencias

Dependencias comunes incluyen:
- Python 3.x
- PyTorch
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- R con paquetes estadísticos

## Contribuyendo

Este es un repositorio de investigación personal. Para sugerencias o mejoras, crea un issue.

## Licencia

Este repositorio es para fines educativos e investigativos.