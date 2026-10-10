package sorts

import (
	"strconv"
	"testing"
)

// generarPeorCaso genera un slice de tamaño n en orden descendente,
// que es el peor caso para la mayoría de los algoritmos de ordenamiento.
func generarPeorCaso(n int) []int {
	datos := make([]int, n)
	for i := 0; i < n; i++ {
		datos[i] = n - i
	}
	return datos
}

func BenchmarkBubbleSort(b *testing.B) {
	for _, n := range []int{100, 500, 1000, 5000, 10000} {
		b.Run("n="+strconv.Itoa(n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				datos := generarPeorCaso(n)
				BubbleSort(datos)
			}
		})
	}
}

func BenchmarkSelectionSort(b *testing.B) {
	for _, n := range []int{100, 500, 1000, 5000, 10000} {
		b.Run("n="+strconv.Itoa(n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				datos := generarPeorCaso(n)
				SelectionSort(datos)
			}
		})
	}
}

func BenchmarkInsertionSort(b *testing.B) {
	for _, n := range []int{100, 500, 1000, 5000, 10000} {
		b.Run("n="+strconv.Itoa(n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				datos := generarPeorCaso(n)
				InsertionSort(datos)
			}
		})
	}
}

func BenchmarkQuickSort(b *testing.B) {
	for _, n := range []int{100, 500, 1000, 5000, 10000} {
		b.Run("n="+strconv.Itoa(n), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				datos := generarPeorCaso(n)
				QuickSort(datos)
			}
		})
	}
}
