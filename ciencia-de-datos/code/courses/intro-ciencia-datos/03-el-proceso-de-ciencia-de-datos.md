# El Proceso de Ciencia de Datos

La Ciencia de Datos sigue un proceso estructurado que garantiza que los resultados sean válidos, reproducibles y accionables. El marco de trabajo más utilizado es **CRISP-DM** (Cross-Industry Standard Process for Data Mining), que consta de seis fases iterativas.

## Las seis fases de CRISP-DM

```
                  +------------------+
                  | Entendimiento    |
                  | del Negocio      |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Entendimiento    |
                  | de los Datos     |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Preparación      |
                  | de los Datos     |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Modelado         |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Evaluación       |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Despliegue       |
                  +------------------+
```

Las flechas entre fases van en ambos sentidos: el proceso es **iterativo** y se puede retroceder a fases anteriores cuando se descubre nueva información.

### 1. Entendimiento del Negocio

Es la fase más importante y la que más se suele saltar. Sin un objetivo claro, todo el trabajo posterior carece de dirección.

- Definir los objetivos del negocio.
- Traducirlos a objetivos técnicos de análisis.
- Definir criterios de éxito (¿cómo sabemos que el proyecto funcionó?).
- Identificar los recursos disponibles y las restricciones.

> **Ejemplo:** "Reducir en un 15% la tasa de cancelación de clientes en los próximos 6 meses."

### 2. Entendimiento de los Datos

Antes de modelar, hay que conocer los datos disponibles.

- Recolectar datos iniciales de las fuentes identificadas.
- Describir los datos (forma, tipo, volumen).
- Explorar los datos para detectar patrones iniciales (EDA).
- Verificar la calidad de los datos: valores faltantes, outliers, inconsistencias.

### 3. Preparación de los Datos

Ocupa entre el 60% y el 80% del tiempo de un proyecto de datos. Es el trabajo de limpiar, transformar y estructurar los datos para que sean aptos para el modelado.

- Limpieza: manejar valores nulos, corregir errores, eliminar duplicados.
- Transformación: normalización, codificación de variables categóricas, ingeniería de características.
- Integración: combinar datos de múltiples fuentes.
- Muestreo: seleccionar subconjuntos representativos cuando los datos son muy grandes.

### 4. Modelado

Se aplican algoritmos para encontrar patrones o hacer predicciones.

- Seleccionar la técnica de modelado adecuada (regresión, clasificación, clustering, etc.).
- Dividir los datos en entrenamiento, validación y prueba.
- Entrenar el modelo y ajustar hiperparámetros.
- Documentar los supuestos y limitaciones del modelo elegido.

### 5. Evaluación

No basta con que el modelo funcione bien en datos históricos; debe cumplir los objetivos del negocio.

- Evaluar el modelo con las métricas definidas en la fase 1.
- Revisar si los resultados tienen sentido en el contexto del negocio.
- Decidir si se despliega, se ajusta o se descarta.
- Identificar posibles problemas (sobreajuste, sesgos, falta de datos).

### 6. Despliegue

El modelo pasa a producción y comienza a generar valor real.

- Integrar el modelo en sistemas existentes.
- Crear dashboards, reportes o APIs según el caso de uso.
- Monitorear el rendimiento del modelo en el tiempo (los modelos se degradan).
- Documentar el proceso completo para garantizar reproducibilidad.

## Principios clave del proceso

- **Iteración:** Rara vez se avanza en línea recta. Cada fase puede revelar información que obligue a volver a fases anteriores.
- **Colaboración:** El proceso involucra a stakeholders de negocio, ingenieros de datos, científicos de datos y equipos de operaciones.
- **Reproducibilidad:** Cada paso debe ser documentado y reproducible para que otros (o tu yo del futuro) puedan entender y replicar el trabajo.
