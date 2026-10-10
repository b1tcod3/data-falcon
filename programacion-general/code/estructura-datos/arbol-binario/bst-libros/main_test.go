package main

import (
	"reflect"
	"testing"
)

func TestTraverseAndPrintOrdenAlfabetico(t *testing.T) {
	var raiz *TreeNode
	for _, libro := range []string{"El Quijote", "1984", "Cien años de soledad"} {
		raiz = Insert(raiz, libro)
	}

	got := TraverseAndPrint(raiz)
	// orden lexicográfico (puede variar con acentos/mayúsculas; aquí ASCII simple)
	want := []string{"1984", "Cien años de soledad", "El Quijote"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("TraverseAndPrint() = %v, esperado %v", got, want)
	}
}

func TestArbolVacio(t *testing.T) {
	var raiz *TreeNode
	got := TraverseAndPrint(raiz)
	if len(got) != 0 {
		t.Errorf("se esperaba lista vacía, se obtuvo %v", got)
	}
}

func TestInsertNodoRaiz(t *testing.T) {
	var raiz *TreeNode
	raiz = Insert(raiz, "primer libro")
	if raiz == nil || raiz.value != "primer libro" {
		t.Errorf("la raíz debería tener el primer libro, es %v", raiz)
	}
}

func TestInsertLibrosAdicionales(t *testing.T) {
	var raiz *TreeNode
	for _, libro := range []string{"Cien años de soledad", "Orgullo y prejuicio", "Matar a un ruiseñor"} {
		raiz = Insert(raiz, libro)
	}

	got := TraverseAndPrint(raiz)
	want := []string{"Cien años de soledad", "Matar a un ruiseñor", "Orgullo y prejuicio"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("TraverseAndPrint() = %v, esperado %v", got, want)
	}
}
