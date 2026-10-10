# Entropía y Ganancia de Información

Antes de construir cualquier modelo predictivo, necesitamos saber qué variables (atributos) contienen información útil. En ciencia de datos, no todas las variables valen lo mismo. Algunas son poderosas para separar clases; otras solo añaden ruido.

## Entropía

La **Entropía** es la medida matemática del "caos" o la impureza en un conjunto de datos.

- Si un grupo tiene 50% de casos positivos y 50% de negativos, su entropía es **máxima (1.0)**. No hay orden, solo incertidumbre.
- Si el grupo es 100% de un solo tipo (todo "Sí" o todo "No"), su entropía es **nula (0.0)**. Hay certeza absoluta.

```
Entropía máxima (0.5 / 0.5)  →  H = 1.0
Entropía media   (0.75 / 0.25) →  H ≈ 0.81
Entropía baja    (0.9 / 0.1)  →  H ≈ 0.47
Entropía nula    (1.0 / 0.0)  →  H = 0.0
```

## Ganancia de Información (Information Gain)

La **Ganancia de Información** es la métrica que nos dice cuánto disminuye la entropía general cuando dividimos los datos usando un atributo específico.

El proceso es:

1. Calcular la entropía del conjunto antes de dividir.
2. Dividir los datos según cada posible valor del atributo.
3. Calcular la entropía ponderada de los subgrupos resultantes.
4. La Ganancia de Información es la diferencia entre la entropía original y la entropía ponderada después de la división.

```
Ganancia = Entropía(original) - Entropía(división)
```

**A mayor ganancia, mejor atributo para empezar a segmentar.**

## Selección de Atributos

El primer paso en cualquier proyecto de Machine Learning es aislar las variables con mayor ganancia de información. Si el problema es **categórico** (clasificación), se utiliza la **Ganancia de Información** basada en entropía. Si el problema es **numérico** (regresión), se utiliza la **Reducción de Varianza** en lugar de la entropía:

- Clasificación → Ganancia de Información (entropía)
- Regresión → Reducción de Varianza (varianza)

## Conexión con el proceso CRISP-DM

La selección de atributos ocurre durante la [Preparación de los Datos](../fase-3-preparacion-de-datos/01-las-tareas-de-cocina-de-datos.md) y la fase de **Modelado**. Las variables con baja ganancia de información pueden descartarse para simplificar el modelo y reducir el sobreajuste. Una vez identificados los mejores atributos, el siguiente paso es construir un modelo que los combine: los [árboles de decisión](./03-arboles-de-decision-y-reglas.md).
