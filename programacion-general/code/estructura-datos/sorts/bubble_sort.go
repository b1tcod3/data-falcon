// Package sorts contiene la implementación de los algoritmos de
// ordenamiento estudiados en el curso de estructuras de datos.
//
// Este paquete es importable (a diferencia de los programas de ejemplo en
// cada carpeta) para permitir que el benchmark lo reutilice.
package sorts

import "cmp"

// BubbleSort ordena un slice de forma ascendente utilizando Bubble Sort.
//
// Es estable y tiene una optimización de "salida temprana": si en una
// pasada no se realizó ningún intercambio, el slice ya está ordenado.
//
// Parámetros:
//   - lista: un slice de elementos que implementan cmp.Ordered.
//
// Complejidad:
//   - Tiempo: O(n^2) en el peor caso, O(n) en el mejor caso.
//   - Espacio: O(1).
func BubbleSort[T cmp.Ordered](lista []T) {
	n := len(lista)

	// bucle externo: en cada pasada el elemento más grande se mueve al final
	for i := 0; i < n; i++ {
		intercambiado := false
		// bucle interno: el último elemento de la pasada anterior ya está ordenado
		for j := 0; j < n-i-1; j++ {
			if lista[j] > lista[j+1] {
				lista[j], lista[j+1] = lista[j+1], lista[j]
				intercambiado = true
			}
		}
		// si no se realizó ningún intercambio, la lista ya está ordenada
		if !intercambiado {
			break
		}
	}
}
