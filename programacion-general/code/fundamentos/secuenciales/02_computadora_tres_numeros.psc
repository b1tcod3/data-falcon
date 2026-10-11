// Ejercicio secuencial: computadora que procesa tres numeros (version PSeInt)
//
// Solicita tres numeros y muestra la suma de estos; luego la division de la
// suma de los dos primeros entre la resta de los dos ultimos; y finalmente la
// multiplicacion de los resultados de la suma y la division.
//
// Nota: la resta de los dos ultimos se interpreta como num2 - num3.

Algoritmo ComputadoraTresNumeros
    Definir num1, num2, num3 Como Real
    Definir suma, resta, division, producto Como Real

    Escribir "Primer numero:"
    Leer num1
    Escribir "Segundo numero:"
    Leer num2
    Escribir "Tercer numero:"
    Leer num3

    suma <- num1 + num2 + num3
    resta <- num2 - num3
    division <- (num1 + num2) / resta
    producto <- suma * division

    Escribir ""
    Escribir "Suma de los tres numeros: ", suma
    Escribir "Division (num1 + num2) / (num2 - num3): ", division
    Escribir "Producto suma * division: ", producto
FinAlgoritmo
