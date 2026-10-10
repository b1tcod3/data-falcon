package sorts

import "cmp"

// QuickSort ordena un slice de forma ascendente utilizando Quick Sort.
//
// Es in-place y muy eficiente en la mayoría de casos. Usa el último
// elemento como pivote.
//
// Parámetros:
//   - arr: un slice de elementos comparables.
//
// Complejidad:
//   - Tiempo: O(n log n) promedio, O(n^2) peor caso (slice ya ordenado).
//   - Espacio: O(log n) por la profundidad de recursión.
func QuickSort[T cmp.Ordered](arr []T) {
	if len(arr) == 0 {
		return
	}
	quicksort(arr, 0, len(arr)-1)
}

func quicksort[T cmp.Ordered](arr []T, left, right int) {
	if left >= right {
		return
	}

	pivotPos := partition(arr, left, right)

	if pivotPos > 0 {
		quicksort(arr, left, pivotPos-1)
	}
	quicksort(arr, pivotPos+1, right)
}

func partition[T cmp.Ordered](arr []T, left, right int) int {
	pivot := right
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
