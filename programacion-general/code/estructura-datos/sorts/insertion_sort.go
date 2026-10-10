package sorts

import "cmp"

// InsertionSort ordena un slice de forma ascendente utilizando Insertion Sort.
//
// Es eficiente para conjuntos de datos pequeños o listas casi ordenadas.
//
// Parámetros:
//   - lista: un slice de elementos comparables.
//
// Complejidad:
//   - Tiempo: O(n^2) en el peor caso, O(n) en el mejor caso.
//   - Espacio: O(1).
func InsertionSort[T cmp.Ordered](lista []T) {
	n := len(lista)

	// Empezamos desde el segundo elemento (índice 1)
	for i := 1; i < n; i++ {
		// Movemos los elementos mayores hacia la derecha para hacer
		// espacio para el elemento actual
		j := i
		for j > 0 && lista[j] < lista[j-1] {
			lista[j], lista[j-1] = lista[j-1], lista[j]
			j--
		}
	}
}

// InsertionSortDesc ordena un slice de forma descendente.
func InsertionSortDesc[T cmp.Ordered](lista []T) {
	n := len(lista)

	for i := 1; i < n; i++ {
		// Movemos los elementos menores hacia la derecha
		j := i
		for j > 0 && lista[j] > lista[j-1] {
			lista[j], lista[j-1] = lista[j-1], lista[j]
			j--
		}
	}
}
