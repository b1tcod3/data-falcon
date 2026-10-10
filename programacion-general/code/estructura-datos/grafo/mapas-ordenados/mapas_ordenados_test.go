package main

import (
	"reflect"
	"testing"
)

func TestBTreeOrdenClaves(t *testing.T) {
	graph := construirGrafo()
	got := sortedKeys(graph)
	want := []string{"Atlanta", "Boston", "Chicago", "Denver", "El Paso"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("sortedKeys() = %v, esperado %v", got, want)
	}
}

func TestRangeQuery(t *testing.T) {
	graph := construirGrafo()
	got := rangeQuery(graph, "Atlanta", "Chicago")
	want := []string{"Atlanta", "Boston", "Chicago"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("rangeQuery() = %v, esperado %v", got, want)
	}
}

func TestMinMax(t *testing.T) {
	graph := construirGrafo()
	keys := sortedKeys(graph)
	if keys[0] != "Atlanta" {
		t.Errorf("la primera clave debería ser Atlanta, es %q", keys[0])
	}
	if keys[len(keys)-1] != "El Paso" {
		t.Errorf("la última clave debería ser El Paso, es %q", keys[len(keys)-1])
	}
}

func TestDijkstraBTreeCostos(t *testing.T) {
	graph := construirGrafo()
	result := dijkstraBTree(graph, "Atlanta")

	casos := map[string]uint32{
		"Atlanta": 0,
		"Boston":  100,
		"Denver":  160,
		"Chicago": 200,
		"El Paso": 280,
	}
	for ciudad, esperado := range casos {
		if result.cost[ciudad] != esperado {
			t.Errorf("costo a %s = $%d, esperado $%d", ciudad, result.cost[ciudad], esperado)
		}
	}
}

func TestFindPath(t *testing.T) {
	graph := construirGrafo()
	result := dijkstraBTree(graph, "Atlanta")
	got := findPath(result.predecessors, "Atlanta", "El Paso")
	want := []string{"Atlanta", "Denver", "Chicago", "El Paso"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("findPath() = %v, esperado %v", got, want)
	}
}

func TestIterOrdenado(t *testing.T) {
	graph := construirGrafo()
	result := dijkstraBTree(graph, "Atlanta")
	keys := sortedKeys(result.cost)
	if keys[0] != "Atlanta" {
		t.Errorf("la primera clave debería ser Atlanta, es %q", keys[0])
	}
	if keys[len(keys)-1] != "El Paso" {
		t.Errorf("la última clave debería ser El Paso, es %q", keys[len(keys)-1])
	}
}
