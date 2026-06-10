#![allow(dead_code)]

//! Árbol Binario de Búsqueda en Rust (Binary Search Tree)
//!
//! Este módulo contiene la implementación de un BST donde cada nodo tiene
//! un valor, un hijo izquierdo (menor) y un hijo derecho (mayor).
//!
//! ## Funcionamiento
//! En un BST, para cada nodo, todos los elementos del subárbol izquierdo
//! son menores y todos los del derecho son mayores. Esto permite búsquedas
//! eficientes en O(log N) cuando el árbol está balanceado.

/// Nodo del árbol binario de búsqueda
///
/// Cada nodo contiene un valor entero y referencias a sus hijos izquierdo
/// y derecho. El uso de `Box` permite recursión en la estructura.
///
/// # Complejidad de búsqueda
/// * **Mejor caso**: O(1) — el valor está en la raíz
/// * **Caso promedio**: O(log N) — árbol balanceado
/// * **Peor caso**: O(N) — árbol degenerado (lista enlazada)
#[derive(Debug)]
struct TreeNode {
    value: i32,
    left: Option<Box<TreeNode>>,
    right: Option<Box<TreeNode>>,
}

impl TreeNode {
    fn new(val: i32) -> Self {
        TreeNode {
            value: val,
            left: None,
            right: None,
        }
    }

    /// Busca un valor en el árbol recursivamente
    ///
    /// # Parámetros
    /// * `target` - El valor entero a buscar
    ///
    /// # Devuelve
    /// * `Some(&TreeNode)` - una referencia al nodo si se encuentra
    /// * `None` - si el valor no existe en el árbol
    ///
    /// # Ejemplo
    /// ```
    /// let mut raiz = TreeNode::new(50);
    /// // ... construir árbol ...
    /// let resultado = raiz.search(25);
    /// assert!(resultado.is_some());
    /// ```
    ///
    /// # Complejidad
    /// O(log N) en promedio, O(N) en el peor caso
    fn search(&self, target: i32) -> Option<&TreeNode> {
        if self.value == target {
            return Some(self);
        }

        if target < self.value {
            self.left.as_ref().and_then(|child| child.search(target))
        } else {
            self.right.as_ref().and_then(|child| child.search(target))
        }
    }

    /// Inserta un valor en el árbol recursivamente
    ///
    /// Recorre el árbol hasta encontrar la posición correcta y lo inserta
    /// como hoja. Si el valor ya existe, no hace nada.
    ///
    /// # Parámetros
    /// * `value` - El valor entero a insertar
    ///
    /// # Ejemplo
    /// ```
    /// let mut raiz = TreeNode::new(50);
    /// raiz.insert(25);
    /// raiz.insert(75);
    /// assert!(raiz.search(25).is_some());
    /// ```
    ///
    /// # Complejidad
    /// O(log N) en promedio, O(N) en el peor caso
    fn insert(&mut self, value: i32) {
        if value < self.value {
            match &mut self.left {
                None => self.left = Some(Box::new(TreeNode::new(value))),
                Some(node) => node.insert(value),
            }
        } else if value > self.value {
            match &mut self.right {
                None => self.right = Some(Box::new(TreeNode::new(value))),
                Some(node) => node.insert(value),
            }
        }
    }
}

/// Árbol Binario de Búsqueda
///
/// Wrapper que mantiene la raíz del árbol y delega operaciones a los nodos.
struct BinarySearchTree {
    root: Option<Box<TreeNode>>,
}

impl BinarySearchTree {
    fn new() -> Self {
        BinarySearchTree { root: None }
    }

    fn from_root(root: TreeNode) -> Self {
        BinarySearchTree {
            root: Some(Box::new(root)),
        }
    }

    /// Busca un valor en el árbol
    ///
    /// # Parámetros
    /// * `target` - El valor a buscar
    ///
    /// # Devuelve
    /// * `Some(&TreeNode)` si se encuentra
    /// * `None` si no existe
    fn search(&self, target: i32) -> Option<&TreeNode> {
        self.root.as_ref().and_then(|node| node.search(target))
    }

    /// Inserta un valor en el árbol
    ///
    /// Si el árbol está vacío, crea la raíz.
    /// Si el valor ya existe, no hace nada.
    fn insert(&mut self, value: i32) {
        match &mut self.root {
            None => self.root = Some(Box::new(TreeNode::new(value))),
            Some(node) => node.insert(value),
        }
    }
}

