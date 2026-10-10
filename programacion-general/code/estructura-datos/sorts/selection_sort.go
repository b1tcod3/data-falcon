package sorts

import "cmp"

// SelectionSort ordena un slice de forma ascendente utilizando Selection Sort.
//
// Es inestable (puede cambiar el orden relativo de elementos iguales) pero
// eficiente en memoria ya que opera in-place, haciendo un máximo de n-1 swaps.
//
// Parámetros:
//   - arr: un slice de elementos comparables.
//
// Complejidad:
//   - Tiempo: O(n^2) en todos los casos.
//   - Espacio: O(1).
func SelectionSort[T cmp.Ordered](arr []T) {
	n := len(arr)

	for i := 0; i < n; i++ {
		// Encontrar el índice del elemento mínimo de la sublista no ordenada
		minIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}

		// Intercambiar el elemento mínimo con el primer elemento no ordenado
		if i != minIdx {
			arr[i], arr[minIdx] = arr[minIdx], arr[i]
		}
	}
}

// SelectionSortDesc ordena un slice de forma descendente utilizando
// Selection Sort. Busca el máximo en cada iteración.
func SelectionSortDesc[T cmp.Ordered](arr []T) {
	n := len(arr)

	for i := 0; i < n; i++ {
		maxIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] > arr[maxIdx] {
				maxIdx = j
			}
		}

		if i != maxIdx {
			arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
		}
	}
}
