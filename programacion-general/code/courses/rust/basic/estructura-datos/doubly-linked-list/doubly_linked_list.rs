//! Lista Doblemente Enlazada en Rust (Doubly Linked List)
//!
//! Este módulo contiene la implementación de una lista doblemente enlazada
//! utilizando `Rc<RefCell<Node>>` para permitir múltiples referencias mutables.
//! Cada nodo mantiene un enlace al siguiente y al anterior, permitiendo
//! operaciones O(1) tanto al inicio como al final.
//!
//! ## Funcionamiento
//! Usa `Rc` (Reference Counting) para compartir propiedad entre nodos y
//! `RefCell` para mutabilidad interior en tiempo de ejecución.

use std::cell::RefCell;
use std::rc::Rc;

type NodePtr = Rc<RefCell<Node>>;

struct Node {
    data: String,
    next: Option<NodePtr>,
    previous: Option<NodePtr>,
}

impl Node {
    fn new(data: &str) -> NodePtr {
        Rc::new(RefCell::new(Node {
            data: data.to_string(),
            next: None,
            previous: None,
        }))
    }
}

struct DoublyLinkedList {
    first_node: Option<NodePtr>,
    last_node: Option<NodePtr>,
}

impl DoublyLinkedList {
    fn new() -> Self {
        DoublyLinkedList {
            first_node: None,
            last_node: None,
        }
    }

    fn insert_at_end(&mut self, value: &str) {
        let new_node = Node::new(value);

        match self.last_node.take() {
            Some(old_last) => {
                new_node.borrow_mut().previous = Some(old_last.clone());
                old_last.borrow_mut().next = Some(new_node.clone());
                self.last_node = Some(new_node);
            }
            None => {
                self.first_node = Some(new_node.clone());
                self.last_node = Some(new_node);
            }
        }
    }

    fn remove_from_front(&mut self) -> Option<String> {
        let old_first = self.first_node.take();

        if let Some(node) = old_first {
            let data_to_return = node.borrow().data.clone();
            self.first_node = node.borrow_mut().next.take();

            match &self.first_node {
                Some(new_first) => {
                    new_first.borrow_mut().previous = None;
                }
                None => {
                    self.last_node = None;
                }
            }
            return Some(data_to_return);
        }
        None
    }
}

struct Queue {
    queue: DoublyLinkedList,
}

impl Queue {
    fn new() -> Self {
        Queue {
            queue: DoublyLinkedList::new(),
        }
    }

    fn enque(&mut self, value: &str) {
        self.queue.insert_at_end(value);
    }

    fn deque(&mut self) -> Option<String> {
        self.queue.remove_from_front()
    }
}

fn main() {
    let mut fila_supermercado = Queue::new();

    fila_supermercado.enque("Ana");
    fila_supermercado.enque("Carlos");
    fila_supermercado.enque("Beatriz");

    if let Some(atendido) = fila_supermercado.deque() {
        println!("Se atendió a: {}", atendido);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_queue_fifo_order() {
        let mut q = Queue::new();
        q.enque("a");
        q.enque("b");
        q.enque("c");

        assert_eq!(q.deque(), Some("a".to_string()));
        assert_eq!(q.deque(), Some("b".to_string()));
        assert_eq!(q.deque(), Some("c".to_string()));
        assert_eq!(q.deque(), None);
    }

    #[test]
    fn test_queue_vacia() {
        let mut q: Queue = Queue::new();
        assert_eq!(q.deque(), None);
    }

    #[test]
    fn test_un_elemento() {
        let mut q = Queue::new();
        q.enque("unico");
        assert_eq!(q.deque(), Some("unico".to_string()));
        assert_eq!(q.deque(), None);
    }

    #[test]
    fn test_doubly_linked_list_insert_at_end() {
        let mut list = DoublyLinkedList::new();
        list.insert_at_end("a");
        list.insert_at_end("b");
        list.insert_at_end("c");

        assert_eq!(list.remove_from_front(), Some("a".to_string()));
        assert_eq!(list.remove_from_front(), Some("b".to_string()));
        assert_eq!(list.remove_from_front(), Some("c".to_string()));
        assert_eq!(list.remove_from_front(), None);
    }

    #[test]
    fn test_doubly_linked_list_vacia() {
        let mut list: DoublyLinkedList = DoublyLinkedList::new();
        assert_eq!(list.remove_from_front(), None);
    }
}
