# Probabilidades y Sobreajuste

Una clasificación binaria rígida ("Sí" o "No") es insuficiente para la toma de decisiones financieras o de marketing, donde se requiere priorizar riesgos mediante un ranking. Los árboles de decisión ofrecen una solución natural para esto, pero esconden un peligro: el sobreajuste.

## Estimación de Probabilidades

Los árboles se convierten en estimadores de probabilidad analizando la proporción de la etiqueta dentro de cada hoja.

**Ejemplo:** Si en una hoja caen 8 clientes que cancelaron y 2 que se quedaron, la probabilidad de cancelación es del 80%.

Esta probabilidad estimada permite **ordenar** a los individuos por riesgo, algo mucho más valioso que una simple etiqueta de "Sí/No". Con este ranking, un banco puede ofrecer retención solo a los clientes con más de 70% de probabilidad de cancelación, optimizando su presupuesto de retención usando el marco de [Valor Esperado](../fase-1-comprension-del-negocio/03-el-valor-esperado.md).

## El Problema de las Muestras Pequeñas

Si un segmento es tan específico que solo contiene un registro, la matemática tradicional le asignaría un 100% o 0% de probabilidad. Asumir certeza absoluta por un solo caso es un error analítico grave conocido como **Sobreajuste (*Overfitting*)**.

El sobreajuste ocurre cuando el modelo "memoriza" el ruido y los casos particulares de los datos de entrenamiento en lugar de aprender los patrones generales. Un árbol sobreajustado tendrá:

- Muchas hojas con muy pocos registros.
- Precisión perfecta en entrenamiento, pero pobre en datos nuevos.
- Reglas extremadamente específicas y poco generalizables.

## La Corrección de Laplace

Para evitar estimaciones extremas basadas en poca evidencia, la ciencia de datos aplica un "suavizado" matemático conocido como **Corrección de Laplace** (o *Laplace smoothing*):

$$p(c) = \frac{n + 1}{n + m + 2}$$

Donde:
- $n$ = número de casos positivos en la hoja
- $m$ = número de casos negativos en la hoja

**Efecto de la corrección:**

| n | m | Sin corrección | Con Laplace |
|---|---|---|---|
| 1 | 0 | 100% | 67% |
| 2 | 0 | 100% | 75% |
| 10 | 0 | 100% | 92% |
| 80 | 20 | 80% | 79.4% |
| 800 | 200 | 80% | 79.9% |

La fórmula modera las probabilidades hacia un 50% neutral cuando hay muy pocos datos, pero su efecto desaparece a medida que el tamaño de la muestra ($n+m$) crece, convergiendo con la probabilidad real.

## Advertencias Críticas para la Práctica

### 1. La Importancia del Contexto en las Variables

El ranking global de atributos (cuál variable es mejor para toda la base de datos) no dictará exactamente el orden del árbol. Como el árbol evalúa subgrupos de forma recursiva, una variable que era inútil a nivel global puede volverse el predictor más importante dentro de una rama específica.

**Ejemplo:** La variable "tiene mascota" puede ser irrelevante para toda la población, pero dentro del subgrupo "clientes sin hijos", puede ser el mejor predictor de gasto en seguros.

### 2. La Ilusión de la Precisión

Un modelo que alcanza un 73% de precisión en los datos con los que fue entrenado no garantiza ese rendimiento en la vida real. Validar si el modelo generaliza bien o si solo "memorizó" el pasado será el foco de la siguiente fase: [Evaluación](../fase-5-evaluacion/01-la-trampa-de-las-falsas-alarmas.md).

## Conexión con las siguientes fases

El sobreajuste se detecta durante la [Evaluación](../fase-5-evaluacion/01-la-trampa-de-las-falsas-alarmas.md) al comparar el rendimiento del modelo en datos de entrenamiento vs. datos de prueba. Una gran diferencia entre ambos es la señal de alerta más clara de que el modelo no generaliza.
