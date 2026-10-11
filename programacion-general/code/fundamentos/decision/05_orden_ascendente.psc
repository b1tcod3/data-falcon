// Ejercicio de decision: numeros en orden ascendente (version PSeInt)
//
// Dados dos numeros, mostrarlos en orden ascendente (de menor a mayor).

Algoritmo OrdenAscendente
    Definir num1, num2, menor, mayor Como Real

    Escribir "Primer numero:"
    Leer num1
    Escribir "Segundo numero:"
    Leer num2

    Si num1 < num2 Entonces
        menor <- num1
        mayor <- num2
    Sino
        menor <- num2
        mayor <- num1
    FinSi

    Escribir ""
    Escribir "Orden ascendente: ", menor, " - ", mayor
FinAlgoritmo
