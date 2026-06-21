//! Algoritmo de Dijkstra en Rust
//!
//! Este módulo implementa el algoritmo de Dijkstra para encontrar el camino
//! más corto desde un nodo origen a todos los demás en un grafo ponderado
//! con pesos no negativos.
//!
//! ## Funcionamiento
//! Usa una cola de prioridad (BinaryHeap) para siempre explorar la ruta más
//! barata disponible, actualizando distancias cuando encuentra caminos más
//! cortos. Complejidad: O((V + E) log V)

use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Clone, Eq, PartialEq)]
struct State {
    cost: u32,
    city: String,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

/// Encuentra el costo más barato desde `start` a cada ciudad
///
/// # Parámetros
/// * `graph` - Mapa de ciudad a lista de (vecino, costo)
/// * `start` - Ciudad de origen
///
/// # Devuelve
/// * `HashMap<String, u32>` - costo mínimo a cada ciudad alcanzable
///
/// # Complejidad
/// O((V + E) log V)
///
/// # Ejemplo
/// ```
/// let mut map = HashMap::new();
/// map.insert("A".to_string(), vec![("B".to_string(), 10)]);
/// map.insert("B".to_string(), vec![]);
/// let dist = dijkstra(&map, "A");
/// assert_eq!(dist.get("A"), Some(&0));
/// assert_eq!(dist.get("B"), Some(&10));
/// ```
fn dijkstra(
    graph: &HashMap<String, Vec<(String, u32)>>,
    start: &str,
) -> HashMap<String, u32> {
    let mut distances = HashMap::new();
    let mut heap = BinaryHeap::new();

    distances.insert(start.to_string(), 0);
    heap.push(State {
        cost: 0,
        city: start.to_string(),
    });

    while let Some(State { cost, city }) = heap.pop() {
        if cost > *distances.get(&city).unwrap_or(&u32::MAX) {
            continue;
        }

        if let Some(routes) = graph.get(&city) {
            for (next_city, price) in routes {
                let next_cost = cost + price;
                let current_known_cost = *distances.get(next_city).unwrap_or(&u32::MAX);

                if next_cost < current_known_cost {
                    distances.insert(next_city.clone(), next_cost);
                    heap.push(State {
                        cost: next_cost,
                        city: next_city.clone(),
                    });
                }
            }
        }
    }

    distances
}

fn main() {
    let mut map = HashMap::new();
    map.insert(
        "Atlanta".to_string(),
        vec![("Boston".to_string(), 100), ("Denver".to_string(), 160)],
    );
    map.insert(
        "Boston".to_string(),
        vec![
            ("Chicago".to_string(), 120),
            ("Denver".to_string(), 180),
        ],
    );
    map.insert(
        "Chicago".to_string(),
        vec![("El Paso".to_string(), 80)],
    );
    map.insert(
        "Denver".to_string(),
        vec![
            ("Chicago".to_string(), 40),
            ("El Paso".to_string(), 140),
        ],
    );
    map.insert("El Paso".to_string(), vec![]);

    let cheapest_routes = dijkstra(&map, "Atlanta");

    println!("Costo más bajo desde Atlanta a El Paso: ${}", cheapest_routes["El Paso"]);
    println!("Costo más bajo desde Atlanta a Boston: ${}", cheapest_routes["Boston"]);
    println!("Costo más bajo desde Atlanta a Denver: ${}", cheapest_routes["Denver"]);
    println!("Costo más bajo desde Atlanta a Chicago: ${}", cheapest_routes["Chicago"]);

    // Ruta esperada: Atlanta -> Denver (160) -> Chicago (40) -> El Paso (80) = 280
    assert_eq!(cheapest_routes["El Paso"], 280);
}

#[cfg(test)]
mod tests {
    use super::*;

    fn build_city_graph() -> HashMap<String, Vec<(String, u32)>> {
        let mut map = HashMap::new();
        map.insert("Atlanta".to_string(), vec![
            ("Boston".to_string(), 100),
            ("Denver".to_string(), 160),
        ]);
        map.insert("Boston".to_string(), vec![
            ("Chicago".to_string(), 120),
            ("Denver".to_string(), 180),
        ]);
        map.insert("Chicago".to_string(), vec![
            ("El Paso".to_string(), 80),
        ]);
        map.insert("Denver".to_string(), vec![
            ("Chicago".to_string(), 40),
            ("El Paso".to_string(), 140),
        ]);
        map.insert("El Paso".to_string(), vec![]);
        map
    }

    #[test]
    fn test_ruta_mas_barata_el_paso() {
        let map = build_city_graph();
        let dist = dijkstra(&map, "Atlanta");
        assert_eq!(dist.get("El Paso"), Some(&280));
    }

    #[test]
    fn test_origen_mismo() {
        let map = build_city_graph();
        let dist = dijkstra(&map, "Atlanta");
        assert_eq!(dist.get("Atlanta"), Some(&0));
    }

    #[test]
    fn test_conexion_directa() {
        let map = build_city_graph();
        let dist = dijkstra(&map, "Atlanta");
        assert_eq!(dist.get("Boston"), Some(&100));
        assert_eq!(dist.get("Denver"), Some(&160));
    }

    #[test]
    fn test_ruta_indirecta_mas_barata() {
        // Denver -> Chicago (40) es más barato que Boston -> Chicago (120)
        let map = build_city_graph();
        let dist = dijkstra(&map, "Atlanta");
        // Atlanta -> Denver (160) -> Chicago (40) = 200
        // vs Atlanta -> Boston (100) -> Chicago (120) = 220
        assert_eq!(dist.get("Chicago"), Some(&200));
    }

    #[test]
    fn test_ciudad_aislada() {
        let mut map = build_city_graph();
        map.insert("Solitaria".to_string(), vec![]);
        let dist = dijkstra(&map, "Atlanta");
        assert!(!dist.contains_key("Solitaria"));
    }

    #[test]
    fn test_grafo_vacio() {
        let map: HashMap<String, Vec<(String, u32)>> = HashMap::new();
        let dist = dijkstra(&map, "Origen");
        assert!(dist.is_empty() || dist.contains_key("Origen"));
    }

    #[test]
    fn test_dos_caminos_mismo_destino() {
        let mut map = HashMap::new();
        map.insert("A".to_string(), vec![
            ("B".to_string(), 5),
            ("C".to_string(), 10),
        ]);
        map.insert("B".to_string(), vec![("C".to_string(), 3)]);
        map.insert("C".to_string(), vec![]);

        let dist = dijkstra(&map, "A");
        // A -> B (5) -> C (3) = 8 vs A -> C (10) = 10
        assert_eq!(dist.get("C"), Some(&8));
    }
}
