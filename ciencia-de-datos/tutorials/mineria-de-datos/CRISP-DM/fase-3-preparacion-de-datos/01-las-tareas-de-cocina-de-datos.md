# Las Tareas Típicas de "Cocina" de Datos

Esta fase se ejecuta prácticamente de la mano con la *Comprensión de los Datos*. Las herramientas de ciencia de datos son sumamente poderosas, pero imponen requisitos estrictos sobre la estructura de la información, exigiendo formatos que rara vez se presentan de forma natural en los sistemas de una empresa.

Durante la preparación, la materia prima se manipula y transforma mediante técnicas estándar para garantizar mejores resultados analíticos.

## Formateo e integración

Los datos dispersos en múltiples fuentes deben transformarse a un formato tabular limpio. Esto implica:

- Unificar esquemas de diferentes bases de datos.
- Estandarizar formatos de fecha, moneda y unidades.
- Resolver conflictos entre campos con el mismo nombre pero diferente significado.
- Crear una sola tabla o conjunto de tablas listas para el análisis.

## Gestión de ausencias

Los valores faltantes (*missing values*) son inevitables en datos reales. Hay dos enfoques principales:

| Enfoque | Descripción | Cuándo usarlo |
|---------|-------------|---------------|
| **Eliminación** | Borrar filas o columnas con valores ausentes | Cuando la cantidad de valores faltantes es pequeña o aleatoria |
| **Imputación** | Inferir el valor faltante a partir de otros datos (media, mediana, regresión, KNN) | Cuando la pérdida de datos sería muy costosa o los faltantes siguen un patrón |

## Conversión de tipos

Los algoritmos tienen requisitos específicos sobre los tipos de datos que aceptan. Es necesario adaptar las variables según la tecnología elegida:

- **Variables categóricas** → codificación one-hot, ordinal o target encoding para algoritmos que solo procesan números.
- **Variables numéricas** → discretización (convertir en rangos) para algoritmos simbólicos o basados en reglas.
- **Texto** → vectorización (TF-IDF, embeddings) para algoritmos de machine learning.

## Escalado y normalización

Las variables numéricas suelen estar en escalas muy diferentes (edad en años vs. ingreso en miles de dólares). Si no se escalan, las variables con magnitudes mayores dominarán injustamente muchos algoritmos.

| Técnica | Qué hace |
|---------|----------|
| **Normalización (min-max)** | Escala los valores a un rango fijo, generalmente [0, 1] |
| **Estandarización (z-score)** | Centra en 0 con desviación estándar 1 |
| **Escalado robusto** | Usa mediana y rango intercuartil, resistente a outliers |

## El factor de la creatividad humana: Feature Engineering

Definir y construir las variables que alimentarán al modelo —lo que hoy conocemos como *Feature Engineering*— es uno de los puntos donde más influyen la creatividad, el sentido común y el conocimiento de negocio del analista.

Una buena variable ingenierizada puede:

- Revelar patrones que los datos crudos ocultan (ej. "días desde la última compra" en lugar de la fecha absoluta).
- Incorporar conocimiento del dominio (ej. "ratio de gasto en comida vs. ingreso" para segmentación).
- Reducir la complejidad del modelo (una variable bien diseñada puede reemplazar varias mal diseñadas).

> El éxito de toda la solución suele sostenerse sobre la genialidad con la que se diseñen estas variables.

## Conexión con la Fase 2

La preparación de datos se alimenta directamente del diagnóstico de la [Fase 2](../fase-2-comprension-de-los-datos/01-los-retos-de-la-materia-prima.md): si identificaste problemas de integración, inconsistencia o costos, aquí es donde los resuelves.