fn main() {
    // Construimos el árbol insertando datos en orden aleatorio:
    //         50
    //       /    \
    //     25      75
    //    /  \    /  \
    //  10   30  60   80

    let mut tree = BinarySearchTree::new();
    tree.insert(50);
    tree.insert(25);
    tree.insert(75);
    tree.insert(10);
    tree.insert(30);
    tree.insert(60);
    tree.insert(80);

    println!("Árbol balanceado (inserción aleatoria):");
    for &v in &[50, 25, 75, 10, 30, 60, 80, 99] {
        match tree.search(v) {
            Some(nodo) => println!("  ✓ {} encontrado", nodo.value),
            None => println!("  ✗ {} no encontrado", v),
        }
    }

    // Ejemplo del texto: insertar 45 en el árbol
    // 50 -> 25 -> 33 -> 40 -> (45 insertado como right child de 40)
    println!();

    let mut arbol_ejemplo = BinarySearchTree::new();
    for &v in &[50, 25, 75, 33, 40, 45] {
        arbol_ejemplo.insert(v);
    }

    println!("Insertar 45 en árbol de ejemplo:");
    arbol_ejemplo.insert(45);
    match arbol_ejemplo.search(45) {
        Some(nodo) => println!("  ✓ 45 insertado y encontrado (valor: {})", nodo.value),
        None => println!("  ✗ 45 no encontrado"),
    }

    // Demostración de árbol degenerado (datos ordenados)
    println!();

    let mut arbol_degenerado = BinarySearchTree::new();
    for &v in &[1, 2, 3, 4, 5] {
        arbol_degenerado.insert(v);
    }
    println!("Árbol degenerado (inserción ordenada 1..5):");
    for &v in &[1, 3, 5] {
        match arbol_degenerado.search(v) {
            Some(nodo) => println!("  ✓ {} encontrado", nodo.value),
            None => println!("  ✗ {} no encontrado", v),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_test_tree() -> BinarySearchTree {
        let mut tree = BinarySearchTree::new();
        for &v in &[50, 25, 75, 10, 30, 60, 80] {
            tree.insert(v);
        }
        tree
    }

    #[test]
    fn test_search_raiz() {
        let tree = build_test_tree();
        let result = tree.search(50);
        assert!(result.is_some());
        assert_eq!(result.unwrap().value, 50);
    }

    #[test]
    fn test_search_nodo_interno() {
        let tree = build_test_tree();
        assert!(tree.search(25).is_some());
        assert_eq!(tree.search(25).unwrap().value, 25);
        assert!(tree.search(75).is_some());
        assert_eq!(tree.search(75).unwrap().value, 75);
    }

    #[test]
    fn test_search_hoja() {
        let tree = build_test_tree();
        assert!(tree.search(10).is_some());
        assert_eq!(tree.search(10).unwrap().value, 10);
        assert!(tree.search(30).is_some());
        assert!(tree.search(60).is_some());
        assert!(tree.search(80).is_some());
    }

    #[test]
    fn test_search_no_encontrado() {
        let tree = build_test_tree();
        assert!(tree.search(99).is_none());
        assert!(tree.search(-5).is_none());
    }

    #[test]
    fn test_search_arbol_vacio() {
        let tree: BinarySearchTree = BinarySearchTree::new();
        assert!(tree.search(42).is_none());
    }

    #[test]
    fn test_insert_y_search() {
        let mut tree = BinarySearchTree::new();
        tree.insert(10);
        tree.insert(5);
        tree.insert(15);

        assert!(tree.search(10).is_some());
        assert!(tree.search(5).is_some());
        assert!(tree.search(15).is_some());
        assert!(tree.search(20).is_none());
    }

    #[test]
    fn test_insert_duplicado_no_sobrescribe() {
        let mut tree = BinarySearchTree::new();
        tree.insert(10);
        tree.insert(5);
        tree.insert(10);

        assert!(tree.search(5).is_some());
        assert!(tree.search(10).is_some());
    }

    #[test]
    fn test_insert_arbol_vacio() {
        let mut tree = BinarySearchTree::new();
        tree.insert(42);
        assert!(tree.search(42).is_some());
    }

    #[test]
    fn test_arbol_degenerado_insercion_ordenada() {
        let mut tree = BinarySearchTree::new();
        for &v in &[1, 2, 3, 4, 5] {
            tree.insert(v);
        }
        assert!(tree.search(1).is_some());
        assert!(tree.search(5).is_some());
        assert_eq!(tree.root.as_ref().unwrap().value, 1);
    }
}
