// HashMap vs BTreeMap en Go.
//
// Este programa recrea la comparación que en Rust se hacía entre HashMap y
// BTreeMap en el algoritmo de Dijkstra. Go no tiene un BTreeMap en su
// biblioteca estándar: el equivalente es un map combinado con sort.Strings
// sobre las claves cuando el orden es importante.
//
//   - map:         O(1) promedio insert/búsqueda, sin orden de claves.
//   - map + sort:  itera claves en orden alfabético (O(n log n)).
//
// Ejecutar con:
//
//	go run ./grafo/mapas-ordenados
package main

import (
	"fmt"
	"math"
	"slices"
	"sort"
)

// Edge es una arista ponderada del grafo.
type Edge struct {
	to   string
	cost uint32
}

// DijkstraResult agrupa predecesores y costos para reconstruir rutas.
type DijkstraResult struct {
	predecessors map[string]string
	cost         map[string]uint32
}

const infinity = math.MaxUint32

// sortedKeys devuelve las claves de un map en orden alfabético,
// replicando la iteración ordenada de un BTreeMap.
func sortedKeys[V any](m map[string]V) []string {
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	return keys
}

// dijkstraBTree replica el comportamiento de Dijkstra con BTreeMap:
// la selección del siguiente nodo es determinista (empates se resuelven
// a favor del nombre alfabéticamente menor).
func dijkstraBTree(graph map[string][]Edge, start string) DijkstraResult {
	cost := map[string]uint32{}
	predecessors := map[string]string{}
	visited := map[string]bool{}

	for city := range graph {
		cost[city] = infinity
		predecessors[city] = ""
		visited[city] = false
	}
	cost[start] = 0

	for {
		// seleccionar la ciudad no visitada con menor costo, con empates
		// resueltos por orden alfabético (equivalente a min_by_key con BTreeMap)
		current := ""
		currentCost := uint32(infinity)
		for _, city := range sortedKeys(cost) {
			if !visited[city] && cost[city] < currentCost {
				current = city
				currentCost = cost[city]
			}
		}
		if current == "" {
			break
		}

		visited[current] = true

		for _, edge := range graph[current] {
			newCost := currentCost + edge.cost
			if newCost < cost[edge.to] {
				cost[edge.to] = newCost
				predecessors[edge.to] = current
			}
		}
	}

	return DijkstraResult{predecessors: predecessors, cost: cost}
}

// dijkstraHash replica el comportamiento de Dijkstra con HashMap:
// solo devuelve los costos, sin orden particular.
func dijkstraHash(graph map[string][]Edge, start string) map[string]uint32 {
	cost := map[string]uint32{}
	visited := map[string]bool{}

	for city := range graph {
		cost[city] = infinity
		visited[city] = false
	}
	cost[start] = 0

	for {
		current := ""
		currentCost := uint32(infinity)
		for city, c := range cost {
			if !visited[city] && c < currentCost {
				current = city
				currentCost = c
			}
		}
		if current == "" {
			break
		}

		visited[current] = true

		for _, edge := range graph[current] {
			newCost := currentCost + edge.cost
			if newCost < cost[edge.to] {
				cost[edge.to] = newCost
			}
		}
	}

	return cost
}

// findPath reconstruye la ruta desde el final usando los predecesores.
func findPath(predecessors map[string]string, start, end string) []string {
	path := []string{end}
	current := end
	for {
		prev, ok := predecessors[current]
		if !ok || prev == "" {
			break
		}
		path = append(path, prev)
		current = prev
	}
	slices.Reverse(path)
	return path
}

// rangeQuery replica graph.range(a..=b) de BTreeMap sobre claves ordenadas.
func rangeQuery[V any](m map[string]V, from, to string) []string {
	resultado := []string{}
	for _, k := range sortedKeys(m) {
		if k >= from && k <= to {
			resultado = append(resultado, k)
		}
	}
	return resultado
}

func construirGrafo() map[string][]Edge {
	grafo := map[string][]Edge{}
	grafo["Atlanta"] = []Edge{{to: "Boston", cost: 100}, {to: "Denver", cost: 160}}
	grafo["Boston"] = []Edge{{to: "Chicago", cost: 120}, {to: "Denver", cost: 180}}
	grafo["Chicago"] = []Edge{{to: "El Paso", cost: 80}}
	grafo["Denver"] = []Edge{{to: "Chicago", cost: 40}, {to: "El Paso", cost: 140}}
	grafo["El Paso"] = []Edge{}
	return grafo
}

func main() {
	graph := construirGrafo()

	fmt.Println("========================================================")
	fmt.Println("map vs map+sort en Dijkstra (Comparación BTreeMap/HashMap)")
	fmt.Println("========================================================")

	// --- Ejemplo 1: Dijkstra con mapa ordenado (output determinista) ---
	fmt.Println("\n--- Ejemplo 1: Dijkstra ordenado (equivalente BTreeMap) ---")
	result := dijkstraBTree(graph, "Atlanta")
	for _, city := range sortedKeys(result.cost) {
		if result.cost[city] < infinity {
			ruta := findPath(result.predecessors, "Atlanta", city)
			fmt.Printf("  Atlanta -> %s : $%d (ruta: %s)\n", city, result.cost[city], ruta)
		}
	}

	// --- Ejemplo 2: Dijkstra con map simple (sin orden) ---
	fmt.Println("\n--- Ejemplo 2: Dijkstra con map (sin orden; se ordena al imprimir) ---")
	costHash := dijkstraHash(graph, "Atlanta")
	for _, city := range sortedKeys(costHash) {
		if costHash[city] < infinity {
			fmt.Printf("  Atlanta -> %s : $%d\n", city, costHash[city])
		}
	}

	// --- Ejemplo 3: Range query: ciudades de 'A' a 'C' ---
	fmt.Println("\n--- Ejemplo 3: Range query: ciudades de 'A' a 'C' ---")
	for _, city := range rangeQuery(graph, "Atlanta", "C") {
		fmt.Printf("  %s : distancia = $%d\n", city, costHash[city])
	}

	// --- Ejemplo 4: Min/Max (primera/última ciudad en orden alfabético) ---
	fmt.Println("\n--- Ejemplo 4: Primera/última ciudad (orden alfabético) ---")
	keys := sortedKeys(graph)
	fmt.Printf("  Primera ciudad (A..Z): %s\n", keys[0])
	fmt.Printf("  Última ciudad (A..Z): %s\n", keys[len(keys)-1])

	// --- Ejemplo 5: Iteración ordenada ---
	fmt.Println("\n--- Ejemplo 5: Ciudades en orden alfabético ---")
	for _, city := range keys {
		if c := costHash[city]; c < infinity {
			fmt.Printf("  %s = $%d\n", city, c)
		} else {
			fmt.Printf("  %s = inalcanzable\n", city)
		}
	}

	fmt.Println("\n--- Comparación ---")
	fmt.Println("map:        la iteración no tiene orden definido")
	fmt.Println("map+sort:   las claves se imprimen en orden alfabético")
}
