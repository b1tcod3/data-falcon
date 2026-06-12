//! Recorrido In-Order de un Árbol Binario de Búsqueda
//!
//! Este módulo demuestra el recorrido in-order (izquierda, nodo, derecha)
//! que imprime los elementos de un BST en orden ascendente.
//! Implementado con valores String para simular una biblioteca de libros.
//!
//! ## Funcionamiento
//! El recorrido in-order visita primero el subárbol izquierdo, luego el nodo
//! actual, y finalmente el subárbol derecho, produciendo elementos ordenados.

/// Nodo del árbol con valor String
///
/// # Complejidad del recorrido
/// O(N) — visita cada nodo exactamente una vez
#[derive(Debug)]
struct TreeNode {
    value: String,
    left: Option<Box<TreeNode>>,
    right: Option<Box<TreeNode>>,
}

/// Recorre el árbol en orden (in-order) e imprime cada valor
///
/// # Parámetros
/// * `node` - Referencia al nodo (o None) desde donde comenzar el recorrido
///
/// # Ejemplo
/// ```
/// let mut raiz = TreeNode { value: "Moby Dick".to_string(), left: None, right: None };
/// // ... agregar hijos ...
/// traverse_and_print(&Some(Box::new(raiz)));
/// ```
///
/// # Complejidad
/// O(N) — visita cada nodo exactamente una vez
fn traverse_and_print(node: &Option<Box<TreeNode>>) {
    if let Some(n) = node {
        traverse_and_print(&n.left);
        println!("{}", n.value);
        traverse_and_print(&n.right);
    }
}

fn main() {
    let mut root = TreeNode {
        value: "Moby Dick".to_string(),
        left: None,
        right: None,
    };
    let left_child = TreeNode {
        value: "Alice in Wonderland".to_string(),
        left: None,
        right: None,
    };
    let right_child = TreeNode {
        value: "Robinson Crusoe".to_string(),
        left: None,
        right: None,
    };

    root.left = Some(Box::new(left_child));
    root.right = Some(Box::new(right_child));

    let tree = Some(Box::new(root));

    println!("--- Mi Biblioteca Ordenada ---");
    traverse_and_print(&tree);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_book_tree() -> Option<Box<TreeNode>> {
        let mut root = TreeNode {
            value: "Moby Dick".to_string(),
            left: None,
            right: None,
        };
        let left_child = TreeNode {
            value: "Alice in Wonderland".to_string(),
            left: None,
            right: None,
        };
        let right_child = TreeNode {
            value: "Robinson Crusoe".to_string(),
            left: None,
            right: None,
        };

        root.left = Some(Box::new(left_child));
        root.right = Some(Box::new(right_child));

        Some(Box::new(root))
    }

    #[test]
    fn test_traverse_in_order() {
        let tree = build_book_tree();
        // in-order: Alice -> Moby Dick -> Robinson Crusoe
        traverse_and_print(&tree);
        // si no panic, ok
    }

    #[test]
    fn test_arbol_vacio() {
        let tree: Option<Box<TreeNode>> = None;
        traverse_and_print(&tree);
        // no debe panic
    }

    #[test]
    fn test_un_solo_libro() {
        let tree = Some(Box::new(TreeNode {
            value: "Don Quijote".to_string(),
            left: None,
            right: None,
        }));
        traverse_and_print(&tree);
    }

    #[test]
    fn test_estructura_nodos() {
        let tree = build_book_tree();
        if let Some(ref node) = tree {
            assert_eq!(node.value, "Moby Dick");
            assert!(node.left.is_some());
            assert!(node.right.is_some());
            assert_eq!(node.left.as_ref().unwrap().value, "Alice in Wonderland");
            assert_eq!(node.right.as_ref().unwrap().value, "Robinson Crusoe");
        }
    }
}
