// Ejercicio de decision: promedio de goles (version PSeInt)
//
// Un equipo registra los goles anotados en cuatro encuentros. Se calcula e
// imprime el promedio de goles solo si la suma de los goles es mayor que 10;
// en caso contrario se avisa que no se calcula el promedio.

Algoritmo PromedioGoles
    Definir goles, suma Como Entero
    Definir promedio Como Real
    Definir i Como Entero
    Dimension goles[4]

    Para i <- 1 Hasta 4 Hacer
        Escribir "Goles del encuentro ", i, ":"
        Leer goles[i]
    FinPara

    suma <- 0
    Para i <- 1 Hasta 4 Hacer
        suma <- suma + goles[i]
    FinPara

    Escribir ""
    Si suma > 10 Entonces
        promedio <- suma / 4
        Escribir "Promedio de goles: ", promedio
    Sino
        Escribir "La suma no supera los 10 goles, no se pide calcular promedio."
    FinSi
FinAlgoritmo
