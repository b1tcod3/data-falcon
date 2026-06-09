# Tipos de Datos

No todos los datos son iguales. Entender la naturaleza de los datos con los que trabajas es fundamental para elegir las técnicas de análisis y visualización adecuadas.

## Según su estructura

### Datos estructurados

Son datos organizados en un formato predefinido, típicamente filas y columnas. Cada columna representa una variable y cada fila una observación.

- **Ejemplos:** Bases de datos relacionales, hojas de cálculo, archivos CSV.
- **Ventaja:** Fáciles de almacenar, consultar y analizar.
- **Herramientas:** SQL, pandas, Excel.

```
| Cliente | Edad | Ingreso | Compras |
|---------|------|---------|---------|
| A       | 28   | 45000   | 12      |
| B       | 35   | 62000   | 8       |
| C       | 42   | 38000   | 15      |
```

### Datos semiestructurados

Tienen cierta organización pero no siguen un esquema rígido de tablas. Incluyen etiquetas o marcadores que separan los elementos.

- **Ejemplos:** JSON, XML, HTML, archivos de log.
- **Ventaja:** Flexibles, pueden contener información jerárquica.
- **Herramientas:** parsers de JSON/XML, bases de datos NoSQL.

```json
{
  "cliente": "A",
  "edad": 28,
  "direccion": {
    "ciudad": "Madrid",
    "cp": "28001"
  }
}
```

### Datos no estructurados

No tienen una estructura predefinida. Son el tipo de datos más abundante (se estima que representa el 80% de los datos generados).

- **Ejemplos:** Texto libre, imágenes, audio, video, publicaciones en redes sociales.
- **Ventaja:** Ricos en información, capturan matices que los datos estructurados pierden.
- **Desafío:** Difíciles de procesar automáticamente; requieren técnicas avanzadas como procesamiento de lenguaje natural (NLP) o visión por computadora.

## Según su naturaleza estadística

### Datos cuantitativos (numéricos)

Representan cantidades medibles. Se dividen en:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Discretos** | Valores enteros, contables | Número de hijos, cantidad de productos vendidos |
| **Continuos** | Valores en un rango continuo | Altura, peso, temperatura, ingreso |

### Datos cualitativos (categóricos)

Representan categorías o grupos. Se dividen en:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Nominales** | Categorías sin orden jerárquico | Color de ojos, país, tipo de cliente |
| **Ordinales** | Categorías con orden pero sin distancia fija | Nivel educativo, calificación (bajo, medio, alto) |

## Escalas de medición

La teoría de Stevens clasifica las variables en cuatro escalas que determinan qué operaciones matemáticas tienen sentido:

| Escala | Característica | Operaciones posibles | Ejemplo |
|--------|---------------|---------------------|---------|
| **Nominal** | Solo nombres/categorías | Igualdad / desigualdad | Género, color |
| **Ordinal** | Orden, pero sin distancia uniforme | Mayor / menor | Ranking, nivel socioeconómico |
| **Intervalo** | Distancia uniforme, sin cero absoluto | Suma, resta | Temperatura °C, año |
| **Razón** | Distancia uniforme, con cero absoluto | Todas (incluye multiplicación) | Altura, ingreso, tiempo |

## Fuentes comunes de datos

- **Bases de datos transaccionales:** Registros de ventas, transacciones bancarias.
- **Sensores e IoT:** Lecturas de temperatura, GPS, dispositivos wearable.
- **Web scraping:** Datos extraídos de sitios web.
- **APIs:** Datos obtenidos de servicios como Twitter, Google Maps, servicios climáticos.
- **Logs:** Archivos de servidores, aplicaciones, dispositivos.
- **Encuestas y formularios:** Datos recolectados directamente de personas.
