# Benchmark de Ordenamientos

La forma más directa de **sentir la Notación O** es medir los algoritmos con entradas crecientes. El programa de benchmark mide Bubble Sort, Selection Sort, Insertion Sort y Quick Sort sobre arreglos en peor caso (orden descendente) de 100, 500, 1K, 5K y 10K elementos.

## Dónde se mide

Go ofrece dos maneras complementarias:

1. **Benchmark manual** en [`benchmark/main.go`](../../../programacion-general/code/estructura-datos/benchmark/main.go), que cronometra cada algoritmo y presenta una tabla.
2. **Benchmarks nativos** con el paquete `testing` en [`sorts/bench_test.go`](../../../programacion-general/code/estructura-datos/sorts/bench_test.go).

```bash
cd programacion-general/code/estructura-datos

# Tabla comparativa
go run ./benchmark

# Benchmarks nativos del paquete testing
go test ./sorts/ -bench=. -run=^$
```

## Ejemplo de salida

```
Algoritmo       | 100          | 500          | 1K           | 5K           | 10K
-------------------------------------------------------------------------------
Bubble Sort     | 29 µs        | 711 µs       | 3.1 ms       | 106 ms       | 310 ms
Selection Sort  | 26 µs        | 607 µs       | 2.3 ms       | 60 ms        | 239 ms
Insert Sort     | 22 µs        | 488 µs       | 2.0 ms       | 54 ms        | 236 ms
Quick Sort      | 208 µs       | 927 µs       | 3.6 ms       | 102 ms       | 349 ms
```

## Lectura de resultados

- Al pasar de 500 a 1K (el doble de datos), los algoritmos O(n²) casi **cuadruplican** su tiempo → confirma el crecimiento cuadrático.
- Al pasar de 1K a 5K (5x datos), el tiempo del peor caso sube ~25-30x, muy cerca del comportamiento esperado `(5² = 25)`.
- Quick Sort no siempre gana en arreglos pequeños: su factor constante es alto debido a las llamadas recursivas y la elección de pivote con peor caso.

Estos números son relativos a cada máquina; lo que importa es **la tasa de crecimiento**, no los valores absolutos.

## Material de referencia

En la versión Rust el benchmark vivía en `benchmark.rs` y compilaba con `rustc`; en Go, para poder reutilizarlo, los algoritmos se movieron a un paquete importable (`sorts/`) y el cronometrado quedó en `benchmark/main.go`.