#![allow(dead_code)]

//! Lista Enlazada Simple en Rust (Singly Linked List)
//!
//! Este módulo contiene la implementación de una lista enlazada simple,
//! donde cada nodo apunta al siguiente. Es una estructura de datos lineal
//! y dinámica que permite inserción y eliminación eficiente al inicio.
//!
//! ## Funcionamiento
//! Los datos se almacenan en nodos, donde cada nodo contiene un valor
//! y una referencia al siguiente nodo. La lista mantiene una referencia
//! al primer nodo (cabeza).

use std::fmt; // Para formatear la salida de la lista

/// Nodo individual de la lista enlazada
///
/// Cada nodo contiene un dato (`data`) y un puntero al siguiente nodo
/// (`next`). El último nodo de la lista tiene `next = None`.
#[derive(Debug)]
struct Node {
    data: String,
    next: Option<Box<Node>>,
}

impl Node {
    /// Crea un nuevo nodo con el dato proporcionado
    fn new(data: &str) -> Self {
        Node {
            data: data.to_string(),
            next: None,
        }
    }
}

/// Lista Enlazada Simple
///
/// Mantiene una referencia al primer nodo (`first_node`). Las operaciones
/// al inicio (push_front, pop_front) son O(1), mientras que las operaciones
/// al final requieren recorrer la lista (O(n)).
///
/// # Ejemplos
/// ```
/// let mut list = LinkedList::new();
/// list.push_front("mundo");
/// list.push_front("hola");
/// assert_eq!(list.to_vec(), vec!["hola", "mundo"]);
/// ```
///
/// # Complejidad
/// * **push_front**: O(1)
/// * **pop_front**: O(1)
/// * **push_back**: O(n)
/// * **to_vec**: O(n)
#[derive(Debug)]
struct LinkedList {
    first_node: Option<Box<Node>>,
}

impl LinkedList {
    /// Crea una nueva lista enlazada vacía
    fn new() -> Self {
        LinkedList { first_node: None }
    }

    /// Agrega un elemento al inicio de la lista
    ///
    /// # Parámetros
    /// * `data` - El valor a agregar
    ///
    /// # Complejidad
    /// O(1) - solo se actualiza la referencia al primer nodo
    fn push_front(&mut self, data: &str) {
        let mut new_node = Box::new(Node::new(data));
        new_node.next = self.first_node.take();
        self.first_node = Some(new_node);
    }

    /// Agrega un elemento al final de la lista
    ///
    /// # Parámetros
    /// * `data` - El valor a agregar
    ///
    /// # Complejidad
    /// O(n) - requiere recorrer toda la lista hasta el último nodo
    fn push_back(&mut self, data: &str) {
        let new_node = Box::new(Node::new(data));

        let mut current = &mut self.first_node;
        while let Some(node) = current {
            current = &mut node.next;
        }
        *current = Some(new_node);
    }

    /// Elimina y retorna el primer elemento de la lista
    ///
    /// # Devuelve
    /// * `Some(String)` - el dato del primer nodo
    /// * `None` - si la lista está vacía
    ///
    /// # Complejidad
    /// O(1) - solo se actualiza la referencia al primer nodo
    fn pop_front(&mut self) -> Option<String> {
        self.first_node.take().map(|node| {
            self.first_node = node.next;
            node.data
        })
    }

    /// Obtiene el primer elemento sin eliminarlo
    fn peek_front(&self) -> Option<&str> {
        self.first_node.as_ref().map(|node| node.data.as_str())
    }

    /// Obtiene el elemento en el índice especificado sin eliminarlo
    ///
    /// # Parámetros
    /// * `index` - El índice del elemento a obtener (0-based)
    ///
    /// # Devuelve
    /// * `Some(&str)` - el dato del nodo en la posición `index`
    /// * `None` - si el índice está fuera de los límites de la lista
    ///
    /// # Complejidad
    /// O(n) - requiere recorrer la lista hasta el índice solicitado
    fn read(&self, index: usize) -> Option<&str> {
        let mut current = &self.first_node;
        let mut current_index = 0;

        while current_index < index {
            current = &current.as_ref()?.next;
            current_index += 1;
        }

        current.as_ref().map(|node| node.data.as_str())
    }

    /// Busca un valor en la lista y retorna su índice
    ///
    /// # Parámetros
    /// * `value` - El valor a buscar
    ///
    /// # Devuelve
    /// * `Some(usize)` - el índice de la primera ocurrencia del valor
    /// * `None` - si el valor no se encuentra en la lista
    ///
    /// # Complejidad
    /// O(n) - requiere recorrer la lista hasta encontrar el valor
    fn index_of(&self, value: &str) -> Option<usize> {
        let mut current = &self.first_node;
        let mut current_index = 0;

        while let Some(node) = current {
            if node.data == value {
                return Some(current_index);
            }
            current = &node.next;
            current_index += 1;
        }

        None
    }

    /// Retorna una representación como Vec de todos los elementos
    ///
    /// # Complejidad
    /// O(n) - requiere recorrer toda la lista
    fn to_vec(&self) -> Vec<String> {
        let mut result = Vec::new();
        let mut current = &self.first_node;
        while let Some(node) = current {
            result.push(node.data.clone());
            current = &node.next;
        }
        result
    }

    /// Retorna el número de elementos en la lista
    ///
    /// # Complejidad
    /// O(n)
    fn len(&self) -> usize {
        let mut count = 0;
        let mut current = &self.first_node;
        while let Some(node) = current {
            count += 1;
            current = &node.next;
        }
        count
    }

    /// Verifica si la lista está vacía
    fn is_empty(&self) -> bool {
        self.first_node.is_none()
    }

