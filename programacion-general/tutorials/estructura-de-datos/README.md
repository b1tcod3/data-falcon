# Estructura de Datos y Algoritmos en Go

Curso práctico de **Estructuras de Datos** implementado en **Go**, basado en el libro *A Common-Sense Guide to Data Structures and Algorithms*. Todo el código vive en [`programacion-general/code/estructura-datos/`](../../code/estructura-datos/) y cada programa incluye sus propias pruebas unitarias.

## Contenido

1. [Introducción y Notación O](./01-introduccion-y-notacion-o.md)
2. [Bubble Sort](./02-bubble-sort.md)
3. [Selection Sort](./03-selection-sort.md)
4. [Insertion Sort](./04-insertion-sort.md)
5. [Quick Sort](./05-quick-sort.md)
6. [Benchmark de Ordenamientos](./06-benchmark-de-ordenamientos.md)
7. [Colas y Pilas](./07-colas-y-pilas.md)
8. [Listas Enlazadas](./08-listas-enlazadas.md)
9. [Árboles Binarios de Búsqueda](./09-arboles-binarios-de-busqueda.md)
10. [Grafos](./10-grafos.md)

## Cómo ejecutar el código

Todos los programas están dentro de un único módulo Go (`estructura-datos`):

```bash
cd programacion-general/code/estructura-datos

# Ejecutar un programa de ejemplo
go run ./cola
go run ./grafo/dijkstra

# Ejecutar todas las pruebas del curso
go test ./...

# Benchmarks de ordenamiento
go test ./sorts/ -bench=.
```

## Orden sugerido de estudio

1. Completar las lecciones de ordenamiento (2–6) para dominar la notación O y los algoritmos básicos.
2. Seguir con las estructuras lineales: pilas, colas y listas enlazadas (7–8).
3. Terminar con estructuras jerárquicas y de red: árboles binarios y grafos (9–10).