# Visualización y Comunicación de Datos

Un análisis excelente vale poco si no se comunica de forma efectiva. La visualización de datos es la herramienta principal del científico de datos para transmitir hallazgos a audiencias tanto técnicas como no técnicas.

## Principios básicos de visualización

### 1. Conoce tu audiencia

- **Audiencia técnica:** Puede interpretar gráficos complejos, distribuciones, boxplots, matrices de correlación.
- **Audiencia ejecutiva:** Necesita mensajes claros, pocos números, enfoque en insights y recomendaciones.
- **Audiencia general:** Gráficos simples, anotaciones explicativas, sin jerga técnica.

### 2. Elige el gráfico correcto

| Tipo de dato | Gráfico recomendado |
|-------------|-------------------|
| Una variable numérica | Histograma, boxplot |
| Una variable categórica | Barras, pastel (solo si hay pocas categorías) |
| Dos variables numéricas | Dispersión (scatter plot) |
| Relación temporal | Líneas (line chart) |
| Comparar grupos | Barras agrupadas, boxplots lado a lado |
| Composición | Barras apiladas, área apilada |
| Correlación | Mapa de calor (heatmap) |
| Distribución de datos | Violín (violin plot), histograma |

### 3. Menos es más

- Elimina la tinta no esencial (líneas de cuadrícula innecesarias, bordes, sombras 3D).
- Usa colores con propósito, no decorativos.
- Etiqueta ejes de forma clara y legible.
- Evita gráficos circulares con más de 5 categorías.

## Storytelling con datos

La comunicación efectiva de datos sigue una estructura narrativa:

1. **Contexto:** ¿Cuál es la situación? ¿Qué está en juego?
2. **Conflicto:** ¿Qué problema o patrón descubrimos? ¿Qué es inesperado?
3. **Resolución:** ¿Qué significa esto? ¿Qué recomienda hacer?

### El enfoque "Big Idea"

Define tu mensaje principal en una sola oración. Todo en tu presentación debe apoyar esa idea. Si un gráfico no contribuye a ella, no lo incluyas.

## Trampas comunes en visualización

- **Escalas manipuladas:** Un eje Y que no empieza en cero puede exagerar diferencias.
- **Gráficos 3D:** Distorsionan la percepción y son difíciles de leer.
- **Demasiada información:** Intentar mostrar todo en un solo gráfico.
- **Colores confusos:** Usar rojo/verde sin considerar daltonismo; usar demasiados colores.
- **Correlación como causalidad:** Un gráfico no demuestra que una variable cause a otra.

## Herramientas de visualización

| Herramienta | Ideal para |
|-------------|-----------|
| **Matplotlib** | Gráficos estáticos, publicación científica, control total |
| **Seaborn** | Gráficos estadísticos atractivos con poco código |
| **Plotly** | Gráficos interactivos, dashboards web |
| **Tableau / Power BI** | Dashboards empresariales, audiencias no técnicas |
| **ggplot2 (R)** | Gramática de gráficos, análisis exploratorio en R |

## Checklist para una buena visualización

- ¿El gráfico responde a una pregunta específica?
- ¿La audiencia puede interpretarlo sin explicación adicional?
- ¿Los ejes están etiquetados y las escalas son claras?
- ¿Los colores son accesibles (considerando daltonismo)?
- ¿Se evitó distorsionar los datos con escalas engañosas?
- ¿El título comunica el hallazgo principal, no solo la descripción?
