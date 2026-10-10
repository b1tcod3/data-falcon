# Árboles Binarios de Búsqueda

Un **árbol binario de búsqueda** (BST) es una estructura jerárquica donde cada nodo tiene a lo sumo dos hijos y cumple la propiedad fundamental:

- Todo el **subárbol izquierdo** contiene valores **menores** que el nodo.
- Todo el **subárbol derecho** contiene valores **mayores** que el nodo.

Gracias a esa propiedad, buscar un valor es como jugar a "más alto o más bajo": en cada paso se descarta la mitad del árbol restante.

## Nodo y árbol en Go

```go
type TreeNode struct {
	value int
	left  *TreeNode
	right *TreeNode
}

type BinarySearchTree struct {
	root *TreeNode
}
```

## Operaciones

### Búsqueda (iterativa)

```go
func (bst *BinarySearchTree) Search(value int) bool {
	nodo := bst.root
	for nodo != nil {
		switch {
		case value == nodo.value:
			return true
		case value < nodo.value:
			nodo = nodo.left
		default:
			nodo = nodo.right
		}
	}
	return false
}
```

### Inserción

Desciende por el camino correcto hasta encontrar un hueco `nil`:

```go
func (bst *BinarySearchTree) Insert(value int) {
	nuevo := &TreeNode{value: value}
	if bst.root == nil {
		bst.root = nuevo
		return
	}
	nodo := bst.root
	for {
		if value < nodo.value {
			if nodo.left == nil { nodo.left = nuevo; return }
			nodo = nodo.left
		} else {
			if nodo.right == nil { nodo.right = nuevo; return }
			nodo = nodo.right
		}
	}
}
```

### Eliminación

El caso complejo es cuando el nodo tiene **dos hijos**: se reemplaza por su *sucesor in-order* (el mínimo del subárbol derecho) y se elimina el sucesor:

```go
func deleteNode(node *TreeNode, value int) *TreeNode {
	// ... casos hoja y de un solo hijo ...
	// Caso dos hijos
	sucesor := minValueNode(node.right)
	node.value = sucesor.value
	node.right = deleteNode(node.right, sucesor.value)
	return node
}
```

## Complejidad y balance

| Operación | Árbol balanceado | Árbol degenerado |
| --- | --- | --- |
| Search / Insert / Delete | O(log n) | O(n) |

Un árbol **degenerado** (se insertan valores ordenados `10, 20, 30, 40, 50`) degenera en una lista y pierde toda la ventaja. Las estructuras **autobalanceadas** (AVL, Red-Black) garantizan O(log n) siempre.

Un detalle elegante: el **recorrido in-order** (izquierda → nodo → derecha) devuelve los valores **ordenados**:

```go
func (bst *BinarySearchTree) InOrder() []int {
	// recorrido recursivo
}
```

## Árbol de libros (valores string)

El mismo árbol funciona con cadenas en un catálogo de libros: la comparación pasa a ser alfabética.

Código: [`arbol-binario/binary-search-tree/main.go`](../../../programacion-general/code/estructura-datos/arbol-binario/binary-search-tree/main.go), [`arbol-binario/bst-libros/main.go`](../../../programacion-general/code/estructura-datos/arbol-binario/bst-libros/main.go) y sus [pruebas](../../../programacion-general/code/estructura-datos/arbol-binario/binary-search-tree/main_test.go).

```bash
cd programacion-general/code/estructura-datos
go run ./arbol-binario/binary-search-tree
# In-order (ordenado): [20, 30, 40, 50, 60, 70, 80]
go run ./arbol-binario/bst-libros
# In-order: 1984 | Cien años de soledad | El Quijote
```

En la versión Rust se usaba `Option<Box<TreeNode>>` para representar la ausencia de hijos; en Go esa ausencia es simplemente el puntero `nil`.