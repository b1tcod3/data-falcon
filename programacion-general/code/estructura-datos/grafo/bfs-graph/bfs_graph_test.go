package main

import (
	"reflect"
	"testing"
)

func grafoDePrueba() *SocialGraph {
	g := NewSocialGraph()
	for _, persona := range []string{"Ana", "Carlos", "Beatriz", "David"} {
		g.AddPerson(persona)
	}
	g.AddFriendship("Ana", "Carlos")
	g.AddFriendship("Ana", "Beatriz")
	g.AddFriendship("Carlos", "Beatriz")
	g.AddFriendship("Carlos", "David")
	return g
}

func TestAddPerson(t *testing.T) {
	g := NewSocialGraph()
	g.AddPerson("Ana")
	if !g.HasPerson("Ana") {
		t.Error("HasPerson(Ana) debería ser true")
	}
	if g.HasPerson("Carlos") {
		t.Error("HasPerson(Carlos) debería ser false")
	}
}

func TestAddPersonNoDuplica(t *testing.T) {
	g := NewSocialGraph()
	g.AddPerson("Ana")
	g.AddPerson("Ana")
	if nc := len(g.network["Ana"]); nc != 0 {
		t.Errorf("Ana debería tener 0 amigos, tiene %d", nc)
	}
}

func TestBfsDesdeAna(t *testing.T) {
	g := grafoDePrueba()
	got := g.BfsOrder("Ana")
	// Los vecinos de Ana (Carlos, Beatriz) se visitan antes que David
	if len(got) != 4 {
		t.Fatalf("se esperaban 4 personas, se obtuvieron %v", got)
	}
	if got[0] != "Ana" {
		t.Errorf("el primer nodo debería ser Ana, es %q", got[0])
	}
	if got[1] != "Carlos" || got[2] != "Beatriz" {
		t.Errorf("los vecinos directos deberían ser Carlos y Beatriz, se obtuvo %v", got[1:3])
	}
	if got[3] != "David" {
		t.Errorf("David debería ser el último, se obtuvo %q", got[3])
	}
}

func TestBfsDesdeBeatriz(t *testing.T) {
	g := grafoDePrueba()
	got := g.BfsOrder("Beatriz")
	if got[0] != "Beatriz" {
		t.Errorf("el primer nodo debería ser Beatriz, es %q", got[0])
	}
	// Sin la arista Ana-Beatriz solo se llegaría a Ana vía Carlos
	cubreTodos := map[string]bool{}
	for _, p := range got {
		cubreTodos[p] = true
	}
	for _, persona := range []string{"Ana", "Carlos", "Beatriz", "David"} {
		if !cubreTodos[persona] {
			t.Errorf("el recorrido desde Beatriz debería alcanzar a %s, se obtuvo %v", persona, got)
		}
	}
}

func TestBfsPersonaInexistente(t *testing.T) {
	g := grafoDePrueba()
	got := g.BfsOrder("Zoe")
	if len(got) != 1 || got[0] != "Zoe" {
		t.Errorf("se esperaba [Zoe], se obtuvo %v", got)
	}
}

func TestGrafoSinConexiones(t *testing.T) {
	g := NewSocialGraph()
	g.AddPerson("Ana")
	g.AddPerson("Carlos")
	got := g.BfsOrder("Ana")
	want := []string{"Ana"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("BfsOrder() = %v, esperado %v", got, want)
	}
}

func TestAddFriendshipDirigidaAmbosLados(t *testing.T) {
	g := NewSocialGraph()
	g.AddPerson("Ana")
	g.AddPerson("Carlos")
	g.AddFriendship("Ana", "Carlos")

	amigosAna := g.network["Ana"]
	amigosCarlos := g.network["Carlos"]
	if len(amigosAna) != 1 || amigosAna[0] != "Carlos" {
		t.Errorf("Ana debería tener a Carlos como amigo, tiene %v", amigosAna)
	}
	if len(amigosCarlos) != 1 || amigosCarlos[0] != "Ana" {
		t.Errorf("Carlos debería tener a Ana como amigo, tiene %v", amigosCarlos)
	}
}
