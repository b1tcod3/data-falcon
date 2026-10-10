# Grafos

Un **grafo** es un conjunto de **nodos** (vértices) conectados por **aristas** (edges). Se usa para modelar redes: relaciones sociales, ciudades y rutas, redes de computadoras, dependencias, etc.

## 1. Grafo no ponderado: redes sociales

Cada persona es un nodo y sus amigos son las aristas. La **lista de adyacencia** es el `map[string][]*Person` (en Rust era `Rc<RefCell<Person>>`):

```go
type Person struct {
	name    string
	friends []*Person
}
```

Código: [`grafo/social-graph/main.go`](../../code/estructura-datos/grafo/social-graph/main.go) y sus [pruebas](../../code/estructura-datos/grafo/social-graph/social_graph_test.go).

## 2. Búsqueda en Amplitud (BFS)

BFS explora el grafo **por niveles**: primero los vecinos directos, luego los vecinos de los vecinos, etc. Usa una **cola** para garantizar ese orden de visita:

```go
func (g *SocialGraph) BfsOrder(from string) []string {
	visitados := map[string]bool{}
	cola := []string{from}
	resultado := []string{}

	for len(cola) > 0 {
		persona := cola[0]
		cola = cola[1:]
		if visitados[persona] { continue }
		visitados[persona] = true
		resultado = append(resultado, persona)
		for _, amigo := range g.network[persona] {
			if !visitados[amigo] { cola = append(cola, amigo) }
		}
	}
	return resultado
}
```

En el grafo de ejemplo, el árbol de amistad es `Ana ↔ Carlos ↔ Beatriz ↔ David`, y el recorrido desde Ana es `Ana → Carlos → Beatriz → David`.

Código: [`grafo/bfs-graph/main.go`](../../code/estructura-datos/grafo/bfs-graph/main.go) y sus [pruebas](../../code/estructura-datos/grafo/bfs-graph/bfs_graph_test.go).

## 3. Dijkstra: camino más barato

Un **grafo ponderado** añade un costo a cada arista. Dijkstra encuentra la ruta de menor costo entre un origen y todas las ciudades: siempre expande el nodo más barato no visitado (una **cola de prioridad mínima**).

En Rust se usaba `BinaryHeap` invirtiendo el orden; en Go se usa el paquete estándar `container/heap`:

```go
type PriorityQueue []State
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].cost < pq[j].cost } // mínima
```

El grafo de ciudades (Atlanta, Boston, Chicago, Denver, El Paso) tiene estas rutas:

```
Atlanta ↔ Boston (100)   Atlanta ↔ Denver (160)
Boston  ↔ Chicago (120)  Boston  ↔ Denver (180)
Chicago ↔ El Paso (80)   Denver  ↔ Chicago (40)
Denver  ↔ El Paso (140)
```

La ruta más barata a El Paso es `Atlanta → Denver (160) → Chicago (40) → El Paso (80) = $280`, más barata que ir vía Boston.

Código: [`grafo/dijkstra/main.go`](../../code/estructura-datos/grafo/dijkstra/main.go) y sus [pruebas](../../code/estructura-datos/grafo/dijkstra/main_test.go).

```bash
go run ./grafo/dijkstra
# Costo más bajo desde Atlanta a El Paso: $ 280
```

## 4. map ordenado vs map simple

Go (como Rust con `HashMap`) no garantiza orden al iterar un `map`. Para obtener salida determinista como un `BTreeMap` (y soportar *range queries*, min/max), se combina el `map` con `sort.Strings`:

```go
func sortedKeys[V any](m map[string]V) []string {
	keys := make([]string, 0, len(m))
	for k := range m { keys = append(keys, k) }
	sort.Strings(keys)
	return keys
}
```

Esto replica las operaciones del `BTreeMap` de Rust: iteración alfabética, *range query* (`rangeQuery(grafo, "Atlanta", "Chicago")`) y min/max (primera/última clave).

Código: [`grafo/mapas-ordenados/main.go`](../../code/estructura-datos/grafo/mapas-ordenados/main.go) y sus [pruebas](../../code/estructura-datos/grafo/mapas-ordenados/mapas_ordenados_test.go).

| Estructura | Insert/Read | Orden de claves | Uso ideal |
| --- | --- | --- | --- |
| `map` | O(1) promed. | Sin orden | Búsquedas rápidas |
| `map` + `sort.Strings` | O(1) + O(n log n) al ordenar | Alfabético | Reportes, logs, rangos |

## Resumen

- **Lista de adyacencia** = manera práctica de representar grafos.
- **BFS** explora por niveles con una cola (O(V + E)).
- **Dijkstra** resuelve rutas de costo mínimo (O((V + E) log V)).
- Cuando el **orden de salida importa**, ordena las claves del map.