# Los Dos Tipos de Problemas de Negocio

Las decisiones que se benefician de la ciencia de datos y el DDD se dividen en dos grandes categorías. Cada una tiene objetivos, enfoques y métricas de éxito diferentes.

## Tipo 1: Descubrimientos

**Objetivo principal:** Encontrar información oculta y útil explorando los datos, sin probar una hipótesis predefinida.

En este tipo de problema, no sabemos exactamente qué estamos buscando. Exploramos los datos con la esperanza de descubrir patrones, segmentaciones o correlaciones que puedan generar nuevas oportunidades de negocio.

### Ejemplo: Target

Target analizó los históricos de compra de sus clientas para identificar patrones que indicaran un embarazo antes del nacimiento del bebé. Al detectar estos patrones, podían enviar ofertas de pañales y productos relacionados antes que la competencia, ganando la lealtad de la nueva madre desde el principio.

> **Clave del éxito:** Target no sabía de antemano qué productos predecían un embarazo. El análisis exploratorio reveló combinaciones inesperadas (como lociones sin fragancia y ciertos suplementos) que, en conjunto, eran un fuerte predictor.

### Características del Tipo 1

- No hay una hipótesis previa clara.
- El valor está en encontrar lo inesperado.
- Difícil de medir el ROI por anticipado.
- Requiere curiosidad y pensamiento exploratorio.
- Se apoya en visualización de datos (lección [06](../intro-ciencia-datos/06-visualizacion-y-comunicacion.md)) y estadística descriptiva (lección [05](../intro-ciencia-datos/05-estadistica-descriptiva-fundamental.md)).

## Tipo 2: Escala Masiva

**Objetivo principal:** Mejorar ligeramente la precisión de una decisión que se repite millones de veces.

En lugar de buscar grandes descubrimientos, se trata de optimizar decisiones pequeñas pero extremadamente frecuentes. Un aumento mínimo en la precisión matemática se traduce en millones de dólares cuando se multiplica por millones de decisiones.

### Ejemplo: MegaTelCo (Churn)

Una empresa de telecomunicaciones necesita identificar qué clientes específicos, de entre millones, son propensos a cancelar su contrato. Una vez identificados, pueden ofrecerles incentivos de retención personalizados.

> **Clave del éxito:** No necesitan predecir el churn con un 100% de precisión. Si pasan del 85% al 87% de precisión, ese 2% adicional representa millones de dólares en clientes retenidos.

### Características del Tipo 2

- Decisiones que se repiten cientos de miles o millones de veces.
- Pequeñas mejoras en precisión generan gran impacto acumulado.
- La decisión suele estar automatizada (sin intervención humana).
- Requiere modelos predictivos robustos (machine learning).
- Las métricas de rendimiento del modelo son críticas.

### El poder del Tipo 2

En operaciones masivas como las siguientes, incluso una mejora mínima tiene un impacto financiero enorme:

| Aplicación | Impacto de una mejora del 1% |
|------------|------------------------------|
| **Detección de fraudes** | Millones de dólares en transacciones fraudulentas evitadas |
| **Calificación crediticia** | Reducción de defaults sin perder clientes solventes |
| **Publicidad online** | Aumento en tasas de clic y conversión |
| **Recomendaciones** | Mayor engagement y ventas cruzadas |

## Comparación

| Aspecto | Tipo 1: Descubrimientos | Tipo 2: Escala Masiva |
|---------|------------------------|----------------------|
| Enfoque | Exploratorio | Predictivo |
| Pregunta | "¿Qué patrones existen?" | "¿Qué decisión tomar ahora?" |
| Frecuencia | Una vez o pocas veces | Millones de veces |
| ROI | Puede ser transformador o nulo | Pequeño pero seguro y escalable |
| Método | Análisis exploratorio, visualización | Modelos de machine learning |
| Riesgo | Alto (puede no encontrar nada) | Bajo (mejora incremental garantizada) |

Ambos tipos son válidos y complementarios. Una organización madura en DDD utiliza ambos enfoques según el problema que enfrenta.
