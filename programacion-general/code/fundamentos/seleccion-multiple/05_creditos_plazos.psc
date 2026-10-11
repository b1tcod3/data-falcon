// Ejercicio de seleccion multiple: creditos por plazos (version PSeInt)
//
// Un almacen otorga creditos. Segun el plazo (en meses) el cliente recibe un
// articulo:
//   48 -> Computadora           36 -> Televisor de 42 pulgadas
//   24 -> BlackBerry            12 -> Camara digital
//   6  -> Impresora

Algoritmo CreditosPlazos
    Definir plazo Como Entero
    Definir articulo Como Caracter

    articulo <- ""

    Escribir "Ingrese el plazo en meses (48, 36, 24, 12 o 6):"
    Leer plazo

    Segun plazo Hacer
        48:
            articulo <- "Computadora"
        36:
            articulo <- "Televisor de 42 pulgadas"
        24:
            articulo <- "BlackBerry"
        12:
            articulo <- "Camara digital"
        6:
            articulo <- "Impresora"
        De Otro Modo:
            articulo <- ""
    FinSegun

    Escribir ""
    Si articulo = "" Entonces
        Escribir "Plazo no contemplado en el almacen."
    Sino
        Escribir "Con ", plazo, " meses recibe: ", articulo
    FinSi
FinAlgoritmo
