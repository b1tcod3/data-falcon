// Ejercicio secuencial: reparto de una herencia (version PSeInt)
//
// El testamento establece: a la esposa le corresponde el 40% del total
// heredado y el resto se distribuye entre los cuatro hijos con los
// porcentajes 30%, 20%, 40% y 10% respectivamente (sobre el resto).
// Se muestra lo que le corresponde a la madre, a los hijos en general y a
// cada uno de ellos.

Algoritmo Herencia
    Definir total_heredado, madre, resto, total_hijos Como Real
    Definir porc_esposa Como Real
    Definir porc_hijos, hijos Como Real
    Definir i Como Entero

    porc_esposa <- 0.40
    Dimension porc_hijos[4]
    porc_hijos[1] <- 0.30
    porc_hijos[2] <- 0.20
    porc_hijos[3] <- 0.40
    porc_hijos[4] <- 0.10
    Dimension hijos[4]

    Escribir "Total de la herencia:"
    Leer total_heredado

    madre <- total_heredado * porc_esposa
    resto <- total_heredado - madre

    total_hijos <- 0
    Para i <- 1 Hasta 4 Hacer
        hijos[i] <- resto * porc_hijos[i]
        total_hijos <- total_hijos + hijos[i]
    FinPara

    Escribir ""
    Escribir "=== Reparto de la herencia ==="
    Escribir "Madre (40%): $ ", madre
    Escribir "Resto a repartir (60%): $ ", resto
    Para i <- 1 Hasta 4 Hacer
        Escribir "Hijo ", i, " (", porc_hijos[i] * 100, "% del resto): $ ", hijos[i]
    FinPara
    Escribir "Total para los hijos: $ ", total_hijos
FinAlgoritmo
