# Introducción y Notación O

Las **estructuras de datos** son formas de organizar y almacenar la información para que los algoritmos operen sobre ella de manera eficiente. La elección de la estructura correcta determina la rapidez de las operaciones más frecuentes de un programa.

## ¿Qué es la Notación O?

La **Notación O** (*Big O*) describe cuánto tiempo o memoria necesita un algoritmo conforme crece el tamaño de su entrada (`n`). No mide segundos, sino **cómo crece** la cantidad de pasos.

| Notación | Nombre | Ejemplo típico |
| --- | --- | --- |
| O(1) | Constante | Leer un elemento de un slice |
| O(log n) | Logarítmico | Búsqueda binaria |
| O(n) | Lineal | Recorrer todos los elementos |
| O(n log n) | Lineal-logarítmico | Quick Sort, Merge Sort |
| O(n²) | Cuadrático | Bubble Sort, Selection Sort |
| O(2ⁿ) | Exponencial | Recursión de Fibonacci naive |

## Reglas rápidas

1. **Ignorar constantes y coeficientes**: `O(2n)` es `O(n)`.
2. **Dominan los términos de mayor grado**: `O(n² + n)` es `O(n²)`.
3. **Los peores casos importan**: se describe la tasa de crecimiento en el peor escenario.

En Rust los ejemplos del curso usaban slices (`Vec`); en Go la contraparte natural son los **slices** (`[]T`), que también son eficientes para acceso por índice (O(1)).

## Primeros algoritmos del curso

Los cuatro algoritmos de ordenamiento que veremos —Bubble Sort, Selection Sort, Insertion Sort y Quick Sort— operan **in-place** (modifican el slice original sin copias extra), exactamente como en la versión Rust.

El código Go está en [`programacion-general/code/estructura-datos/sorts/`](../../code/estructura-datos/sorts/). Las funciones son **genéricas** (`sorts.BubbleSort[int]`, `sorts.BubbleSort[string]`, ...), lo que equivale a los subtipos genéricos `<T: PartialOrd>` que se usaban en Rust.

## Resumen

Entender la Notación O sirve para elegir entre estructuras de datos: un arreglo, una lista enlazada, un árbol o un grafo cada uno brinda complejidades distintas según la operación. El resto de las lecciones de este curso exploran cada una con ejemplos ejecutables en Go.