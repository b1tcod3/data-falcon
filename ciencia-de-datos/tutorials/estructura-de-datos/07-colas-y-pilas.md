# Colas y Pilas

Las **colas** (Queue) y las **pilas** (Stack) son estructuras **lineales** con reglas de acceso opuestas. Ambas restringen *dónde* se inserta y se extrae.

| Estructura | Regla | Analogía |
| --- | --- | --- |
| Cola | FIFO (First In, First Out) | Fila del supermercado |
| Pila | LIFO (Last In, First Out) | Pila de platos |

## Cola: gestor de impresiones

Una impresora procesa trabajos en el orden en que llegan. La implementación en Go usa un slice y extrae el primer elemento:

```go
func (pm *PrintManager) QueuePrintJob(document string) {
	pm.queue = append(pm.queue, document) // encolar al final
}

func (pm *PrintManager) Run() {
	for len(pm.queue) > 0 {
		document := pm.queue[0]
		pm.queue = pm.queue[1:] // desencolar por el frente
		pm.Print(document)
	}
}
```

Código: [`cola/main.go`](../../../programacion-general/code/estructura-datos/cola/main.go) y sus [pruebas](../../../programacion-general/code/estructura-datos/cola/print_manager_test.go).

```bash
go run ./cola
# Documento 1
# Documento 2
# Documento 3
```

## Pila: linter de signos balanceados

Un corrector de sintaxis recorre un texto y apila cada signo de apertura (`(`, `[`, `{`). Al encontrar un cierre, verifica que coincida con el **último abierto** y lo desapila:

```go
for _, char := range text {
	if esApertura(char) {
		stack = append(stack, char)
	} else if esCierre(char) {
		if len(stack) == 0 {
			return errors.New("no tiene símbolo de apertura correspondiente")
		}
		if !cierraLaAperturaMasReciente(char) {
			return errors.New("no coincide con la apertura")
		}
		stack = stack[:len(stack)-1]
	}
}
```

Código: [`pila/main.go`](../../../programacion-general/code/estructura-datos/pila/main.go) y sus [pruebas](../../../programacion-general/code/estructura-datos/pila/linter_test.go).

```bash
go run ./pila
# ✓ "({[]})" → válido
# ✓ "(" → error esperado: ( no tiene su símbolo de cierre correspondiente
```

## Complejidad

| Operación | Cola | Pila |
| --- | --- | --- |
| Insertar | O(1) con lista enlazada / O(1) amortizado con slice | O(1) |
| Extraer | O(1) con lista enlazada | O(1) |
| Ver el frente/tope | O(1) | O(1) |

En Go, además del `map`, se puede representar una pila con `container/list` o con un slice; aquí se usó el slice por sencillez y claridad.

## Resumen

- Una **cola** atiende en orden de llegada; se usa en impresoras, colas de mensajes y BFS (lección 10).
- Una **pila** atiende lo más reciente primero; se usa en validación de signos, evaluación de expresiones y recorridos DFS.