// Ejercicio de decision: valor absoluto (version PSeInt)
//
// Dado un numero entero, calcular e imprimir su valor absoluto.

Algoritmo ValorAbsoluto
    Definir numero Como Entero

    Escribir "Ingrese un numero entero (puede ser negativo):"
    Leer numero

    Si numero < 0 Entonces
        numero <- -numero
    FinSi

    Escribir ""
    Escribir "Valor absoluto: ", numero
FinAlgoritmo
