# Selection Sort

**Selection Sort** divide el arreglo en dos zonas: una **ordenada** (a la izquierda) y otra **desordenada** (a la derecha). En cada paso busca el elemento **mínimo** de la zona desordenada y lo mueve al final de la zona ordenada.

## Algoritmo en Go

```go
func SelectionSort[T cmp.Ordered](arr []T) {
	n := len(arr)
	for i := 0; i < n; i++ {
		minIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}
		if i != minIdx {
			arr[i], arr[minIdx] = arr[minIdx], arr[i]
		}
	}
}
```

## Compensación clave

A diferencia de Bubble Sort, Selection Sort hace **muy pocos intercambios**: a lo sumo `n - 1`. Aunque compara tantas veces como Bubble Sort, escribir en memoria es más costoso que leer, así que puede ser más rápido en la práctica. Es un algoritmo **inestable**.

## Complejidad

| Caso | Complejidad |
| --- | --- |
| Peor caso | O(n²) |
| Mejor caso | O(n²) |
| Promedio | O(n²) |
| Espacio | O(1) |

También se incluye una variante descendente (`SelectionSortDesc`) que busca el **máximo** en cada pasada, equivalente a la `selection_sort_desc` de la versión Rust.

## Código completo

- Implementación: [`sorts/selection_sort.go`](../../../programacion-general/code/estructura-datos/sorts/selection_sort.go)
- Pruebas: [`sorts/sorts_test.go`](../../../programacion-general/code/estructura-datos/sorts/sorts_test.go)

```bash
cd programacion-general/code/estructura-datos
go test ./sorts/ -run TestOrdenamientoDescendente -v
```