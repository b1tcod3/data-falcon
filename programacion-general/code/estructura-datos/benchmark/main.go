// Programa de benchmark de los algoritmos de ordenamiento.
//
// Mide el tiempo de Bubble Sort, Selection Sort e Insertion Sort sobre
// arreglos en orden descendente (peor caso) de distintos tamaños.
//
// Ejecutar con:
//
//	go run ./benchmark
package main

import (
	"fmt"
	"time"

	"estructura-datos/sorts"
)

// generarPeorCaso genera un slice de tamaño n en orden descendente.
func generarPeorCaso(n int) []int {
	datos := make([]int, n)
	for i := 0; i < n; i++ {
		datos[i] = n - i
	}
	return datos
}

// formatearDuracion devuelve una duración legible (s, ms o µs).
func formatearDuracion(d time.Duration) string {
	switch {
	case d >= time.Second:
		return fmt.Sprintf("%.4f s", d.Seconds())
	case d >= time.Millisecond:
		return fmt.Sprintf("%.4f ms", float64(d.Microseconds())/1000)
	default:
		return fmt.Sprintf("%.4f µs", float64(d.Nanoseconds())/1000)
	}
}

// benchmark ejecuta una función de ordenamiento sobre el peor caso de tamaño n
// y devuelve cuánto tardó.
func benchmark(n int, ordenar func([]int)) time.Duration {
	lista := generarPeorCaso(n)
	inicio := time.Now()
	ordenar(lista)
	return time.Since(inicio)
}

func main() {
	tamanos := []int{100, 500, 1_000, 5_000, 10_000}

	fmt.Printf("\n%s\n", "================== Benchmark de Algoritmos de Ordenamiento ==================")
	fmt.Printf("%-15s | %-12s | %-12s | %-12s | %-12s | %-12s\n",
		"Algoritmo", "100", "500", "1K", "5K", "10K")
	fmt.Println("-------------------------------------------------------------------------------")

	imprimirFila("Bubble Sort", tamanos, sorts.BubbleSort[int])
	imprimirFila("Selection Sort", tamanos, sorts.SelectionSort[int])
	imprimirFila("Insert Sort", tamanos, sorts.InsertionSort[int])
	imprimirFila("Quick Sort", tamanos, sorts.QuickSort[int])
}

func imprimirFila(nombre string, tamanos []int, ordenar func([]int)) {
	fmt.Printf("%-15s |", nombre)
	for _, n := range tamanos {
		fmt.Printf(" %-12s |", formatearDuracion(benchmark(n, ordenar)))
	}
	fmt.Println()
}
