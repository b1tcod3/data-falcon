# Insertion Sort

**Insertion Sort** es el método que la mayoría de la gente usa de forma intuitiva para ordenar cartas: toma cada elemento y lo **inserta en la posición correcta** dentro de la parte ya ordenada, desplazando los mayores hacia la derecha.

## Algoritmo en Go

```go
func InsertionSort[T cmp.Ordered](lista []T) {
	n := len(lista)
	for i := 1; i < n; i++ {
		j := i
		for j > 0 && lista[j] < lista[j-1] {
			lista[j], lista[j-1] = lista[j-1], lista[j]
			j--
		}
	}
}
```

## Cuándo usarlo

Insertion Sort brilla con dos tipos de entrada:

- **Listas casi ordenadas**: el mejor caso es O(n), porque casi no hay desplazamientos.
- **Conjuntos pequeños**: su bajo factor constante lo hace más rápido que algoritmos más "avanzados" para `n` pequeño.

Es **estable** y funciona bien como base de la idea "los datos que ya vienen casi ordenados se ordenan en tiempo lineal".

## Complejidad

| Caso | Complejidad |
| --- | --- |
| Peor caso (orden inverso) | O(n²) |
| Mejor caso (ya ordenado) | O(n) |
| Promedio | O(n²) |
| Espacio | O(1) |

Como con Selection Sort, se incluye la variante descendente `InsertionSortDesc`.

## Código completo

- Implementación: [`sorts/insertion_sort.go`](../../../programacion-general/code/estructura-datos/sorts/insertion_sort.go)
- Pruebas: [`sorts/sorts_test.go`](../../../programacion-general/code/estructura-datos/sorts/sorts_test.go)

```bash
cd programacion-general/code/estructura-datos
go test ./sorts/ -v
```