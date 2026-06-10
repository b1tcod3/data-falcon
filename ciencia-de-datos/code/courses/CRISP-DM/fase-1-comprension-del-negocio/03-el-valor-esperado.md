# Herramientas Conceptuales: El Valor Esperado

Para que la descomposición del problema no dependa puramente de la inspiración del momento, existe una de las herramientas más potentes del científico de datos: **estructurar el problema de negocio en términos de "Valor Esperado"** (*Expected Value*).

## ¿Qué es el Valor Esperado?

El Valor Esperado es un marco mental que permite tomar un objetivo financiero o estratégico grande y descomponerlo de forma matemática y sistemática en las tareas técnicas de datos que ya conocemos, asegurando que el esfuerzo algorítmico realmente genere un impacto económico directo.

En términos simples:
```
Valor Esperado = (Beneficio de un acierto × Probabilidad de acertar)
                - (Costo de un error × Probabilidad de errar)
```

## Aplicación práctica

### Ejemplo: Campaña de retención de clientes

Imagina que una empresa de telecomunicaciones quiere reducir el churn (cancelaciones).

1. **Objetivo financiero:** Reducir la tasa de cancelación mensual del 5% al 4%.
2. **Descomposición con Valor Esperado:**
   - Cada cliente retenido vale $120 al año en ingresos.
   - Una oferta de retención cuesta $20 por cliente.
   - Si identificamos correctamente a un cliente propenso a cancelar, ganamos $100 netos ($120 - $20).
   - Si identificamos mal a un cliente que no iba a cancelar, perdemos $20 (costo de la oferta sin beneficio).
3. **Traducción a tarea de datos:** Necesitamos un modelo de **clasificación** que prediga qué clientes van a cancelar, con alta precisión para minimizar falsos positivos (ofertar a quien no lo necesita).

## Conexión con las 9 tareas canónicas

Cada tipo de problema de negocio se traduce naturalmente a una o más tareas canónicas mediante el marco de Valor Esperado:

| Objetivo de negocio | Tarea canónica relevante | Métrica de Valor Esperado |
|--------------------|-------------------------|--------------------------|
| Reducir cancelaciones | Clasificación | ($ retenido) × (tasa de acierto) - ($ oferta) × (tasa de error) |
| Optimizar precios | Regresión | ($ precio óptimo - $ precio actual) × volumen de ventas |
| Segmentar mercado | Clustering | Aumento en ventas cruzadas × tamaño del segmento |
| Detectar fraudes | Profiling | ($ fraude evitado) × (tasa de detección) - ($ alertas falsas) × (costo de revisión) |

## Por qué es importante

Sin el marco de Valor Esperado, es fácil caer en dos trampas:

- **Sobreingeniería:** Construir modelos complejos que no generan valor económico real.
- **Suboptimización:** Elegir la métrica técnica incorrecta (ej. precisión) cuando la métrica de negocio relevante es otra (ej. costo total).

El Valor Esperado alinea el esfuerzo técnico con el impacto económico, cerrando el círculo entre la [Comprensión del Negocio](../fase-1-comprension-del-negocio/01-el-arte-de-traducir-el-problema.md) y las fases posteriores de CRISP-DM.
