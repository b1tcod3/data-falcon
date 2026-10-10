package main

import (
	"reflect"
	"testing"
)

func TestListaVacia(t *testing.T) {
	lista := NewLinkedList()
	if !lista.IsEmpty() {
		t.Error("la lista nueva debería estar vacía")
	}
	if lista.Len() != 0 {
		t.Errorf("Len() debería ser 0, es %d", lista.Len())
	}
	if _, ok := lista.PopFront(); ok {
		t.Error("PopFront sobre lista vacía no debería devolver ok")
	}
	if _, ok := lista.PeekFront(); ok {
		t.Error("PeekFront sobre lista vacía no debería devolver ok")
	}
	if got := lista.ToSlice(); len(got) != 0 {
		t.Errorf("ToSlice() debería ser vacío, es %v", got)
	}
}

func TestPushFront(t *testing.T) {
	lista := NewLinkedList()
	lista.PushFront("mundo")
	lista.PushFront("hola")
	if lista.IsEmpty() {
		t.Error("la lista no debería estar vacía")
	}
	if lista.Len() != 2 {
		t.Errorf("Len() debería ser 2, es %d", lista.Len())
	}
	got := lista.ToSlice()
	want := []string{"hola", "mundo"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestPushBack(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.PushBack("c")
	if lista.Len() != 3 {
		t.Errorf("Len() debería ser 3, es %d", lista.Len())
	}
	got := lista.ToSlice()
	want := []string{"a", "b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestPopFront(t *testing.T) {
	lista := NewLinkedList()
	lista.PushFront("x")
	lista.PushFront("y")
	lista.PushFront("z")

	if v, ok := lista.PopFront(); !ok || v != "z" {
		t.Errorf("PopFront() = (%q, %v), esperado (\"z\", true)", v, ok)
	}
	if v, ok := lista.PopFront(); !ok || v != "y" {
		t.Errorf("PopFront() = (%q, %v), esperado (\"y\", true)", v, ok)
	}
	if v, ok := lista.PopFront(); !ok || v != "x" {
		t.Errorf("PopFront() = (%q, %v), esperado (\"x\", true)", v, ok)
	}
	if _, ok := lista.PopFront(); ok {
		t.Error("PopFront sobre lista vacía no debería devolver ok")
	}
}

func TestPeekFront(t *testing.T) {
	lista := NewLinkedList()
	if _, ok := lista.PeekFront(); ok {
		t.Error("PeekFront sobre lista vacía no debería devolver ok")
	}

	lista.PushFront("primero")
	if v, ok := lista.PeekFront(); !ok || v != "primero" {
		t.Errorf("PeekFront() = (%q, %v), esperado (\"primero\", true)", v, ok)
	}

	lista.PushFront("nuevo_primero")
	if v, ok := lista.PeekFront(); !ok || v != "nuevo_primero" {
		t.Errorf("PeekFront() = (%q, %v), esperado (\"nuevo_primero\", true)", v, ok)
	}
}

func TestRead(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.PushBack("c")

	casos := []struct {
		indice int
		valor  string
		ok     bool
	}{
		{0, "a", true},
		{1, "b", true},
		{2, "c", true},
		{3, "", false},
		{99, "", false},
	}
	for _, c := range casos {
		v, ok := lista.Read(c.indice)
		if ok != c.ok || (ok && v != c.valor) {
			t.Errorf("Read(%d) = (%q, %v), esperado (%q, %v)", c.indice, v, ok, c.valor, c.ok)
		}
	}
}

func TestReadListaVacia(t *testing.T) {
	lista := NewLinkedList()
	if _, ok := lista.Read(0); ok {
		t.Error("Read(0) sobre lista vacía no debería devolver ok")
	}
}

func TestIndexOf(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("once")
	lista.PushBack("upon")
	lista.PushBack("a")
	lista.PushBack("time")

	casos := []struct {
		valor  string
		indice int
		ok     bool
	}{
		{"once", 0, true},
		{"upon", 1, true},
		{"a", 2, true},
		{"time", 3, true},
		{"never", 0, false},
	}
	for _, c := range casos {
		indice, ok := lista.IndexOf(c.valor)
		if ok != c.ok || (ok && indice != c.indice) {
			t.Errorf("IndexOf(%q) = (%d, %v), esperado (%d, %v)", c.valor, indice, ok, c.indice, c.ok)
		}
	}
}

func TestIndexOfListaVacia(t *testing.T) {
	lista := NewLinkedList()
	if _, ok := lista.IndexOf("anything"); ok {
		t.Error("IndexOf sobre lista vacía no debería devolver ok")
	}
}

func TestInsertAtIndexInicio(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("b")
	lista.PushBack("c")
	lista.InsertAtIndex(0, "a")
	got := lista.ToSlice()
	want := []string{"a", "b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestInsertAtIndexMedio(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("c")
	lista.InsertAtIndex(1, "b")
	got := lista.ToSlice()
	want := []string{"a", "b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestInsertAtIndexFinal(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.InsertAtIndex(2, "c")
	got := lista.ToSlice()
	want := []string{"a", "b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestInsertAtIndexListaVacia(t *testing.T) {
	lista := NewLinkedList()
	lista.InsertAtIndex(0, "primero")
	got := lista.ToSlice()
	want := []string{"primero"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestInsertAtIndexFueraDeLimites(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.InsertAtIndex(5, "b")
	got := lista.ToSlice()
	want := []string{"a"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestDeleteAtIndexInicio(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.PushBack("c")
	lista.DeleteAtIndex(0)
	got := lista.ToSlice()
	want := []string{"b", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestDeleteAtIndexMedio(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.PushBack("c")
	lista.DeleteAtIndex(1)
	got := lista.ToSlice()
	want := []string{"a", "c"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestDeleteAtIndexFinal(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	lista.PushBack("c")
	lista.DeleteAtIndex(2)
	got := lista.ToSlice()
	want := []string{"a", "b"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestDeleteAtIndexUnicoElemento(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("unico")
	lista.DeleteAtIndex(0)
	if !lista.IsEmpty() {
		t.Error("la lista debería estar vacía después de eliminar el único elemento")
	}
}

func TestDeleteAtIndexListaVacia(t *testing.T) {
	lista := NewLinkedList()
	lista.DeleteAtIndex(0) // no debe panic
	if !lista.IsEmpty() {
		t.Error("la lista debería seguir vacía")
	}
}

func TestDeleteAtIndexFueraDeLimites(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.DeleteAtIndex(5)
	got := lista.ToSlice()
	want := []string{"a"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestEjemploOnceUponATime(t *testing.T) {
	lista := NewLinkedList()
	lista.PushFront("time")
	lista.PushFront("a")
	lista.PushFront("upon")
	lista.PushFront("once")

	got := lista.ToSlice()
	want := []string{"once", "upon", "a", "time"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
	if lista.Len() != 4 {
		t.Errorf("Len() debería ser 4, es %d", lista.Len())
	}
}

func TestPushFrontYPushBackCombinados(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("medio")
	lista.PushFront("inicio")
	lista.PushBack("final")

	got := lista.ToSlice()
	want := []string{"inicio", "medio", "final"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("ToSlice() = %v, esperado %v", got, want)
	}
}

func TestUnSoloElemento(t *testing.T) {
	lista := NewLinkedList()
	lista.PushFront("unico")
	if lista.Len() != 1 {
		t.Errorf("Len() debería ser 1, es %d", lista.Len())
	}
	if v, ok := lista.PeekFront(); !ok || v != "unico" {
		t.Errorf("PeekFront() = (%q, %v)", v, ok)
	}
	if v, ok := lista.PopFront(); !ok || v != "unico" {
		t.Errorf("PopFront() = (%q, %v)", v, ok)
	}
	if !lista.IsEmpty() {
		t.Error("la lista debería estar vacía")
	}
}

func TestString(t *testing.T) {
	lista := NewLinkedList()
	lista.PushBack("a")
	lista.PushBack("b")
	if got := lista.String(); got != "[a -> b]" {
		t.Errorf("String() = %q, esperado %q", got, "[a -> b]")
	}
}
