package main

import (
	"reflect"
	"testing"
)

func TestListaDoblementeVacia(t *testing.T) {
	lista := NewDoublyLinkedList()
	if !lista.IsEmpty() {
		t.Error("la lista nueva debería estar vacía")
	}
	if lista.Len() != 0 {
		t.Errorf("Len() debería ser 0, es %d", lista.Len())
	}
	if _, ok := lista.RemoveFromFront(); ok {
		t.Error("RemoveFromFront sobre lista vacía no debería devolver ok")
	}
}

func TestInsertAtEnd(t *testing.T) {
	lista := NewDoublyLinkedList()
	lista.InsertAtEnd("a")
	lista.InsertAtEnd("b")
	lista.InsertAtEnd("c")

	got := lista.ToSlice()
	want := []string{"a", "b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
	if lista.Len() != 3 {
		t.Errorf("Len() debería ser 3, es %d", lista.Len())
	}
}

func TestRecorridoInverso(t *testing.T) {
	lista := NewDoublyLinkedList()
	lista.InsertAtEnd("a")
	lista.InsertAtEnd("b")
	lista.InsertAtEnd("c")

	got := lista.ToSliceReverse()
	want := []string{"c", "b", "a"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSliceReverse() = %v, esperado %v", got, want)
	}
}

func TestRemoveFromFront(t *testing.T) {
	lista := NewDoublyLinkedList()
	lista.InsertAtEnd("a")
	lista.InsertAtEnd("b")
	lista.InsertAtEnd("c")

	if v, ok := lista.RemoveFromFront(); !ok || v != "a" {
		t.Errorf("RemoveFromFront() = (%q, %v), esperado (\"a\", true)", v, ok)
	}
	got := lista.ToSlice()
	want := []string{"b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}

	// el último nodo debe quedar bien enlazado hacia atrás
	reverse := lista.ToSliceReverse()
	wantReverse := []string{"c", "b"}
	if !reflect.DeepEqual(reverse, wantReverse) {
		t.Errorf("ToSliceReverse() = %v, esperado %v", reverse, wantReverse)
	}
}

func TestRemoveFromFrontHastaVaciar(t *testing.T) {
	lista := NewDoublyLinkedList()
	lista.InsertAtEnd("unico")

	if v, ok := lista.RemoveFromFront(); !ok || v != "unico" {
		t.Errorf("RemoveFromFront() = (%q, %v)", v, ok)
	}
	if !lista.IsEmpty() {
		t.Error("la lista debería quedar vacía")
	}
	if lista.last != nil {
		t.Error("last debería ser nil tras vaciar la lista")
	}
}

func TestQueueFIFO(t *testing.T) {
	cola := NewQueue()
	cola.Enqueue("Ana")
	cola.Enqueue("Carlos")
	cola.Enqueue("Beatriz")

	orden := []string{}
	for !cola.IsEmpty() {
		v, _ := cola.Dequeue()
		orden = append(orden, v)
	}

	want := []string{"Ana", "Carlos", "Beatriz"}
	if !reflect.DeepEqual(orden, want) {
		t.Errorf("orden de atención = %v, esperado %v", orden, want)
	}
}
