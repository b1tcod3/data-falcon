// Ejercicio de decision: cuadrado condicional (version PSeInt)
//
// Calcular el cuadrado de un numero solo si este es igual a 10, 20, 30 o 40;
// en caso contrario el resultado debe ser cero.

Algoritmo CuadradoCondicional
    Definir numero, cuadrado Como Real

    Escribir "Ingrese un numero (opciones: 10, 20, 30 o 40):"
    Leer numero

    Si numero = 10 O numero = 20 O numero = 30 O numero = 40 Entonces
        cuadrado <- numero^2
    Sino
        cuadrado <- 0
    FinSi

    Escribir ""
    Escribir "Resultado: ", cuadrado
FinAlgoritmo
