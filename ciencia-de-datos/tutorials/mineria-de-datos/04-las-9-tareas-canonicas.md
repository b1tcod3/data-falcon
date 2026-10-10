# Las 9 Tareas Canónicas de la Minería de Datos

Como vimos en la lección anterior ([Ciencia de Datos vs. Minería de Datos](./03-ciencia-de-datos-vs-mineria.md)), la Minería de Datos es la ejecución práctica de los principios de la Ciencia de Datos. Pero, ¿qué tareas concretas puede realizar? Existen **9 tareas canónicas** que abarcan prácticamente cualquier problema de minería de datos que enfrentes.

| # | Tarea | ¿Qué intenta hacer? | Ejemplo de Negocio |
|---|-------|---------------------|--------------------|
| 1 | **Clasificación** | Predecir a qué clase discreta (de un grupo pequeño y mutuamente excluyente) pertenece un individuo | ¿Este cliente va a responder a la oferta? (Sí o No) |
| 2 | **Regresión** | Estimar o predecir un valor numérico continuo para cada individuo | ¿Cuánto dinero va a gastar este cliente en servicios el próximo mes? |
| 3 | **Emparejamiento por Similitud** | Encontrar individuos que se parezcan a uno que ya conocemos basándose en sus datos | Identificar empresas que se parezcan a nuestros mejores clientes para mandar al equipo de ventas |
| 4 | **Clustering (Agrupamiento)** | Agrupar a la población por similitudes, pero sin un objetivo o etiqueta previa | Ver si nuestra base de datos de clientes se divide de forma natural en segmentos de mercado |
| 5 | **Agrupación por Co-ocurrencia** | Encontrar asociaciones entre artículos basándose en transacciones de compra | Descubrir que la gente que compra carne molida suele comprar salsa picante a la vez (Análisis de la canasta de compras) |
| 6 | **Profiling (Perfilado)** | Caracterizar el comportamiento típico de un individuo o grupo para crear una "norma" | Monitorear el uso de tarjetas de crédito para detectar fraudes cuando un cargo se sale del perfil normal |
| 7 | **Predicción de Enlaces** | Predecir conexiones que deberían existir entre nodos de una red y qué tan fuertes serán | El algoritmo de LinkedIn o Facebook que te sugiere: "Como tú y Carlos tienen 10 amigos en común, tal vez quieras ser su amigo" |
| 8 | **Reducción de Datos** | Reemplazar un set de datos gigantesco por uno más pequeño que conserve la información más importante | Condensar un historial masivo de películas vistas por un usuario en un perfil simple de sus "géneros favoritos" |
| 9 | **Modelado Causal** | Entender si una acción específica realmente influye y causa un resultado, o si es una coincidencia | Evaluar mediante pruebas A/B si un cliente compró porque vio nuestro anuncio o si iba a comprar de todos modos |

## Categorías generales

Estas 9 tareas se agrupan en tres grandes categorías según su propósito:

### Aprendizaje Supervisado (con etiquetas)

Son tareas donde los datos de entrenamiento incluyen la respuesta correcta. El modelo aprende a partir de ejemplos etiquetados.

- **Clasificación** (tarea 1): La salida es una categoría discreta.
- **Regresión** (tarea 2): La salida es un valor numérico continuo.
- **Modelado Causal** (tarea 9): Se busca determinar causalidad, no solo correlación.

### Aprendizaje No Supervisado (sin etiquetas)

No hay una variable objetivo predefinida. El algoritmo encuentra patrones por sí mismo.

- **Clustering** (tarea 4): Agrupa datos similares sin conocer los grupos de antemano.
- **Agrupación por Co-ocurrencia** (tarea 5): Encuentra asociaciones entre ítems.
- **Reducción de Datos** (tarea 8): Simplifica los datos preservando su estructura esencial.

### Tareas basadas en similitud y relaciones

Se enfocan en medir qué tan parecidos son los elementos entre sí.

- **Emparejamiento por Similitud** (tarea 3): Encontrar elementos similares a uno de referencia.
- **Profiling** (tarea 6): Caracterizar el comportamiento "normal" para detectar anomalías.
- **Predicción de Enlaces** (tarea 7): Predecir conexiones en redes.

## Relación con el proceso CRISP-DM

Estas 9 tareas corresponden principalmente a la fase de **Modelado** dentro del proceso CRISP-DM que veremos en el [módulo de CRISP-DM](./CRISP-DM/fase-4-modelado/01-el-corazon-algoritmico.md). La elección de qué tarea usar depende del tipo de problema de negocio que se definió en las primeras fases del proceso.
