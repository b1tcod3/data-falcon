// Lista Enlazada Simple en Go.
//
// Este programa contiene una implementación de una lista enlazada simple,
// donde cada nodo apunta al siguiente. El último nodo de la lista tiene
// next = nil.
//
// Ejecutar con:
//
//	go run ./listas-enlazadas
package main

import (
	"fmt"
	"strings"
)

// Node es un nodo individual de la lista enlazada.
type Node struct {
	data string
	next *Node
}

// newNode crea un nodo con el dato proporcionado.
func newNode(data string) *Node {
	return &Node{data: data, next: nil}
}

// LinkedList es la lista enlazada simple. Mantiene una referencia al
// primer nodo (cabeza).
type LinkedList struct {
	firstNode *Node
}

// NewLinkedList crea una lista vacía.
func NewLinkedList() *LinkedList {
	return &LinkedList{firstNode: nil}
}

// PushFront agrega un elemento al inicio de la lista. Complejidad: O(1).
func (l *LinkedList) PushFront(data string) {
	nuevo := newNode(data)
	nuevo.next = l.firstNode
	l.firstNode = nuevo
}

// PushBack agrega un elemento al final de la lista. Complejidad: O(n).
func (l *LinkedList) PushBack(data string) {
	nuevo := newNode(data)

	if l.firstNode == nil {
		l.firstNode = nuevo
		return
	}

	actual := l.firstNode
	for actual.next != nil {
		actual = actual.next
	}
	actual.next = nuevo
}

// PopFront elimina y retorna el primer elemento. Complejidad: O(1).
func (l *LinkedList) PopFront() (string, bool) {
	if l.firstNode == nil {
		return "", false
	}
	nodo := l.firstNode
	l.firstNode = nodo.next
	return nodo.data, true
}

// PeekFront obtiene el primer elemento sin eliminarlo.
func (l *LinkedList) PeekFront() (string, bool) {
	if l.firstNode == nil {
		return "", false
	}
	return l.firstNode.data, true
}

// Read obtiene el elemento en el índice especificado sin eliminarlo.
// Devuelve false si el índice está fuera de los límites. Complejidad: O(n).
func (l *LinkedList) Read(index int) (string, bool) {
	nodo := l.firstNode
	indiceActual := 0

	for nodo != nil && indiceActual < index {
		nodo = nodo.next
		indiceActual++
	}

	if nodo == nil {
		return "", false
	}
	return nodo.data, true
}

// IndexOf busca un valor en la lista y retorna su índice.
// Devuelve false si no se encuentra. Complejidad: O(n).
func (l *LinkedList) IndexOf(value string) (int, bool) {
	nodo := l.firstNode
	indice := 0

	for nodo != nil {
		if nodo.data == value {
			return indice, true
		}
		nodo = nodo.next
		indice++
	}

	return 0, false
}

// InsertAtIndex inserta un valor en el índice especificado.
// Si el índice es 0 inserta al inicio; si es igual a la longitud, al final;
// si es mayor que la longitud, no hace nada. Complejidad: O(n).
func (l *LinkedList) InsertAtIndex(index int, value string) {
	if index == 0 {
		l.PushFront(value)
		return
	}

	nodo := l.firstNode
	indiceActual := 0

	for nodo != nil {
		if indiceActual == index-1 {
			nuevo := newNode(value)
			nuevo.next = nodo.next
			nodo.next = nuevo
			return
		}
		nodo = nodo.next
		indiceActual++
	}
}

// DeleteAtIndex elimina el elemento en el índice especificado.
// Complejidad: O(1) para el primer nodo, O(n) en otro caso.
func (l *LinkedList) DeleteAtIndex(index int) {
	if l.firstNode == nil {
		return
	}

	if index == 0 {
		l.firstNode = l.firstNode.next
		return
	}

	nodo := l.firstNode
	indiceActual := 0

	for nodo != nil {
		if indiceActual == index-1 {
			if nodo.next != nil {
				// construimos el puente: el actual apunta al que seguía al objetivo
				nodo.next = nodo.next.next
			}
			return
		}
		nodo = nodo.next
		indiceActual++
	}
}

// ToSlice retorna una representación como slice de todos los elementos.
// Complejidad: O(n).
func (l *LinkedList) ToSlice() []string {
	resultado := []string{}
	nodo := l.firstNode
	for nodo != nil {
		resultado = append(resultado, nodo.data)
		nodo = nodo.next
	}
	return resultado
}

// Len retorna el número de elementos. Complejidad: O(n).
func (l *LinkedList) Len() int {
	contador := 0
	nodo := l.firstNode
	for nodo != nil {
		contador++
		nodo = nodo.next
	}
	return contador
}

// IsEmpty verifica si la lista está vacía.
func (l *LinkedList) IsEmpty() bool {
	return l.firstNode == nil
}

// String imprime la lista en formato [a -> b -> c].
func (l *LinkedList) String() string {
	var parts []string
	nodo := l.firstNode
	for nodo != nil {
		parts = append(parts, nodo.data)
		nodo = nodo.next
	}
	return "[" + strings.Join(parts, " -> ") + "]"
}

func main() {
	// Construimos la lista "once upon a time" usando PushFront.
	// Como PushFront agrega al inicio, construimos en orden inverso.
	listaHistoria := NewLinkedList()
	listaHistoria.PushFront("time")
	listaHistoria.PushFront("a")
	listaHistoria.PushFront("upon")
	listaHistoria.PushFront("once")

	fmt.Println("Lista enlazada:")
	fmt.Printf("  %s\n", listaHistoria.String())
	fmt.Printf("  Longitud: %d\n", listaHistoria.Len())
	fmt.Println()

	// Operación read
	if valor, ok := listaHistoria.Read(2); ok {
		fmt.Printf("  Read(2) = %q\n", valor)
	}

	// Operación index_of
	if indice, ok := listaHistoria.IndexOf("time"); ok {
		fmt.Printf("  IndexOf(\"time\") = %d\n", indice)
	}

	// Insert en el medio
	listaHistoria.InsertAtIndex(1, "very")
	fmt.Printf("  Después de InsertAtIndex(1, \"very\"): %s\n", listaHistoria.String())

	// Delete
	listaHistoria.DeleteAtIndex(1)
	fmt.Printf("  Después de DeleteAtIndex(1):         %s\n", listaHistoria.String())

	// PopFront
	if valor, ok := listaHistoria.PopFront(); ok {
		fmt.Printf("  PopFront() = %q → %s\n", valor, listaHistoria.String())
	}

	// Ejemplo con PushBack
	otraLista := NewLinkedList()
	otraLista.PushBack("esto")
	otraLista.PushBack("es")
	otraLista.PushBack("push_back")
	fmt.Printf("\n  Lista con PushBack(): %s\n", otraLista.String())
}
