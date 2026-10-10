// Grafo social con Búsqueda en Amplitud (BFS).
//
// El grafo se representa como listas de adyacencia: un map que asocia cada
// persona (nodo) con la lista de sus amigos (vecinos).
//
// Ejecutar con:
//
//	go run ./grafo/bfs-graph
package main

import (
	"fmt"
	"strings"
)

// SocialGraph es un grafo no dirigido representado con listas de adyacencia.
type SocialGraph struct {
	network map[string][]string
}

// NewSocialGraph crea un grafo vacío.
func NewSocialGraph() *SocialGraph {
	return &SocialGraph{network: map[string][]string{}}
}

// AddPerson registra una persona en el grafo.
func (g *SocialGraph) AddPerson(name string) {
	if _, existe := g.network[name]; !existe {
		g.network[name] = []string{}
	}
}

// HasPerson indica si una persona existe en el grafo.
func (g *SocialGraph) HasPerson(name string) bool {
	_, existe := g.network[name]
	return existe
}

// AddFriendship agrega una arista (bidireccional) entre dos personas.
func (g *SocialGraph) AddFriendship(name1, name2 string) {
	g.network[name1] = append(g.network[name1], name2)
	g.network[name2] = append(g.network[name2], name1)
}

// BfsOrder recorre el grafo desde la persona inicial usando BFS
// (una cola asegura visitar primero los vecinos directos).
func (g *SocialGraph) BfsOrder(from string) []string {
	visitados := map[string]bool{}
	cola := []string{from}
	resultado := []string{}

	for len(cola) > 0 {
		persona := cola[0]
		cola = cola[1:]

		if visitados[persona] {
			continue
		}

		visitados[persona] = true
		resultado = append(resultado, persona)

		for _, amigo := range g.network[persona] {
			if !visitados[amigo] {
				cola = append(cola, amigo)
			}
		}
	}

	return resultado
}

// DisplayNetworkBfs imprime el recorrido BFS desde una persona.
func (g *SocialGraph) DisplayNetworkBfs(from string) {
	orden := g.BfsOrder(from)
	fmt.Printf("Red visible desde %s (BFS): %s\n", from, strings.Join(orden, " → "))
}

func main() {
	social := NewSocialGraph()
	for _, persona := range []string{"Ana", "Carlos", "Beatriz", "David"} {
		social.AddPerson(persona)
	}

	social.AddFriendship("Ana", "Carlos")
	social.AddFriendship("Ana", "Beatriz")
	social.AddFriendship("Carlos", "Beatriz")
	social.AddFriendship("Carlos", "David")

	fmt.Println("=== Búsqueda en Amplitud (BFS) ===")
	social.DisplayNetworkBfs("Ana")
	fmt.Printf("  ¿Existe David? %v\n", social.HasPerson("David"))
	fmt.Printf("  ¿Existe Zoe? %v\n", social.HasPerson("Zoe"))
}
