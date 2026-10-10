# El Enemigo Silencioso: Data Leakage

Una de las advertencias más importantes en la práctica de ciencia de datos trata sobre un error técnico que puede destruir un proyecto: las **filtraciones** o *data leakage*.

## ¿Qué es una filtración?

Una filtración ocurre cuando una variable incluida en los datos históricos contiene información directa sobre la variable objetivo (*target*), pero dicha información **no estará disponible en el momento exacto en que se deba tomar la decisión en el mundo real**.

Como la preparación de datos se hace "después de los hechos" mirando el pasado, es sumamente fácil cometer este error sin darse cuenta. El modelo parece funcionar de maravilla en los datos históricos, pero fracasa estrepitosamente en producción.

## Ejemplo 1: El visitante web

Imagina que intentas predecir en tiempo real si un usuario va a cerrar su sesión o continuará navegando en un sitio web.

Si incluyes la variable *"número total de páginas visitadas en la sesión"* como predictor, obtendrás un modelo con un éxito aparente rotundo. Los usuarios que visitaron muchas páginas claramente no cerraron la sesión temprano.

**El problema:** En la vida real, es imposible conocer el total de páginas visitadas hasta que la sesión ya terminó. En el momento de hacer la predicción (cuando el usuario acaba de llegar), ese dato simplemente no existe. El modelo es inservible.

## Ejemplo 2: El gran comprador

Ahora imagina que buscas predecir si un cliente nuevo será un "gran comprador" (gastará más de $1000 en su primer año).

Si incluyes variables como las *"categorías de artículos comprados"* o el *"monto de impuestos pagados"*, tu modelo parecerá increíblemente preciso.

**El problema:** Esos datos solo existen después de que la compra ya se efectuó. En el momento de la toma de decisiones (cuando el cliente se registra por primera vez), no tienes esa información. El modelo no puede usarse para predecir nada.

## Cómo detectar y evitar filtraciones

| Señal de alerta | Posible solución |
|----------------|-----------------|
| El modelo tiene una precisión sospechosamente alta (>95%) | Revisar cada variable para ver si contiene información del futuro |
| Variables que son consecuencia del target, no causa | Excluir toda variable que ocurra después del evento a predecir |
| Datos de prueba mezclados con entrenamiento | Asegurar separación temporal estricta entre train y test |
| Normalización hecha antes de dividir datos | Escalar después de separar train/test para evitar contaminación |

## Pregunta clave para cada variable

> **¿Este dato existiría en el momento real de la predicción?**

Si la respuesta es "no" o "tal vez", esa variable es candidata a causar una filtración y debe excluirse.

Una vez que los datos han sido limpiados, transformados y blindados contra filtraciones del futuro, el proceso CRISP-DM nos traslada al laboratorio donde se construyen los algoritmos predictivos: la fase de **Modelado**.
