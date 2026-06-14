# Stakeholders, Testbeds y Monitoreo Continuo

La evaluación tiene tres dimensiones que van más allá de las métricas técnicas: la aprobación de los actores clave del negocio, la fidelidad del entorno de prueba y el monitoreo continuo en el mundo real.

## Aprobación de los Stakeholders

Los líderes y actores clave del negocio necesitan dar el visto bueno antes del despliegue operativo. Ellos buscan garantizar que el modelo:

- Generará más beneficios que perjuicios.
- No cometerá errores catastróficos.
- Es comprensible para quienes deben tomar decisiones basadas en él.

El científico de datos debe asegurar que el comportamiento del modelo sea **completamente comprensible** para los stakeholders. Esto significa:

- Explicar las predicciones en lenguaje de negocio, no en términos matemáticos.
- Presentar casos concretos de aciertos y errores esperados.
- Mostrar el impacto económico usando el marco de [Valor Esperado](../fase-1-comprension-del-negocio/03-el-valor-esperado.md).

## Entornos de Prueba (Testbeds)

Evaluar el desempeño directamente en producción es sumamente complejo debido a la cantidad de piezas móviles y el acceso limitado. Por ello, las empresas con equipos maduros construyen **entornos espejo** que imitan fielmente los datos reales de producción para realizar evaluaciones realistas sin correr riesgos innecesarios.

Un buen testbed debe replicar:

- El volumen y la variedad de datos reales.
- La latencia y los tiempos de respuesta esperados.
- Las condiciones de error y casos extremos.
- El comportamiento de sistemas externos integrados.

## Monitoreo Continuo e "In Vivo"

En ciertos escenarios, la evaluación se extiende al sistema en vivo mediante experimentos controlados aleatorios (pruebas *in vivo*), donde se aplica el modelo a un grupo de tratamiento mientras se mantiene a otro como grupo de control.

Esto es vital porque el mundo cambia de forma constante:

- **Los estafadores adaptan su comportamiento** en respuesta directa a los modelos de detección.
- **Los formatos de los datos de entrada pueden alterarse** sustancialmente sin previo aviso al equipo técnico.
- **Los patrones de consumo evolucionan** con las temporadas, las tendencias y los eventos globales.
- **Los modelos se degradan** con el tiempo (concept drift) y requieren recalibración periódica.

Por estas razones, el monitoreo continuo no es opcional: es parte integral de la fase de Evaluación y se extiende a lo largo de toda la vida útil del modelo en producción.
