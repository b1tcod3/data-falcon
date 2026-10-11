// Ejercicio de decision: simbolos quimicos (version PSeInt)
//
// Dado el simbolo de un elemento quimico se imprime su nombre:
//   H -> Hidrogeno ; O -> Oxigeno ; N -> Nitrogeno
//   otro simbolo -> "Elemento no contemplado"

Algoritmo SimboloQuimico
    Definir simbolo, nombre Como Caracter

    Escribir "Ingrese el simbolo del elemento (H, O o N):"
    Leer simbolo
    simbolo <- Mayusculas(simbolo)

    Segun simbolo Hacer
        "H":
            nombre <- "Hidrogeno"
        "O":
            nombre <- "Oxigeno"
        "N":
            nombre <- "Nitrogeno"
        De Otro Modo:
            nombre <- "Elemento no contemplado"
    FinSegun

    Escribir ""
    Escribir nombre
FinAlgoritmo
