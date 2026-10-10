# Quick Sort

**Quick Sort** sigue la estrategia de *divide y vencerás*: elige un **pivote**, reordena el arreglo para que los menores queden a la izquierda y los mayores a la derecha (`partition`), y repite recursivamente sobre cada mitad.

## Algoritmo en Go

```go
func QuickSort[T cmp.Ordered](arr []T) {
	if len(arr) == 0 {
		return
	}
	quicksort(arr, 0, len(arr)-1)
}

func partition[T cmp.Ordered](arr []T, left, right int) int {
	pivot := right // usamos el último elemento como pivote
	i := left
	for j := left; j < right; j++ {
		if arr[j] < arr[pivot] {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[pivot] = arr[pivot], arr[i]
	return i
}
```

## Por qué es rápido

En el caso promedio cada partición divide el arreglo más o menos por la mitad, generando `log n` niveles de recursión y `n` comparaciones por nivel → **O(n log n)**. La partición es **in-place**, así que no gasta memoria extra significativa.

## Complejidad

| Caso | Complejidad |
| --- | --- |
| Promedio | O(n log n) |
| Peor caso (arreglo ya ordenado, pivote subóptimo) | O(n²) |
| Espacio | O(log n) por recursión |

El peor caso ocurre cuando el pivote termina siempre en un extremo. Técnicas como elegir el pivote al azar o el mediano de tres reducen esa probabilidad.

## Código completo

- Implementación: [`sorts/quick_sort.go`](../../code/estructura-datos/sorts/quick_sort.go)
- Pruebas: [`sorts/sorts_test.go`](../../code/estructura-datos/sorts/sorts_test.go)

```bash
cd programacion-general/code/estructura-datos
go test ./sorts/ -run TestOrdenarListaDesordenada/QuickSort -v
```