// Lista Doblemente Enlazada en Go.
//
// Cada nodo conoce tanto a su siguiente como a su anterior. Se usa como
// base para implementar una Cola (Queue) eficiente.
//
// Ejecutar con:
//
//	go run ./doubly-linked-list
package main

import (
	"fmt"
	"strings"
)

// Node es un nodo de la lista doblemente enlazada.
type Node struct {
	data string
	next *Node
	prev *Node
}

// DoublyLinkedList mantiene referencias al primer y último nodo.
type DoublyLinkedList struct {
	first *Node
	last  *Node
}

// NewDoublyLinkedList crea una lista vacía.
func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{first: nil, last: nil}
}

// InsertAtEnd agrega un elemento al final. Complejidad: O(1).
func (l *DoublyLinkedList) InsertAtEnd(data string) {
	nuevo := &Node{data: data}

	if l.last == nil {
		// lista vacía: el nuevo nodo es primero y último
		l.first = nuevo
		l.last = nuevo
		return
	}

	nuevo.prev = l.last
	l.last.next = nuevo
	l.last = nuevo
}

// RemoveFromFront elimina y retorna el primer elemento. Complejidad: O(1).
func (l *DoublyLinkedList) RemoveFromFront() (string, bool) {
	if l.first == nil {
		return "", false
	}

	valor := l.first.data
	l.first = l.first.next

	if l.first != nil {
		l.first.prev = nil
	} else {
		// la lista quedó vacía
		l.last = nil
	}

	return valor, true
}

// ToSlice retorna todos los elementos como slice. Complejidad: O(n).
func (l *DoublyLinkedList) ToSlice() []string {
	resultado := []string{}
	nodo := l.first
	for nodo != nil {
		resultado = append(resultado, nodo.data)
		nodo = nodo.next
	}
	return resultado
}

// ToSliceReverse retorna los elementos desde el final hacia el inicio.
func (l *DoublyLinkedList) ToSliceReverse() []string {
	resultado := []string{}
	nodo := l.last
	for nodo != nil {
		resultado = append(resultado, nodo.data)
		nodo = nodo.prev
	}
	return resultado
}

// Len retorna el número de elementos. Complejidad: O(n).
func (l *DoublyLinkedList) Len() int {
	contador := 0
	nodo := l.first
	for nodo != nil {
		contador++
		nodo = nodo.next
	}
	return contador
}

// IsEmpty verifica si la lista está vacía.
func (l *DoublyLinkedList) IsEmpty() bool {
	return l.first == nil
}

// String imprime la lista en formato [a <-> b <-> c].
func (l *DoublyLinkedList) String() string {
	return "[" + strings.Join(l.ToSlice(), " <-> ") + "]"
}

// Queue implementa una Cola FIFO sobre la lista doblemente enlazada.
type Queue struct {
	list *DoublyLinkedList
}

// NewQueue crea una cola vacía.
func NewQueue() *Queue {
	return &Queue{list: NewDoublyLinkedList()}
}

// Enqueue agrega un elemento al final de la cola. Complejidad: O(1).
func (q *Queue) Enqueue(data string) {
	q.list.InsertAtEnd(data)
}

// Dequeue elimina y retorna el primer elemento de la cola. Complejidad: O(1).
func (q *Queue) Dequeue() (string, bool) {
	return q.list.RemoveFromFront()
}

// IsEmpty verifica si la cola está vacía.
func (q *Queue) IsEmpty() bool {
	return q.list.IsEmpty()
}

func main() {
	fmt.Println("=== Lista Doblemente Enlazada ===")
	lista := NewDoublyLinkedList()
	lista.InsertAtEnd("A")
	lista.InsertAtEnd("B")
	lista.InsertAtEnd("C")
	fmt.Printf("  Lista: %s\n", lista.String())
	fmt.Printf("  Longitud: %d\n", lista.Len())
	fmt.Printf("  Inversa: %s\n", "["+strings.Join(lista.ToSliceReverse(), " <-> ")+"]")

	if valor, ok := lista.RemoveFromFront(); ok {
		fmt.Printf("  RemoveFromFront() = %q → %s\n", valor, lista.String())
	}

	fmt.Println("\n=== Cola (Queue) sobre la lista ===")
	cola := NewQueue()
	cola.Enqueue("Ana")
	cola.Enqueue("Carlos")
	cola.Enqueue("Beatriz")

	for !cola.IsEmpty() {
		persona, _ := cola.Dequeue()
		fmt.Printf("  Se atendió a: %s\n", persona)
	}
}
