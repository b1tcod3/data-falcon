//! Grafo (Red Social) en Rust
//!
//! Este módulo contiene la implementación de un grafo no dirigido usando
//! listas de adyacencia. Cada persona (nodo) mantiene una lista de amigos
//! (aristas). Usa `Rc<RefCell<Person>>` para permitir referencias compartidas
//! y mutables entre nodos.
//!
//! ## Funcionamiento
//! Los nodos se representan con `Person` y las aristas como una lista de
//! amigos. `Rc` permite que varios nodos compartan el ownership de un amigo.
//! `RefCell` permite mutar un nodo incluso cuando hay múltiples referencias.

use std::cell::RefCell;
use std::rc::Rc;

type PersonPtr = Rc<RefCell<Person>>;

/// Persona en la red social
///
/// Cada persona tiene un nombre y una lista de amigos (referencias a otras
/// personas). Las amistades son bidireccionales: si A es amigo de B,
/// B debería tener a A en su lista.
struct Person {
    name: String,
    friends: Vec<PersonPtr>,
}

impl Person {
    fn new(name: &str) -> PersonPtr {
        Rc::new(RefCell::new(Person {
            name: name.to_string(),
            friends: Vec::new(),
        }))
    }

    /// Agrega una amistad a esta persona
    ///
    /// # Parámetros
    /// * `friend` - Referencia a la persona que será agregada como amiga
    ///
    /// # Complejidad
    /// O(1) — solo agrega al final del vector
    fn add_friend(&mut self, friend: PersonPtr) {
        self.friends.push(friend);
    }

    /// Elimina una amistad por nombre
    ///
    /// # Parámetros
    /// * `name` - El nombre de la persona a eliminar de la lista de amigos
    ///
    /// # Complejidad
    /// O(n) — requiere buscar en el vector
    fn remove_friend(&mut self, name: &str) {
        self.friends.retain(|f| f.borrow().name != name);
    }

    /// Retorna el número de amigos
    fn friends_count(&self) -> usize {
        self.friends.len()
    }

    /// Verifica si una persona está en la lista de amigos
    fn has_friend(&self, name: &str) -> bool {
        self.friends.iter().any(|f| f.borrow().name == name)
    }

    /// Retorna los nombres de los amigos como Vec<String>
    fn friend_names(&self) -> Vec<String> {
        self.friends.iter().map(|f| f.borrow().name.clone()).collect()
    }
}

/// Imprime todas las conexiones de una lista de personas
///
/// # Parámetros
/// * `people` - Slice de referencias a personas
///
/// # Complejidad
/// O(V + E) donde V son personas y E son amistades
fn print_friendships(people: &[PersonPtr]) {
    for person in people {
        let p = person.borrow();
        let friends = p.friend_names();
        if friends.is_empty() {
            println!("{}: (sin amigos)", p.name);
        } else {
            println!("{} -> [{}]", p.name, friends.join(", "));
        }
    }
}

fn main() {
    let ana = Person::new("Ana");
    let carlos = Person::new("Carlos");
    let beatriz = Person::new("Beatriz");

    ana.borrow_mut().add_friend(carlos.clone());
    carlos.borrow_mut().add_friend(ana.clone());

    ana.borrow_mut().add_friend(beatriz.clone());
    beatriz.borrow_mut().add_friend(ana.clone());

    carlos.borrow_mut().add_friend(beatriz.clone());
    beatriz.borrow_mut().add_friend(carlos.clone());

    println!("--- Red Social ---");
    print_friendships(&[ana.clone(), carlos.clone(), beatriz.clone()]);

    println!();
    println!("¿Ana conoce a Carlos? {}", ana.borrow().has_friend("Carlos"));
    println!("Ana tiene {} amigo(s)", ana.borrow().friends_count());

    println!();
    println!("Ana deja de ser amiga de Carlos...");
    ana.borrow_mut().remove_friend("Carlos");
    carlos.borrow_mut().remove_friend("Ana");

    println!("--- Después del cambio ---");
    print_friendships(&[ana.clone(), carlos.clone(), beatriz.clone()]);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_test_network() -> Vec<PersonPtr> {
        let a = Person::new("Alice");
        let b = Person::new("Bob");
        let c = Person::new("Charlie");

        a.borrow_mut().add_friend(b.clone());
        b.borrow_mut().add_friend(a.clone());

        b.borrow_mut().add_friend(c.clone());
        c.borrow_mut().add_friend(b.clone());

        vec![a, b, c]
    }

    #[test]
    fn test_add_friend() {
        let alice = Person::new("Alice");
        let bob = Person::new("Bob");

        alice.borrow_mut().add_friend(bob.clone());
        assert!(alice.borrow().has_friend("Bob"));
    }

    #[test]
    fn test_remove_friend() {
        let alice = Person::new("Alice");
        let bob = Person::new("Bob");

        alice.borrow_mut().add_friend(bob.clone());
        assert!(alice.borrow().has_friend("Bob"));

        alice.borrow_mut().remove_friend("Bob");
        assert!(!alice.borrow().has_friend("Bob"));
    }

    #[test]
    fn test_friends_count() {
        let people = build_test_network();
        assert_eq!(people[0].borrow().friends_count(), 1); // Alice -> Bob
        assert_eq!(people[1].borrow().friends_count(), 2); // Bob -> Alice, Charlie
    }

    #[test]
    fn test_has_friend() {
        let people = build_test_network();
        assert!(people[0].borrow().has_friend("Bob"));
        assert!(!people[0].borrow().has_friend("Charlie"));
    }

    #[test]
    fn test_friend_names() {
        let people = build_test_network();
        let bob_friends = people[1].borrow().friend_names();
        assert!(bob_friends.contains(&"Alice".to_string()));
        assert!(bob_friends.contains(&"Charlie".to_string()));
    }

    #[test]
    fn test_sin_amigos() {
        let solo = Person::new("Solo");
        assert_eq!(solo.borrow().friends_count(), 0);
        assert!(!solo.borrow().has_friend("nadie"));
    }

    #[test]
    fn test_print_friendships() {
        let people = build_test_network();
        print_friendships(&people);
        // no debe panic
    }
}
