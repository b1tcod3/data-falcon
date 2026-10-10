package main

import "testing"

func TestPrintManagerFIFO(t *testing.T) {
	pm := NewPrintManager()
	pm.QueuePrintJob("Documento 1")
	pm.QueuePrintJob("Documento 2")
	pm.QueuePrintJob("Documento 3")
	pm.Run()

	if len(pm.queue) != 0 {
		t.Errorf("la cola debería quedar vacía después de Run(), quedan %d", len(pm.queue))
	}
}

func TestPrintManagerVacio(t *testing.T) {
	pm := NewPrintManager()
	pm.Run() // no debe panic
	if len(pm.queue) != 0 {
		t.Errorf("la cola debería estar vacía, quedan %d", len(pm.queue))
	}
}

func TestQueuePrintJobOrden(t *testing.T) {
	pm := NewPrintManager()
	pm.QueuePrintJob("A")
	pm.QueuePrintJob("B")
	if len(pm.queue) != 2 {
		t.Errorf("la cola debería tener 2 elementos, tiene %d", len(pm.queue))
	}
	if pm.queue[0] != "A" {
		t.Errorf("el primer elemento debería ser A, es %q", pm.queue[0])
	}
	if pm.queue[1] != "B" {
		t.Errorf("el segundo elemento debería ser B, es %q", pm.queue[1])
	}
}
