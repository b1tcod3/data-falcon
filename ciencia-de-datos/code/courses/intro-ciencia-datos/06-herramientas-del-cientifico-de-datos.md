# Herramientas del Científico de Datos

Un científico de datos cuenta con un ecosistema de herramientas que cubren todo el ciclo de vida del dato: desde la adquisición hasta el despliegue de modelos. Conocer las herramientas adecuadas para cada tarea es tan importante como dominar los conceptos.

## Lenguajes de programación

### Python

Es el lenguaje dominante en Ciencia de Datos. Su popularidad se debe a:

- Sintaxis clara y fácil de aprender.
- Ecosistema maduro de bibliotecas especializadas.
- Comunidad enorme y activa.

**Bibliotecas esenciales:**

| Biblioteca | Propósito |
|-----------|-----------|
| **pandas** | Manipulación y análisis de datos estructurados |
| **NumPy** | Computación numérica y álgebra lineal |
| **scikit-learn** | Machine learning (modelos, preprocesamiento, evaluación) |
| **Matplotlib / Seaborn** | Visualización de datos |
| **SciPy** | Estadística avanzada, optimización, señales |
| **Jupyter Notebook** | Entorno interactivo para análisis y documentación |

### R

Es el lenguaje estándar en estadística académica e investigación. Su fortaleza está en:

- Análisis estadístico y modelado de datos.
- Visualización de alta calidad (ggplot2).
- Pruebas estadísticas y metodologías formales.

Muchos científicos de datos optan por aprender ambos lenguajes, usando Python para producción y pipeline de datos, y R para análisis exploratorio profundo.

### SQL

No es opcional. SQL es el lenguaje para consultar bases de datos relacionales, y la mayoría de los datos empresariales vive en bases de datos relacionales. Un científico de datos debe saber escribir consultas SELECT, JOIN, agregaciones y subconsultas sin depender de herramientas visuales.

## Entornos de trabajo

### Jupyter Notebook / JupyterLab

Es el entorno más utilizado para análisis exploratorio. Combina código ejecutable, visualizaciones y texto explicativo en un solo documento. Ideal para:

- Exploración y limpieza de datos.
- Prototipado rápido de modelos.
- Documentación de análisis.
- Presentaciones técnicas.

### VS Code / PyCharm

Editores de código para desarrollo más estructurado. Se usan cuando el análisis se convierte en código de producción (scripts, módulos, aplicaciones).

## Control de versiones

Git es indispensable para:

- Rastrear cambios en el código.
- Colaborar con otros miembros del equipo.
- Mantener versiones reproducibles de análisis.
- Integrar con plataformas como GitHub, GitLab o Bitbucket.

## Plataformas y servicios

### Google Colab

Entorno de Jupyter Notebook en la nube que ofrece GPUs gratuitas. Ideal para aprender y prototipar sin configurar nada localmente.

### Kaggle

Plataforma de competiciones de Ciencia de Datos que también ofrece:

- Datasets públicos para practicar.
- Notebooks en la nube.
- Foros de discusión.
- Kernels para aprender de la comunidad.

## Flujo de trabajo integrado

```
                    +-------------------+
                    |    SQL            |  ← Extraer datos
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    |    pandas         |  ← Limpiar y transformar
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    |    Jupyter        |  ← Explorar y visualizar
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    |    scikit-learn   |  ← Modelar
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    |    Git            |  ← Versionar
                    +-------------------+
```

## ¿Qué aprender primero?

Si estás empezando, esta es una ruta recomendada:

1. **Python básico:** variables, funciones, estructuras de datos.
2. **pandas:** leer, limpiar y manipular datos tabulares.
3. **Matplotlib / Seaborn:** visualizar datos para entenderlos.
4. **Jupyter Notebook:** integrar todo en un flujo interactivo.
5. **SQL:** consultar bases de datos.
6. **scikit-learn:** primeros modelos de machine learning.
7. **Git:** versionar y compartir tu trabajo.
