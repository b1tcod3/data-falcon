# Bubble Sort

**Bubble Sort** recorre repetidamente el arreglo comparando cada par de elementos adyacentes e intercambiándolos si están en el orden equivocado. En cada pasada, el elemento más grande "burbujea" hasta el final.

## Algoritmo en Go

```go
func BubbleSort[T cmp.Ordered](lista []T) {
	n := len(lista)
	for i := 0; i < n; i++ {
		intercambiado := false
		for j := 0; j < n-i-1; j++ {
			if lista[j] > lista[j+1] {
				lista[j], lista[j+1] = lista[j+1], lista[j]
				intercambiado = true
			}
		}
		if !intercambiado {
			break // ya está ordenado
		}
	}
}
```

## Optimización clave

La bandera `intercambiado` permite **salir antes**: si una pasada completa no hizo ningún intercambio, el arreglo ya está ordenado y no se necesitan más iteraciones.

## Complejidad

| Caso | Complejidad |
| --- | --- |
| Peor caso (orden inverso) | O(n²) |
| Mejor caso (ya ordenado) | O(n) |
| Promedio | O(n²) |
| Espacio | O(1) |

Bubble Sort es **estable** (mantiene el orden relativo de elementos iguales) pero ineficiente para listas grandes.

## Código completo

- Implementación: [`sorts/bubble_sort.go`](../../code/estructura-datos/sorts/bubble_sort.go)
- Pruebas: [`sorts/sorts_test.go`](../../code/estructura-datos/sorts/sorts_test.go)

```bash
cd programacion-general/code/estructura-datos
go test ./sorts/ -run TestOrdenarListaDesordenada -v
```