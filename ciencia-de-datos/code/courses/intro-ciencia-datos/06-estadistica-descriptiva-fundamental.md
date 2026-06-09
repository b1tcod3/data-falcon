# Estadística Descriptiva Fundamental

La estadística descriptiva es el primer paso en cualquier análisis de datos. Su objetivo es resumir, organizar y describir las características principales de un conjunto de datos sin hacer inferencias más allá de los datos mismos.

## Población vs. Muestra

- **Población:** Conjunto completo de elementos que se desea estudiar.
- **Muestra:** Subconjunto representativo de la población.

Utilizamos muestras porque estudiar poblaciones completas suele ser inviable por costo, tiempo o acceso. La clave está en que la muestra sea **representativa** para poder generalizar los resultados.

## Medidas de tendencia central

Indican el valor "típico" o "central" alrededor del cual se agrupan los datos.

| Medida | Definición | Cuándo usarla |
|--------|------------|---------------|
| **Media** | Suma de todos los valores dividida entre el número de valores | Datos simétricos sin valores atípicos |
| **Mediana** | Valor central cuando los datos están ordenados | Datos con valores atípicos o distribución asimétrica |
| **Moda** | Valor que aparece con mayor frecuencia | Datos categóricos o distribuciones multimodales |

> **Ejemplo:** En un barrio, los ingresos son [30k, 32k, 31k, 35k, 200k]. La media es 65.6k (engañosa por el valor atípico), pero la mediana es 32k (representa mejor el ingreso típico).

## Medidas de dispersión

Indican cuán dispersos están los datos alrededor del centro.

| Medida | Definición |
|--------|------------|
| **Rango** | Valor máximo menos valor mínimo. Simple pero sensible a atípicos. |
| **Varianza** | Promedio de las diferencias al cuadrado respecto a la media. |
| **Desviación estándar** | Raíz cuadrada de la varianza. En las mismas unidades que los datos. |
| **Rango intercuartil (IQR)** | Diferencia entre el percentil 75 y el percentil 25. Robusto ante atípicos. |

### Interpretación de la desviación estándar

Una desviación estándar pequeña indica que los datos están concentrados cerca de la media. Una grande indica que están muy dispersos.

## Percentiles y cuartiles

Los percentiles dividen los datos en 100 partes iguales. Los cuartiles son percentiles específicos:

- **Q1 (percentil 25):** El 25% de los datos está por debajo de este valor.
- **Q2 (percentil 50):** La mediana.
- **Q3 (percentil 75):** El 75% de los datos está por debajo de este valor.

## Correlación

La correlación mide la relación entre dos variables. Se expresa con el coeficiente de correlación de Pearson (r), que va de -1 a 1.

| Valor | Significado |
|-------|-------------|
| r = 1 | Correlación positiva perfecta (al subir una, sube la otra) |
| r = -1 | Correlación negativa perfecta (al subir una, baja la otra) |
| r = 0 | Sin correlación lineal |

> **Importante:** Correlación no implica causalidad. Dos variables pueden estar correlacionadas sin que una cause la otra.

## La campana de Gauss (distribución normal)

Muchos fenómenos naturales siguen una distribución normal (campana de Gauss). En una distribución normal:

- La media, mediana y moda coinciden en el centro.
- El 68% de los datos está a 1 desviación estándar de la media.
- El 95% está a 2 desviaciones estándar.
- El 99.7% está a 3 desviaciones estándar.

## Resumen visual con el boxplot

El boxplot (diagrama de caja y bigotes) resume cinco estadísticos de un vistazo:

```
     outliers →  o
                |
   bigote sup. → |
                |
      Q3 → ┌────┤
           │    │  ← IQR
      Q1 → └────┤
                |
   bigote inf. → |
                |
     outliers →  o
```
