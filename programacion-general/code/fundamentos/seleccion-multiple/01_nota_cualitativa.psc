// Ejercicio de seleccion multiple: calificacion de una nota (version PSeInt)
//
// Dada una nota de 1 a 5 se imprime la calificacion correspondiente:
//   5 -> Excelente ; 4 -> Bueno ; 3 -> Aceptable ;
//   2 -> Insuficiente ; 1 -> Deficiente

Algoritmo NotaCualitativaSeleccion
    Definir nota Como Entero

    Escribir "Ingrese la nota (1 a 5):"
    Leer nota

    Escribir ""
    Segun nota Hacer
        5:
            Escribir "Excelente"
        4:
            Escribir "Bueno"
        3:
            Escribir "Aceptable"
        2:
            Escribir "Insuficiente"
        1:
            Escribir "Deficiente"
        De Otro Modo:
            Escribir "Nota fuera de rango (debe estar entre 1 y 5)"
    FinSegun
FinAlgoritmo