    /// Imprime la lista en formato: `[elemento1 -> elemento2 -> ...]`
    fn display(&self) {
        let mut current = &self.first_node;
        print!("[");
        while let Some(node) = current {
            print!("{}", node.data);
            current = &node.next;
            if current.is_some() {
                print!(" -> ");
            }
        }
        println!("]");
    }
}

impl fmt::Display for LinkedList {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut current = &self.first_node;
        write!(f, "[")?;
        while let Some(node) = current {
            write!(f, "{}", node.data)?;
            current = &node.next;
            if current.is_some() {
                write!(f, " -> ")?;
            }
        }
        write!(f, "]")
    }
}

fn main() {
    // Construimos la lista "once upon a time" usando push_front.
    // Como push_front agrega al inicio, construimos en orden inverso:
    // "time" se agrega primero, luego "a" se pone antes, etc.
    let mut lista_historia = LinkedList::new();
    lista_historia.push_front("time");
    lista_historia.push_front("a");
    lista_historia.push_front("upon");
    lista_historia.push_front("once");

    println!("Lista enlazada:");
    println!("{:#?}", lista_historia);
    println!();
    println!("Display: {}", lista_historia);
    println!("Longitud: {}", lista_historia.len());
    println!();

    // Demostración de operaciones
    println!("Primer elemento (peek): {:?}", lista_historia.peek_front());
    println!("Pop front: {:?}", lista_historia.pop_front());
    println!("Después de pop: {}", lista_historia);

    // Ejemplo con push_back
    let mut otra_lista = LinkedList::new();
    otra_lista.push_back("esto");
    otra_lista.push_back("es");
    otra_lista.push_back("push_back");
    println!();
    println!("Lista con push_back:");
    otra_lista.display();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_lista_vacia() {
        let list: LinkedList = LinkedList::new();
        assert!(list.is_empty());
        assert_eq!(list.len(), 0);
        assert_eq!(list.peek_front(), None);
        assert_eq!(list.to_vec(), Vec::<String>::new());

        let mut list_mut: LinkedList = LinkedList::new();
        assert_eq!(list_mut.pop_front(), None);
    }

    #[test]
    fn test_push_front() {
        let mut list = LinkedList::new();
        list.push_front("mundo");
        list.push_front("hola");
        assert!(!list.is_empty());
        assert_eq!(list.len(), 2);
        assert_eq!(list.to_vec(), vec!["hola", "mundo"]);
    }

    #[test]
    fn test_push_back() {
        let mut list = LinkedList::new();
        list.push_back("a");
        list.push_back("b");
        list.push_back("c");
        assert_eq!(list.len(), 3);
        assert_eq!(list.to_vec(), vec!["a", "b", "c"]);
    }

    #[test]
    fn test_pop_front() {
        let mut list = LinkedList::new();
        list.push_front("x");
        list.push_front("y");
        list.push_front("z");

        assert_eq!(list.pop_front(), Some("z".to_string()));
        assert_eq!(list.pop_front(), Some("y".to_string()));
        assert_eq!(list.pop_front(), Some("x".to_string()));
        assert_eq!(list.pop_front(), None);
        assert!(list.is_empty());
    }

    #[test]
    fn test_peek_front() {
        let mut list = LinkedList::new();
        assert_eq!(list.peek_front(), None);

        list.push_front("primero");
        assert_eq!(list.peek_front(), Some("primero"));

        list.push_front("nuevo_primero");
        assert_eq!(list.peek_front(), Some("nuevo_primero"));
    }

    #[test]
    fn test_ejemplo_once_upon_a_time() {
        let mut list = LinkedList::new();
        list.push_front("time");
        list.push_front("a");
        list.push_front("upon");
        list.push_front("once");

        assert_eq!(list.to_vec(), vec!["once", "upon", "a", "time"]);
        assert_eq!(list.len(), 4);
    }

    #[test]
    fn test_push_front_y_push_back_combinados() {
        let mut list = LinkedList::new();
        list.push_back("medio");
        list.push_front("inicio");
        list.push_back("final");

        assert_eq!(list.to_vec(), vec!["inicio", "medio", "final"]);
    }

    #[test]
    fn test_index_of() {
        let mut list = LinkedList::new();
        list.push_back("once");
        list.push_back("upon");
        list.push_back("a");
        list.push_back("time");

        assert_eq!(list.index_of("once"), Some(0));
        assert_eq!(list.index_of("upon"), Some(1));
        assert_eq!(list.index_of("a"), Some(2));
        assert_eq!(list.index_of("time"), Some(3));
        assert_eq!(list.index_of("never"), None);
    }

    #[test]
    fn test_index_of_lista_vacia() {
        let list: LinkedList = LinkedList::new();
        assert_eq!(list.index_of("anything"), None);
    }

    #[test]
    fn test_un_solo_elemento() {
        let mut list = LinkedList::new();
        list.push_front("unico");
        assert_eq!(list.len(), 1);
        assert_eq!(list.peek_front(), Some("unico"));
        assert_eq!(list.pop_front(), Some("unico".to_string()));
        assert!(list.is_empty());
    }

    #[test]
    fn test_read() {
        let mut list = LinkedList::new();
        list.push_back("a");
        list.push_back("b");
        list.push_back("c");

        assert_eq!(list.read(0), Some("a"));
        assert_eq!(list.read(1), Some("b"));
        assert_eq!(list.read(2), Some("c"));
        assert_eq!(list.read(3), None);
        assert_eq!(list.read(99), None);
    }

    #[test]
    fn test_read_lista_vacia() {
        let list: LinkedList = LinkedList::new();
        assert_eq!(list.read(0), None);
    }

    #[test]
    fn test_display_y_fmt() {
        let mut list = LinkedList::new();
        list.push_back("a");
        list.push_back("b");
        assert_eq!(format!("{}", list), "[a -> b]");
    }
}
