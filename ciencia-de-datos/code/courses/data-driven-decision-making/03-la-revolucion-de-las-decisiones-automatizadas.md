# La Revolución de las Decisiones Automatizadas

Uno de los puntos más importantes del DDD es su superposición con la automatización. Hoy en día, muchas decisiones de negocio ya no las toma un humano analizando un reporte, sino que las ejecutan sistemas informáticos en fracciones de segundo.

## ¿Qué es una decisión automatizada?

Es una decisión que un sistema computacional toma sin intervención humana directa, basándose en un modelo o algoritmo entrenado con datos históricos. El humano define las reglas y entrena el modelo, pero la decisión en tiempo real la ejecuta la máquina.

```
Datos → Modelo → Decisión → Acción
  ↑                        ↓
  └─── Feedback loop ──────┘
```

## Evolución histórica

### Años 90: Pioneros (Banca y Telecomunicaciones)

Los primeros en adoptar decisiones automatizadas basadas en datos fueron los bancos y las empresas de telecomunicaciones. Sus casos de uso principales:

- **Control de fraudes:** Detectar transacciones sospechosas en tiempo real y bloquearlas automáticamente.
- **Calificación crediticia:** Aprobar o rechazar solicitudes de crédito en segundos, sin intervención de un analista humano.

Estas industrias tenían dos ventajas clave: grandes volúmenes de datos transaccionales y un alto retorno por cada mejora en precisión.

### 2000s: Retailers (Amazon y Netflix)

Amazon y Netflix llevaron la automatización de decisiones al siguiente nivel con los **motores de recomendación**:

- **Amazon:** "Los clientes que compraron esto también compraron aquello." Decidir qué producto mostrarle a cada cliente en tiempo real.
- **Netflix:** Decidir qué películas y series recomendar a cada usuario basándose en su historial de visualización y en los patrones de usuarios similares.

Estas decisiones automatizadas transformaron industrias enteras y crearon ventajas competitivas difíciles de replicar.

### Actualidad: Publicidad Online

La publicidad online moderna es quizás el ejemplo más extremo de DDD automatizado. Cuando cargas una página web:

1. Se te identifica (por cookies, dispositivo, ubicación).
2. Se consulta tu perfil de intereses en milisegundos.
3. Un algoritmo de puja en tiempo real (RTB) decide qué anuncio mostrarte.
4. El anuncio se renderiza en la página.

Todo esto ocurre en los **milisegundos** que tarda en cargar la página. No hay humano en el proceso.

## Implicaciones del DDD automatizado

### Ventajas

- **Velocidad:** Decisiones en milisegundos, imposibles para un humano.
- **Escalabilidad:** Millones de decisiones simultáneas sin aumentar costos.
- **Consistencia:** El mismo criterio se aplica siempre (sin sesgos humanos del momento).
- **Mejora continua:** Los modelos pueden actualizarse automáticamente con nuevos datos.

### Desafíos

- **Sesgo algorítmico:** Si los datos históricos contienen sesgos, el modelo los perpetúa y amplifica.
- **Falta de explicabilidad:** Algunos modelos (deep learning) son "cajas negras" difíciles de interpretar.
- **Dependencia técnica:** Si el sistema falla, la organización puede quedar paralizada.
- **Ética y regulación:** ¿Quién es responsable cuando un algoritmo comete un error?

## El rol del científico de datos en la automatización

El científico de datos (lección [01](../intro-ciencia-datos/01-que-es-la-ciencia-de-datos.md)) no solo construye modelos, sino que debe:

- Definir qué decisiones son candidatas a automatización.
- Establecer umbrales de confianza (cuándo el modelo puede decidir solo y cuándo debe escalar a un humano).
- Monitorear la calidad del modelo en producción (los modelos se degradan con el tiempo).
- Evaluar el impacto ético y de negocio de las decisiones automatizadas.

Las herramientas para implementar estos modelos en producción se cubren en la lección sobre [herramientas](../intro-ciencia-datos/08-herramientas-del-cientifico-de-datos.md).
