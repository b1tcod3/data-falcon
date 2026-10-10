package main

import (
	"reflect"
	"testing"
)

func mapaCiudades() map[string][]Edge {
	return map[string][]Edge{
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
}

func TestRutaMasBarataElPaso(t *testing.T) {
	dist := dijkstra(mapaCiudades(), "Atlanta")
	if dist["El Paso"] != 280 {
		t.Errorf("El Paso debería costar $280, se obtuvo $%d", dist["El Paso"])
	}
}

func TestOrigenMismo(t *testing.T) {
	dist := dijkstra(mapaCiudades(), "Atlanta")
	if dist["Atlanta"] != 0 {
		t.Errorf("el origen debería costar $0, se obtuvo $%d", dist["Atlanta"])
	}
}

func TestConexionDirecta(t *testing.T) {
	dist := dijkstra(mapaCiudades(), "Atlanta")
	if dist["Boston"] != 100 {
		t.Errorf("Boston debería costar $100, se obtuvo $%d", dist["Boston"])
	}
	if dist["Denver"] != 160 {
		t.Errorf("Denver debería costar $160, se obtuvo $%d", dist["Denver"])
	}
}

func TestRutaIndirectaMasBarata(t *testing.T) {
	// Denver -> Chicago (40) es más barato que Boston -> Chicago (120)
	dist := dijkstra(mapaCiudades(), "Atlanta")
	// Atlanta -> Denver (160) -> Chicago (40) = 200
	// vs Atlanta -> Boston (100) -> Chicago (120) = 220
	if dist["Chicago"] != 200 {
		t.Errorf("Chicago debería costar $200, se obtuvo $%d", dist["Chicago"])
	}
}

func TestCiudadAislada(t *testing.T) {
	grafo := mapaCiudades()
	grafo["Solitaria"] = []Edge{}
	dist := dijkstra(grafo, "Atlanta")
	if _, existe := dist["Solitaria"]; existe {
		t.Error("una ciudad aislada no debería ser alcanzable")
	}
}

func TestGrafoVacio(t *testing.T) {
	var grafo map[string][]Edge
	dist := dijkstra(grafo, "Origen")
	if !reflect.DeepEqual(dist, map[string]uint32{"Origen": 0}) {
		t.Errorf("con grafo vacío solo debe existir el origen, se obtuvo %v", dist)
	}
}

func TestDosCaminosMismoDestino(t *testing.T) {
	grafo := map[string][]Edge{
		"A": {{to: "B", cost: 5}, {to: "C", cost: 10}},
		"B": {{to: "C", cost: 3}},
		"C": {},
	}
	dist := dijkstra(grafo, "A")
	// A -> B (5) -> C (3) = 8 vs A -> C (10) = 10
	if dist["C"] != 8 {
		t.Errorf("C debería costar $8, se obtuvo $%d", dist["C"])
	}
}
