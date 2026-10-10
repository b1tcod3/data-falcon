// Árbol Binario de Búsqueda con strings (catálogo de libros).
//
// Muestra cómo un BST también funciona con datos tipo string, comparando
// alfabéticamente. El recorrido in-order devuelve los títulos ordenados.
//
// Ejecutar con:
//
//	go run ./arbol-binario/bst-libros
package main

import (
	"fmt"
	"strings"
)

// TreeNode es un nodo con valor de tipo string.
type TreeNode struct {
	value string
	left  *TreeNode
	right *TreeNode
}

// Insert inserta un valor respetando la propiedad del BST (comparación lexicográfica).
func Insert(node *TreeNode, value string) *TreeNode {
	if node == nil {
		return &TreeNode{value: value}
	}

	if value < node.value {
		node.left = Insert(node.left, value)
	} else {
		node.right = Insert(node.right, value)
	}
	return node
}

// TraverseAndPrint recorre el árbol in-order y devuelve los valores de forma ordenada.
func TraverseAndPrint(node *TreeNode) []string {
	resultado := []string{}
	var recorrer func(*TreeNode)
	recorrer = func(n *TreeNode) {
		if n == nil {
			return
		}
		recorrer(n.left)
		resultado = append(resultado, n.value)
		recorrer(n.right)
	}
	recorrer(node)
	return resultado
}

func main() {
	var raiz *TreeNode

	// Insertamos libros (los insertamos en este orden arbitrario)
	libros := []string{"El Quijote", "1984", "Cien años de soledad"}
	for _, libro := range libros {
		raiz = Insert(raiz, libro)
	}

	fmt.Println("=== Catálogo de libros (BST) ===")
	fmt.Printf("  In-order: %s\n", strings.Join(TraverseAndPrint(raiz), " | "))

	fmt.Println("\n=== Insertando más libros ===")
	for _, libro := range []string{"Matar a un ruiseñor", "Orgullo y prejuicio"} {
		raiz = Insert(raiz, libro)
	}
	fmt.Printf("  In-order: %s\n", strings.Join(TraverseAndPrint(raiz), " | "))
}
