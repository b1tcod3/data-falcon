# El Riesgo de Transferir "Sobre la Pared"

Llevar un prototipo de ciencia de datos a producción habitualmente exige recodificar el modelo para garantizar una mayor velocidad y compatibilidad con la infraestructura de la empresa, lo que demanda una inversión significativa.

## El problema del prototipo

El modelo que funciona en el portátil del científico de datos rara vez está listo para producción:

- Está escrito en Python/R, pero el sistema de producción puede requerir Java, C++ o un motor de reglas.
- Usa bibliotecas y dependencias que no están disponibles en el entorno de producción.
- No está optimizado para latencia baja o alto throughput.
- No maneja correctamente los casos extremos, errores de entrada ni timeouts.

## La metáfora de la pared

Los autores advierten sobre el peligro de diseñar de forma aislada y luego arrojar el modelo "sobre la pared" al equipo de desarrollo, esperando que ellos lo hagan funcionar. Esta práctica suele fracasar porque:

1. El equipo de ingeniería no entiende los supuestos del modelo.
2. El científico de datos no entiende las restricciones técnicas de producción.
3. Ambos equipos trabajan en paralelo sin comunicación hasta el último momento.

> *"Tu modelo no es lo que los científicos de datos diseñan, es lo que los ingenieros construyen."*

## La solución: colaboración temprana

Para mitigar este riesgo, se recomienda involucrar activamente desde el inicio a los desarrolladores o ingenieros de software expertos tanto en sistemas de producción como en ciencia de datos (*data science engineers*).

Su rol evoluciona durante el proyecto:

| Fase del proyecto | Rol del ingeniero |
|------------------|-------------------|
| Comprensión del Negocio | Asesor técnico: identifica restricciones de infraestructura |
| Preparación de Datos | Arquitecto: define pipelines de datos escalables |
| Modelado | Revisor: evalúa viabilidad técnica del enfoque |
| Evaluación | Validador: verifica rendimiento en condiciones de producción |
| Despliegue | Propietario: asume la custodia del producto en producción |

Los ingenieros actúan inicialmente como asesores y asumen gradualmente la propiedad del producto conforme este madura, manteniendo a los científicos de datos involucrados hasta el despliegue final.
