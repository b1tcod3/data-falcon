// Algoritmo de Dijkstra en Go.
//
// Encuentra el camino más barato desde un nodo origen hacia todos los demás
// en un grafo ponderado con pesos no negativos.
//
// En Rust se usaba BinaryHeap con inversión de orden; en Go se usa el paquete
// estándar container/heap configurado como cola de prioridad mínima.
//
// Ejecutar con:
//
//	go run ./grafo/dijkstra
package main

import (
	"container/heap"
	"fmt"
)

// State es un candidato en la cola de prioridad: el costo acumulado para
// llegar a una ciudad.
type State struct {
	cost uint32
	city string
}

// PriorityQueue es una cola de prioridad mínima basada en el costo.
type PriorityQueue []State

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool { return pq[i].cost < pq[j].cost }

func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x any) { *pq = append(*pq, x.(State)) }

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

// dijkstra devuelve el costo más barato desde `start` hasta cada ciudad
// alcanzable. Complejidad: O((V + E) log V).
func dijkstra(graph map[string][]Edge, start string) map[string]uint32 {
	distances := map[string]uint32{}
	pq := &PriorityQueue{}

	distances[start] = 0
	heap.Push(pq, State{cost: 0, city: start})

	for pq.Len() > 0 {
		s := heap.Pop(pq).(State)

		if s.cost > distances[s.city] {
			continue
		}

		for _, edge := range graph[s.city] {
			nextCost := s.cost + edge.cost

			if actual, conocido := distances[edge.to]; !conocido || nextCost < actual {
				distances[edge.to] = nextCost
				heap.Push(pq, State{cost: nextCost, city: edge.to})
			}
		}
	}

	return distances
}

// Edge es una arista ponderada del grafo.
type Edge struct {
	to   string
	cost uint32
}

func main() {
	mapa := map[string][]Edge{
		"Atlanta": {
			{to: "Boston", cost: 100},
			{to: "Denver", cost: 160},
		},
		"Boston": {
			{to: "Chicago", cost: 120},
			{to: "Denver", cost: 180},
		},
		"Chicago": {
			{to: "El Paso", cost: 80},
		},
		"Denver": {
			{to: "Chicago", cost: 40},
			{to: "El Paso", cost: 140},
		},
		"El Paso": {},
	}

	rutas := dijkstra(mapa, "Atlanta")

	fmt.Println("Costo más bajo desde Atlanta a El Paso: $", rutas["El Paso"])
	fmt.Println("Costo más bajo desde Atlanta a Boston: $", rutas["Boston"])
	fmt.Println("Costo más bajo desde Atlanta a Denver: $", rutas["Denver"])
	fmt.Println("Costo más bajo desde Atlanta a Chicago: $", rutas["Chicago"])

	// Ruta esperada: Atlanta -> Denver (160) -> Chicago (40) -> El Paso (80) = 280
	if rutas["El Paso"] != 280 {
		panic(fmt.Sprintf("la ruta más barata a El Paso debería costar $280, se obtuvo $%d", rutas["El Paso"]))
	}
}
