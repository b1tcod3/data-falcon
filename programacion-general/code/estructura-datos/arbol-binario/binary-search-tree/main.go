// Árbol Binario de Búsqueda (Binary Search Tree) en Go.
//
// Un árbol binario de búsqueda es un árbol binario en el que para cada nodo:
//   - Todos los valores del subárbol izquierdo son menores que el nodo.
//   - Todos los valores del subárbol derecho son mayores que el nodo.
//
// Ejecutar con:
//
//	go run ./arbol-binario/binary-search-tree
package main

import (
	"fmt"
	"strings"
)

// TreeNode es un nodo del árbol binario de búsqueda.
type TreeNode struct {
	value int
	left  *TreeNode
	right *TreeNode
}

// BinarySearchTree representa el árbol.
type BinarySearchTree struct {
	root *TreeNode
}

// NewBinarySearchTree crea un árbol vacío.
func NewBinarySearchTree() *BinarySearchTree {
	return &BinarySearchTree{root: nil}
}

// Search indica si un valor existe en el árbol. Complejidad: O(log n) promedio.
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

// Insert agrega un valor al árbol. Complejidad: O(log n) promedio.
func (bst *BinarySearchTree) Insert(value int) {
	nuevo := &TreeNode{value: value}

	if bst.root == nil {
		bst.root = nuevo
		return
	}

	nodo := bst.root
	for {
		if value < nodo.value {
			if nodo.left == nil {
				nodo.left = nuevo
				return
			}
			nodo = nodo.left
		} else {
			if nodo.right == nil {
				nodo.right = nuevo
				return
			}
			nodo = nodo.right
		}
	}
}

// Delete elimina un valor del árbol. Complejidad: O(log n) promedio.
func (bst *BinarySearchTree) Delete(value int) {
	bst.root = deleteNode(bst.root, value)
}

func deleteNode(node *TreeNode, value int) *TreeNode {
	if node == nil {
		return nil
	}

	if value < node.value {
		node.left = deleteNode(node.left, value)
	} else if value > node.value {
		node.right = deleteNode(node.right, value)
	} else {
		// Caso 1: nodo hoja
		if node.left == nil && node.right == nil {
			return nil
		}
		// Caso 2: solo hijo derecho
		if node.left == nil {
			return node.right
		}
		// Caso 3: solo hijo izquierdo
		if node.right == nil {
			return node.left
		}
		// Caso 4: dos hijos → sucesor in-order (mínimo del subárbol derecho)
		sucesor := minValueNode(node.right)
		node.value = sucesor.value
		node.right = deleteNode(node.right, sucesor.value)
	}

	return node
}

func minValueNode(node *TreeNode) *TreeNode {
	actual := node
	for actual.left != nil {
		actual = actual.left
	}
	return actual
}

// InOrder retorna el recorrido in-order (izquierda, nodo, derecha),
// que para un BST produce los valores ordenados.
func (bst *BinarySearchTree) InOrder() []int {
	resultado := []int{}
	var recorrer func(*TreeNode)
	recorrer = func(n *TreeNode) {
		if n == nil {
			return
		}
		recorrer(n.left)
		resultado = append(resultado, n.value)
		recorrer(n.right)
	}
	recorrer(bst.root)
	return resultado
}

func (bst *BinarySearchTree) String() string {
	valores := bst.InOrder()
	parts := make([]string, len(valores))
	for i, v := range valores {
		parts[i] = fmt.Sprintf("%d", v)
	}
	return "[" + strings.Join(parts, ", ") + "]"
}

func main() {
	fmt.Println("=== Árbol Binario de Búsqueda ===")
	arbol := NewBinarySearchTree()
	for _, v := range []int{50, 30, 70, 20, 40, 60, 80} {
		arbol.Insert(v)
	}
	fmt.Printf("  In-order (ordenado): %s\n", arbol.String())
	fmt.Printf("  Search(40) = %v\n", arbol.Search(40))
	fmt.Printf("  Search(45) = %v\n", arbol.Search(45))

	fmt.Println("\n=== Insertar 45 ===")
	arbol.Insert(45)
	fmt.Printf("  In-order: %s\n", arbol.String())
	fmt.Printf("  Search(45) = %v\n", arbol.Search(45))

	fmt.Println("\n=== Eliminar 20 (hoja), 30 (un hijo), 50 (dos hijos) ===")
	arbol.Delete(20)
	fmt.Printf("  Tras Delete(20): %s\n", arbol.String())
	arbol.Delete(30)
	fmt.Printf("  Tras Delete(30): %s\n", arbol.String())
	arbol.Delete(50)
	fmt.Printf("  Tras Delete(50): %s\n", arbol.String())

	fmt.Println("\n=== Árbol degenerado (equivale a lista) ===")
	degenerado := NewBinarySearchTree()
	for _, v := range []int{10, 20, 30, 40, 50} {
		degenerado.Insert(v)
	}
	fmt.Printf("  In-order: %s\n", degenerado.String())
	fmt.Printf("  Search(40) = %v\n", degenerado.Search(40))
}
