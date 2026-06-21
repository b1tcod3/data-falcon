#![allow(dead_code)]

//! Búsqueda en Anchura (BFS) en un Grafo Social
//!
//! Este módulo implementa un grafo usando listas de adyacencia con
//! `HashMap<String, Vec<String>>` y el algoritmo BFS (Breadth-First Search)
//! para recorrer la red.
//!
//! ## Funcionamiento
//! BFS usa una cola FIFO para explorar el grafo por niveles: primero visita
//! al nodo inicial, luego a todos sus vecinos directos, luego a los vecinos
//! de los vecinos, etc.

use std::collections::{HashMap, HashSet, VecDeque};

/// Grafo Social usando listas de adyacencia
///
/// Cada persona (clave) tiene una lista de nombres de amigos (valores).
/// Las amistades son bidireccionales.
struct SocialGraph {
    network: HashMap<String, Vec<String>>,
}

impl SocialGraph {
    fn new() -> Self {
        SocialGraph {
            network: HashMap::new(),
        }
    }

    /// Agrega una persona al grafo
    fn add_person(&mut self, name: &str) {
        self.network.entry(name.to_string()).or_insert(Vec::new());
    }

    /// Agrega una amistad bidireccional entre dos personas
    ///
    /// # Parámetros
    /// * `a` - Nombre de la primera persona
    /// * `b` - Nombre de la segunda persona
    ///
    /// # Complejidad
    /// O(1)
    fn add_friendship(&mut self, a: &str, b: &str) {
        self.network.entry(a.to_string()).or_insert(Vec::new()).push(b.to_string());
        self.network.entry(b.to_string()).or_insert(Vec::new()).push(a.to_string());
    }

    /// Recorre el grafo desde `start_person` usando BFS
    ///
    /// Imprime cada persona visitada en el orden del recorrido por niveles.
    ///
    /// # Parámetros
    /// * `start_person` - La persona desde donde comenzar el recorrido
    ///
    /// # Complejidad
    /// O(V + E) donde V son vértices y E aristas
    ///
    /// # Ejemplo
    /// ```
    /// let mut graph = SocialGraph::new();
    /// graph.add_friendship("Ana", "Carlos");
    /// graph.add_friendship("Ana", "Beatriz");
    /// graph.display_network_bfs("Ana");
    /// ```
    fn display_network_bfs(&self, start_person: &str) {
        let mut queue: VecDeque<&str> = VecDeque::new();
        let mut visited: HashSet<&str> = HashSet::new();

        queue.push_back(start_person);
        visited.insert(start_person);

        while let Some(current_person) = queue.pop_front() {
            println!("Visitando: {}", current_person);

            if let Some(friends) = self.network.get(current_person) {
                for friend in friends {
                    if !visited.contains(friend.as_str()) {
                        visited.insert(friend.as_str());
                        queue.push_back(friend.as_str());
                    }
                }
            }
        }
    }

    /// Retorna el orden de visita BFS como Vec<String>
    fn bfs_order(&self, start_person: &str) -> Vec<String> {
        let mut queue: VecDeque<&str> = VecDeque::new();
        let mut visited: HashSet<&str> = HashSet::new();
        let mut order: Vec<String> = Vec::new();

        if !self.network.contains_key(start_person) {
            return order;
        }

        queue.push_back(start_person);
        visited.insert(start_person);

        while let Some(current_person) = queue.pop_front() {
            order.push(current_person.to_string());

            if let Some(friends) = self.network.get(current_person) {
                for friend in friends {
                    if !visited.contains(friend.as_str()) {
                        visited.insert(friend.as_str());
                        queue.push_back(friend.as_str());
                    }
                }
            }
        }

        order
    }

    /// Verifica si existe una persona en el grafo
    fn has_person(&self, name: &str) -> bool {
        self.network.contains_key(name)
    }
}

fn main() {
    let mut graph = SocialGraph::new();

    graph.add_friendship("Ana", "Carlos");
    graph.add_friendship("Ana", "Beatriz");
    graph.add_friendship("Carlos", "Beatriz");
    graph.add_friendship("Beatriz", "David");

    println!("--- BFS desde Ana ---");
    graph.display_network_bfs("Ana");

    println!();
    println!("--- BFS desde David ---");
    graph.display_network_bfs("David");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_test_graph() -> SocialGraph {
        let mut graph = SocialGraph::new();
        graph.add_friendship("Ana", "Carlos");
        graph.add_friendship("Ana", "Beatriz");
        graph.add_friendship("Carlos", "Beatriz");
        graph.add_friendship("Beatriz", "David");
        graph.add_person("Elena");
        graph
    }

    #[test]
    fn test_bfs_visita_todos_alcanzables() {
        let graph = build_test_graph();
        let order = graph.bfs_order("Ana");
        assert!(order.contains(&"Ana".to_string()));
        assert!(order.contains(&"Carlos".to_string()));
        assert!(order.contains(&"Beatriz".to_string()));
        assert!(order.contains(&"David".to_string()));
        assert_eq!(order.len(), 4);
    }

    #[test]
    fn test_bfs_empieza_con_start() {
        let graph = build_test_graph();
        let order = graph.bfs_order("Ana");
        assert_eq!(order[0], "Ana");
    }

    #[test]
    fn test_bfs_persona_aislada() {
        let graph = build_test_graph();
        let order = graph.bfs_order("Elena");
        assert_eq!(order, vec!["Elena"]);
    }

    #[test]
    fn test_bfs_persona_inexistente() {
        let graph: SocialGraph = SocialGraph::new();
        let order = graph.bfs_order("Inexistente");
        assert!(order.is_empty());
    }

    #[test]
    fn test_bfs_grafo_vacio() {
        let graph: SocialGraph = SocialGraph::new();
        let order = graph.bfs_order("Alguien");
        assert!(order.is_empty());
    }

    #[test]
    fn test_add_person() {
        let mut graph = SocialGraph::new();
        graph.add_person("Solo");
        assert!(graph.has_person("Solo"));
        assert_eq!(graph.bfs_order("Solo"), vec!["Solo"]);
    }

    #[test]
    fn test_amistad_bidireccional() {
        let mut graph = SocialGraph::new();
        graph.add_friendship("A", "B");
        assert!(graph.network["A"].contains(&"B".to_string()));
        assert!(graph.network["B"].contains(&"A".to_string()));
    }
}
