// Grafo social representado mediante listas de adyacencia.
//
// Cada Person es un nodo del grafo; sus amigos forman sus aristas.
// En Rust se usaba Rc<RefCell<Person>>; en Go se usan punteros nativos.
//
// Ejecutar con:
//
//	go run ./grafo/social-graph
package main

import (
	"fmt"
	"strings"
)

// Person es un nodo del grafo social.
type Person struct {
	name    string
	friends []*Person
}

// NewPerson crea una persona sin amigos.
func NewPerson(name string) *Person {
	return &Person{name: name, friends: []*Person{}}
}

// AddFriend agrega una amistad (evitando duplicados).
// Complejidad: O(n) por la comprobación de duplicados.
func (p *Person) AddFriend(friend *Person) {
	if !p.HasFriend(friend) {
		p.friends = append(p.friends, friend)
	}
}

// RemoveFriend elimina una amistad.
func (p *Person) RemoveFriend(friend *Person) {
	for i, f := range p.friends {
		if f == friend {
			p.friends = append(p.friends[:i], p.friends[i+1:]...)
			return
		}
	}
}

// FriendsCount retorna el número de amigos.
func (p *Person) FriendsCount() int {
	return len(p.friends)
}

// HasFriend indica si un amigo ya pertenece a la lista.
func (p *Person) HasFriend(friend *Person) bool {
	for _, f := range p.friends {
		if f == friend {
			return true
		}
	}
	return false
}

// FriendNames devuelve los nombres de los amigos.
func (p *Person) FriendNames() []string {
	nombres := make([]string, len(p.friends))
	for i, f := range p.friends {
		nombres[i] = f.name
	}
	return nombres
}

// PrintFriendships imprime la lista de amistades de la persona.
func (p *Person) PrintFriendships() {
	fmt.Printf("%s es amigo de: %s\n", p.name, strings.Join(p.FriendNames(), ", "))
}

func main() {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	beatriz := NewPerson("Beatriz")

	ana.AddFriend(carlos)
	ana.AddFriend(beatriz)
	carlos.AddFriend(ana)
	carlos.AddFriend(beatriz)

	fmt.Println("=== Grafo social ===")
	ana.PrintFriendships()
	carlos.PrintFriendships()
	beatriz.PrintFriendships()

	fmt.Printf("\n  Ana tiene %d amigos\n", ana.FriendsCount())
	fmt.Printf("  ¿Ana es amiga de Beatriz? %v\n", ana.HasFriend(beatriz))

	fmt.Println("\n  Ana deja de ser amiga de Carlos:")
	ana.RemoveFriend(carlos)
	ana.PrintFriendships()
}
