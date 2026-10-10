package main

import (
	"reflect"
	"testing"
)

func nuevoArbol(nodos ...int) *BinarySearchTree {
	bst := NewBinarySearchTree()
	for _, v := range nodos {
		bst.Insert(v)
	}
	return bst
}

func TestInsertYSearch(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70, 20, 40, 60, 80)

	presentes := []int{50, 30, 70, 20, 40, 60, 80}
	for _, v := range presentes {
		if !arbol.Search(v) {
			t.Errorf("Search(%d) debería ser true", v)
		}
	}

	ausentes := []int{10, 35, 45, 65, 90}
	for _, v := range ausentes {
		if arbol.Search(v) {
			t.Errorf("Search(%d) debería ser false", v)
		}
	}
}

func TestSearchArbolVacio(t *testing.T) {
	arbol := NewBinarySearchTree()
	if arbol.Search(1) {
		t.Error("Search sobre árbol vacío debería ser false")
	}
}

func TestSearchUnSoloNodo(t *testing.T) {
	arbol := nuevoArbol(42)
	if !arbol.Search(42) {
		t.Error("Search(42) debería ser true")
	}
	if arbol.Search(41) {
		t.Error("Search(41) debería ser false")
	}
}

func TestInsertRaiz(t *testing.T) {
	arbol := NewBinarySearchTree()
	arbol.Insert(5)
	if arbol.root == nil || arbol.root.value != 5 {
		t.Errorf("la raíz debería ser 5, es %v", arbol.root)
	}
}

func TestInsertMantieneOrdenInOrder(t *testing.T) {
	arbol := nuevoArbol(5, 3, 8, 1, 4, 7, 9)
	got := arbol.InOrder()
	want := []int{1, 3, 4, 5, 7, 8, 9}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestInsertElementosRepetidos(t *testing.T) {
	arbol := nuevoArbol(10, 5, 10) // segundo 10 irá al subárbol derecho
	got := arbol.InOrder()
	want := []int{5, 10, 10}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteHoja(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70, 20, 40)
	arbol.Delete(20)
	if arbol.Search(20) {
		t.Error("Search(20) debería ser false tras eliminar")
	}
	got := arbol.InOrder()
	want := []int{30, 40, 50, 70}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteUnSoloHijo(t *testing.T) {
	arbol := nuevoArbol(50, 30, 20) // 30 solo tiene hijo izquierdo
	arbol.Delete(30)
	got := arbol.InOrder()
	want := []int{20, 50}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteSoloHijoDerecho(t *testing.T) {
	arbol := nuevoArbol(50, 70, 60, 80) // 70 con hijos 60 y 80
	arbol.Delete(70)
	got := arbol.InOrder()
	want := []int{50, 60, 80}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteDosHijos(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70, 20, 40, 60, 80)
	arbol.Delete(50) // dos hijos → sucesor in-order
	if arbol.Search(50) {
		t.Error("Search(50) debería ser false tras eliminar")
	}
	got := arbol.InOrder()
	want := []int{20, 30, 40, 60, 70, 80}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteRaizUnicoNodo(t *testing.T) {
	arbol := nuevoArbol(42)
	arbol.Delete(42)
	if arbol.root != nil {
		t.Error("la raíz debería ser nil tras eliminar el único nodo")
	}
}

func TestDeleteElementoInexistente(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70)
	arbol.Delete(99) // no debe alterar el árbol
	got := arbol.InOrder()
	want := []int{30, 50, 70}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteDerechaSubarbol(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70, 60, 80, 75, 90)
	arbol.Delete(60)
	if arbol.Search(60) {
		t.Error("Search(60) debería ser false")
	}
	got := arbol.InOrder()
	want := []int{30, 50, 70, 75, 80, 90}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestArbolDegeneradoEquivaleLista(t *testing.T) {
	arbol := nuevoArbol(10, 20, 30, 40, 50)
	got := arbol.InOrder()
	want := []int{10, 20, 30, 40, 50}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestDeleteRaizArbolDegenerado(t *testing.T) {
	arbol := nuevoArbol(10, 20, 30)
	arbol.Delete(10) // raíz con un solo hijo derecho
	got := arbol.InOrder()
	want := []int{20, 30}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("InOrder() = %v, esperado %v", got, want)
	}
}

func TestSucesorInOrder(t *testing.T) {
	arbol := nuevoArbol(50, 30, 70, 20, 40, 60, 80)
	sucesor := minValueNode(arbol.root.right)
	if sucesor.value != 60 {
		t.Errorf("el sucesor in-order de la raíz debería ser 60, es %d", sucesor.value)
	}
}
