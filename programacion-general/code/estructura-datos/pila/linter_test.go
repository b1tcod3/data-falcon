package main

import "testing"

func TestLintSignosValidos(t *testing.T) {
	linter := NewLinter()
	validos := []string{
		"()",
		"[]",
		"{}",
		"({[]})",
		"function() { return [1, 2, 3]; }",
	}
	for _, texto := range validos {
		if err := linter.Lint(texto); err != nil {
			t.Errorf("Lint(%q): error inesperado: %v", texto, err)
		}
	}
}

func TestLintFaltaCierre(t *testing.T) {
	linter := NewLinter()
	err := linter.Lint("(")
	if err == nil {
		t.Fatal("se esperaba un error para '('")
	}
	if linter.GetError() != "( no tiene su símbolo de cierre correspondiente" {
		t.Errorf("mensaje inesperado: %q", linter.GetError())
	}
}

func TestLintFaltaApertura(t *testing.T) {
	linter := NewLinter()
	err := linter.Lint(")")
	if err == nil {
		t.Fatal("se esperaba un error para ')'")
	}
	if linter.GetError() != ") no tiene un símbolo de apertura correspondiente" {
		t.Errorf("mensaje inesperado: %q", linter.GetError())
	}
}

func TestLintDesbalanceados(t *testing.T) {
	linter := NewLinter()
	if err := linter.Lint("([)]"); err == nil {
		t.Error("se esperaba un error para '([)]'")
	}
}

func TestLintTextoVacío(t *testing.T) {
	linter := NewLinter()
	if err := linter.Lint(""); err != nil {
		t.Errorf("el texto vacío debería ser válido, error: %v", err)
	}
}

func TestLintEstadoReutilizable(t *testing.T) {
	linter := NewLinter()
	if err := linter.Lint("("); err == nil {
		t.Error("primer Lint debería fallar")
	}
	// reutilizar el mismo linter no debe arrastrar la pila anterior
	if err := linter.Lint("()"); err != nil {
		t.Errorf("segundo Lint debería ser válido, error: %v", err)
	}
}
