package sorts

import (
	"slices"
	"testing"
)

// ordenadores asocia un nombre con la función de ordenamiento a probar.
var ordenadores = map[string]func([]int){
	"BubbleSort":    BubbleSort[int],
	"SelectionSort": SelectionSort[int],
	"InsertionSort": InsertionSort[int],
	"QuickSort":     QuickSort[int],
}

func TestOrdenarListaDesordenada(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{64, 34, 25, 12, 22, 11, 90}
			ordenar(got)
			want := []int{11, 12, 22, 25, 34, 64, 90}
			if !slices.Equal(got, want) {
				t.Errorf("%s: obtenido %v, esperado %v", nombre, got, want)
			}
		})
	}
}

func TestListaYaOrdenada(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{1, 2, 3, 4, 5}
			ordenar(got)
			want := []int{1, 2, 3, 4, 5}
			if !slices.Equal(got, want) {
				t.Errorf("%s: obtenido %v, esperado %v", nombre, got, want)
			}
		})
	}
}

func TestListaVacia(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{}
			ordenar(got)
			if len(got) != 0 {
				t.Errorf("%s: se esperaba slice vacío, obtenido %v", nombre, got)
			}
		})
	}
}

func TestElementosRepetidos(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{3, 1, 4, 1, 5, 9, 2, 6, 5}
			ordenar(got)
			want := []int{1, 1, 2, 3, 4, 5, 5, 6, 9}
			if !slices.Equal(got, want) {
				t.Errorf("%s: obtenido %v, esperado %v", nombre, got, want)
			}
		})
	}
}

func TestUnElemento(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{42}
			ordenar(got)
			if !slices.Equal(got, []int{42}) {
				t.Errorf("%s: obtenido %v", nombre, got)
			}
		})
	}
}

func TestDosElementos(t *testing.T) {
	for nombre, ordenar := range ordenadores {
		t.Run(nombre, func(t *testing.T) {
			got := []int{2, 1}
			ordenar(got)
			if !slices.Equal(got, []int{1, 2}) {
				t.Errorf("%s: obtenido %v", nombre, got)
			}
		})
	}
}

func TestOrdenamientoDescendente(t *testing.T) {
	got := []int{64, 25, 12, 22, 11}
	SelectionSortDesc(got)
	if !slices.Equal(got, []int{64, 25, 22, 12, 11}) {
		t.Errorf("SelectionSortDesc: obtenido %v", got)
	}

	got2 := []int{64, 25, 12, 22, 11}
	InsertionSortDesc(got2)
	if !slices.Equal(got2, []int{64, 25, 22, 12, 11}) {
		t.Errorf("InsertionSortDesc: obtenido %v", got2)
	}
}

func TestOrdenamientoStrings(t *testing.T) {
	got := []string{"pera", "manzana", "banana", "uva"}
	QuickSort(got)
	want := []string{"banana", "manzana", "pera", "uva"}
	if !slices.Equal(got, want) {
		t.Errorf("QuickSort strings: obtenido %v, esperado %v", got, want)
	}
}
