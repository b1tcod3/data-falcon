# La Trampa de las Falsas Alarmas

El propósito central de la fase de Evaluación es evaluar rigurosamente los resultados obtenidos para ganar la certeza de que los patrones encontrados reflejan regularidades reales del negocio y no simples anomalías o excentricidades de la muestra estadística analizada.

Aunque técnicamente es posible realizar un despliegue inmediato tras el modelado, es una práctica desaconsejable. Siempre resulta más rápido, económico, seguro y sencillo realizar pruebas previas dentro de un entorno controlado de laboratorio.

## La trampa

La evaluación no solo mide la precisión matemática en el laboratorio, sino también la viabilidad económica y el cumplimiento de las metas de negocio originales. Un modelo puede exhibir una precisión impecable en el laboratorio —superior al 99%— pero fracasar rotundamente en el negocio por un factor aparentemente menor: las falsas alarmas.

### Ejemplo: Detección de fraude

Imagina un modelo de detección de fraudes con 99.5% de precisión en un banco que procesa 10 millones de transacciones al día:

- 0.5% de error → 50,000 transacciones marcadas como fraude incorrectamente cada día.
- Cada una requiere que un analista humano revise el caso.
- Si cada revisión toma 5 minutos, se necesitan más de 4,000 horas-hombre al día.
- El costo operativo de proveer personal para procesar dichas alertas puede volver el modelo económicamente inviable.
- Además, el impacto negativo en la satisfacción del cliente (tarjetas bloqueadas injustamente) genera costos difíciles de cuantificar.

### Lo mismo aplica para

- **Detección de spam:** Correos legítimos marcados como spam destruyen la confianza del usuario.
- **Detección de intrusiones:** Alertas de seguridad falsas saturan al equipo de SOC y ocultan ataques reales.
- **Aprobación de crédito:** Rechazar clientes solventes por error es perder ingresos.

## La métrica correcta

La precisión no siempre es la métrica adecuada. Dependiendo del costo de cada tipo de error, pueden ser más relevantes:

| Métrica | Mide | Ideal para |
|---------|------|------------|
| **Precisión (precision)** | De las predicciones positivas, ¿cuántas son correctas? | Minimizar falsas alarmas |
| **Recall (sensibilidad)** | De los casos positivos reales, ¿cuántos detectamos? | Minimizar falsos negativos |
| **F1-Score** | Balance entre precisión y recall | Escenarios con clases desbalanceadas |
| **Costo total** | Impacto económico combinado de todos los errores | Alineación con objetivos de negocio (ver [Valor Esperado](../fase-1-comprension-del-negocio/03-el-valor-esperado.md)) |
