// Programa de ejemplo de una Pila (Stack) aplicada a un "linter" de
// llaves/paréntesis/corchetes balanceados.
//
// Ejecutar con:
//
//	go run ./pila
package main

import (
	"errors"
	"fmt"
)

// Linter revisa que los pares de apertura/cierre estén balanceados
// usando una pila (LIFO).
type Linter struct {
	lastErr string
	stack   []rune
}

// NewLinter crea un Linter vacío.
func NewLinter() *Linter {
	return &Linter{
		lastErr: "",
		stack:   []rune{},
	}
}

// Lint valida el texto y devuelve un error si los signos no están balanceados.
func (l *Linter) Lint(text string) error {
	l.stack = nil
	l.lastErr = ""

	for _, char := range text {
		if l.esApertura(char) {
			l.stack = append(l.stack, char)
		} else if l.esCierre(char) {
			if len(l.stack) == 0 {
				l.lastErr = fmt.Sprintf("%c no tiene un símbolo de apertura correspondiente", char)
				return errors.New(l.lastErr)
			}

			if !l.cierraLaAperturaMasReciente(char) {
				l.lastErr = fmt.Sprintf("%c no tiene su símbolo de apertura correspondiente", char)
				return errors.New(l.lastErr)
			}

			l.stack = l.stack[:len(l.stack)-1]
		}
	}

	if len(l.stack) > 0 {
		ultimo := l.stack[len(l.stack)-1]
		l.lastErr = fmt.Sprintf("%c no tiene su símbolo de cierre correspondiente", ultimo)
		return errors.New(l.lastErr)
	}

	return nil
}

// GetError devuelve el último error registrado.
func (l *Linter) GetError() string {
	return l.lastErr
}

func (l *Linter) esApertura(char rune) bool {
	return char == '(' || char == '[' || char == '{'
}

func (l *Linter) esCierre(char rune) bool {
	return char == ')' || char == ']' || char == '}'
}

func (l *Linter) aperturaDe(char rune) rune {
	switch char {
	case ')':
		return '('
	case ']':
		return '['
	case '}':
		return '{'
	default:
		return 0
	}
}

func (l *Linter) aperturaMasReciente() rune {
	if len(l.stack) == 0 {
		return 0
	}
	return l.stack[len(l.stack)-1]
}

func (l *Linter) cierraLaAperturaMasReciente(char rune) bool {
	return l.aperturaDe(char) == l.aperturaMasReciente()
}

func main() {
	linter := NewLinter()

	ejemplos := []struct {
		texto  string
		valido bool
	}{
		{"()", true},
		{"({[]})", true},
		{"function() { return [1, 2, 3]; }", true},
		{"(", false},
		{")", false},
		{"([)]", false},
	}

	for _, ej := range ejemplos {
		err := linter.Lint(ej.texto)
		if (err == nil) != ej.valido {
			fmt.Printf("✗ %q: se esperaba %v, se obtuvo error=%v\n", ej.texto, ej.valido, err)
		} else if err != nil {
			fmt.Printf("✓ %q → error esperado: %v\n", ej.texto, err)
		} else {
			fmt.Printf("✓ %q → válido\n", ej.texto)
		}
	}
}
