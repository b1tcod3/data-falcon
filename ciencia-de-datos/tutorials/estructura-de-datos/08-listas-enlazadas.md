# Listas Enlazadas

Una **lista enlazada** almacena los datos en nodos conectados por punteros. A diferencia del slice (memoria contigua), cada nodo puede estar en cualquier parte de la memoria; lo que los une es la referencia al siguiente (y, en la variante doble, al anterior).

## Lista enlazada simple

```go
type Node struct {
	data string
	next *Node
}

type LinkedList struct {
	firstNode *Node
}
```

Operaciones principales:

| Operación | Complejidad |
| --- | --- |
| `PushFront` (insertar al inicio) | O(1) |
| `PushBack` (insertar al final) | O(n) |
| `PopFront` (eliminar el inicio) | O(1) |
| `Read` / `IndexOf` / `InsertAtIndex` / `DeleteAtIndex` | O(n) |

La operación `index_of` demuestra la desventaja frente al slice: encontrar el valor `"time"` en una lista de 4 elementos requiere recorrer nodo por nodo:

```go
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
```

El algoritmo `once upon a time` construye la frase con `PushFront` (que inserta al inicio), por lo que se agregan las palabras en orden inverso.

Código: [`listas-enlazadas/main.go`](../../../programacion-general/code/estructura-datos/listas-enlazadas/main.go) y sus [pruebas](../../../programacion-general/code/estructura-datos/listas-enlazadas/linked_list_test.go).

```bash
go run ./listas-enlazadas
# [once -> upon -> a -> time]
```

## Lista doblemente enlazada

Cada nodo conoce a su siguiente **y** a su anterior, lo que permite recorrer en ambas direcciones:

```go
type Node struct {
	data string
	next *Node
	prev *Node
}
```

Con punteros a `first` y `last`, tanto insertar al final como eliminar al inicio son O(1). Esto la convierte en la base ideal para una **cola eficiente**:

```go
func (q *Queue) Enqueue(data string) { q.list.InsertAtEnd(data) }     // O(1)
func (q *Queue) Dequeue() (string, bool) { return q.list.RemoveFromFront() } // O(1)
```

En la versión Rust el ejemplo usaba `Rc<RefCell<...>>` para el nodo anterior; en Go basta el puntero nativo `*Node`, lo que simplifica bastante el código.

Código: [`doubly-linked-list/main.go`](../../../programacion-general/code/estructura-datos/doubly-linked-list/main.go) y sus [pruebas](../../../programacion-general/code/estructura-datos/doubly-linked-list/doubly_linked_list_test.go).

```bash
go run ./doubly-linked-list
# Se atendió a: Ana
# Se atendió a: Carlos
# Se atendió a: Beatriz
```

## ¿Cuándo fijarse en las listas enlazadas?

- Se ganan inserciones y eliminaciones en los extremos en O(1).
- Se pierde el **acceso aleatorio**: leer el índice `k` cuesta O(k).
- En Go (como en los demás lenguajes modernos), un slice suele ser suficiente; las listas enlazadas destacan cuando el patrón dominante es insertar/eliminar en el medio de colecciones grandes.