# Diseñar el Escenario de Uso

En esta etapa inicial, el equipo debe obligarse a pensar a fondo en la ejecución real en la vida cotidiana de la empresa. Para lograrlo, se deben responder tres preguntas clave:

## Las tres preguntas fundamentales

### 1. ¿Qué queremos hacer exactamente?

No basta con decir "mejorar las ventas" o "reducir costos". Hay que ser específicos:

- ¿Qué decisión concreta cambiará gracias a este análisis?
- ¿Quién tomará esa decisión?
- ¿Con qué frecuencia se tomará?

### 2. ¿Cómo lo vamos a hacer en la práctica?

Hay que visualizar el día a día del modelo en producción:

- ¿El resultado será un reporte periódico, un dashboard, o una decisión automatizada?
- ¿Quién consumirá el resultado y en qué formato?
- ¿Cada cuánto se actualizarán los datos y las predicciones?

### 3. ¿Qué partes corresponden realmente a un modelo de minería de datos?

No todo el problema necesita un algoritmo. Hay que separar:

- **Tareas de datos:** Limpieza, integración, validación.
- **Tareas de modelo:** Clasificación, regresión, clustering, etc.
- **Tareas operativas:** Integración con sistemas existentes, capacitación de usuarios.

## Ciclos dentro de ciclos

Los autores advierten: el escenario de uso inicial casi siempre es una versión simplificada. A medida que el proyecto avance, será necesario regresar a esta fase y ajustar el diseño para que se adapte a la realidad del negocio. No es un paso atrás; es la naturaleza iterativa del proceso que refleja el [diagrama de CRISP-DM](../../../intro-ciencia-datos/02-el-proceso-de-ciencia-de-datos.md).

> **Ejemplo:** Un banco quería predecir defaults crediticios. El escenario inicial asumía que el modelo se ejecutaría una vez al mes. Al avanzar, descubrieron que necesitaban predicciones en tiempo real para integrarlas en su app móvil. Tuvieron que volver a diseñar el escenario de uso.

## Relación con otras fases

El diseño del escenario de uso alimenta directamente a la fase de [Entendimiento de los Datos](../../../intro-ciencia-datos/02-el-proceso-de-ciencia-de-datos.md#2-entendimiento-de-los-datos): para saber qué datos necesitas, primero debes tener claro qué decisión vas a tomar y cómo.
