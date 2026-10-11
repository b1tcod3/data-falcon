// Ejercicio de seleccion multiple: central telefonica (version PSeInt)
//
// Una central cobra por las llamadas de larga distancia segun el indicativo:
//   1 -> Bogota (50/min) ; 2 -> Cali (70/min) ; 4 -> Medellin (100/min) ;
//   5 -> Barranquilla (160/min) ; 6 -> Pereira (180/min) ; 7 -> Cucuta (190/min)
// Se muestra la ciudad, la tarifa por minuto y el valor total de la llamada.

Algoritmo CentralTelefonica
    Definir indicativo Como Entero
    Definir minutos, tarifa, valor_total Como Real
    Definir ciudad Como Caracter

    ciudad <- "Desconocida"
    tarifa <- 0

    Escribir "Indicativo de la ciudad (1, 2, 4, 5, 6 o 7):"
    Leer indicativo
    Escribir "Numero de minutos:"
    Leer minutos

    Segun indicativo Hacer
        1:
            ciudad <- "Bogota"
            tarifa <- 50
        2:
            ciudad <- "Cali"
            tarifa <- 70
        4:
            ciudad <- "Medellin"
            tarifa <- 100
        5:
            ciudad <- "Barranquilla"
            tarifa <- 160
        6:
            ciudad <- "Pereira"
            tarifa <- 180
        7:
            ciudad <- "Cucuta"
            tarifa <- 190
        De Otro Modo:
            tarifa <- 0
    FinSegun

    Escribir ""
    Si tarifa = 0 Entonces
        Escribir "Indicativo no contemplado en la central."
    Sino
        valor_total <- tarifa * minutos
        Escribir "Ciudad: ", ciudad
        Escribir "Tarifa por minuto: $ ", tarifa
        Escribir "Valor total de la llamada: $ ", valor_total
    FinSi
FinAlgoritmo
