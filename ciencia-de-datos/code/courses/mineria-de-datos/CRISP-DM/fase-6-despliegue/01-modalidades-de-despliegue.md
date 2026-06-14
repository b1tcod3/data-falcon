# Modalidades de Despliegue

En la fase de despliegue, los resultados obtenidos —o los sistemas de minería de datos en sí mismos— se integran en la operación real de la empresa para materializar el retorno de la inversión (ROI).

El despliegue puede tomar múltiples formas dependiendo de la complejidad técnica y las necesidades operativas de la organización.

## Despliegue de Modelos

Se implementa un modelo predictivo estático directamente dentro de un sistema de información o proceso de negocio existente.

**Ejemplos:**
- Integrar un modelo de *churn* para enviar ofertas automáticas a clientes en riesgo.
- Incorporar un modelo de fraude que genera "casos" en un sistema de gestión para analistas humanos.
- Un modelo de aprobación de crédito que puntúa solicitudes en tiempo real.

En esta modalidad, el modelo se entrena, se evalúa, se despliega y se mantiene relativamente estable hasta que una nueva versión lo reemplaza.

## Despliegue de Técnicas

Se automatiza el proceso completo de minería en producción para que el sistema construya y pruebe modelos de manera autónoma. Se utiliza cuando el mundo cambia demasiado rápido para el equipo humano o cuando hay demasiadas tareas de modelado para gestionarlas manualmente.

**Ejemplo:** Sistemas automatizados de publicidad en línea que optimizan y generan nuevos modelos en producción ante cada nueva campaña publicitaria. Cada campaña tiene su propio conjunto de audiencias y creatividades; no tendría sentido que un científico de datos entrene manualmente cientos de modelos al día.

Esta modalidad requiere una infraestructura técnica más sofisticada y equipos de ingeniería de datos robustos.

## Despliegue No Técnico o Sutil

A veces el resultado del análisis no es un sistema automatizado, sino conocimiento accionable que se implementa mediante cambios procedimentales simples.

**Ejemplo del texto:** Imprimir una lista de reglas de diagnóstico descubiertas por el algoritmo y pegarla con cinta adhesiva a un costado de las impresoras industriales para resolver fallas rápidamente.

Esta forma de despliegue, aunque modesta, puede generar un enorme valor sin requerir inversión en infraestructura tecnológica.

## Tabla comparativa

| Tipo | Automatización | Complejidad técnica | Mantenimiento |
|------|---------------|-------------------|--------------|
| **Modelos** | Media: el modelo se actualiza periódicamente | Media | Bajo: actualizaciones manuales |
| **Técnicas** | Alta: el sistema se re-entrena solo | Alta | Alto: requiere monitoreo continuo |
| **No técnico** | Nula | Baja | Muy bajo: cambios procedimentales |
