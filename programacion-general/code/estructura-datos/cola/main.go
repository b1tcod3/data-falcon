// Programa de ejemplo de una Cola (Queue) aplicada a un gestor de
// impresiones (FIFO: el primer documento encolado es el primero en imprimirse).
//
// Ejecutar con:
//
//	go run ./cola
package main

import "fmt"

// PrintManager gestiona una cola de documentos a imprimir.
type PrintManager struct {
	queue []string
}

// NewPrintManager crea un gestor de impresión con la cola vacía.
func NewPrintManager() *PrintManager {
	return &PrintManager{queue: []string{}}
}

// QueuePrintJob encola un documento al final de la cola.
func (pm *PrintManager) QueuePrintJob(document string) {
	pm.queue = append(pm.queue, document)
}

// Run procesa los documentos en orden FIFO. En Go, el equivalente de
// shift/remove(0) es eliminar el primer elemento del slice.
func (pm *PrintManager) Run() {
	for len(pm.queue) > 0 {
		document := pm.queue[0]
		pm.queue = pm.queue[1:]
		pm.Print(document)
	}
}

// Print imprime un documento.
func (pm *PrintManager) Print(document string) {
	fmt.Println(document)
}

func main() {
	pm := NewPrintManager()
	pm.QueuePrintJob("Documento 1")
	pm.QueuePrintJob("Documento 2")
	pm.QueuePrintJob("Documento 3")
	pm.Run()
}
