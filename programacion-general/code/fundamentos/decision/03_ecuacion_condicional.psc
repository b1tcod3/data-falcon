// Ejercicio de decision: ecuacion condicional (version PSeInt)
//
// Dado un valor r se halla el resultado de la ecuacion:
//   P = (r - 2)^3   si r es diferente de 2
//   P = 1           si r es igual a 2

Algoritmo EcuacionCondicional
    Definir r, p Como Real

    Escribir "Ingrese el valor de r:"
    Leer r

    Si r <> 2 Entonces
        p <- (r - 2)^3
    Sino
        p <- 1
    FinSi

    Escribir ""
    Escribir "El valor de P es: ", p
FinAlgoritmo
