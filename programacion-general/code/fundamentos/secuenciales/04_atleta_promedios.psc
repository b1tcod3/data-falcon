// Ejercicio secuencial: atleta y promedios de entrenamiento (version PSeInt)
//
// Un atleta mide el tiempo (en minutos) y la distancia (en metros) en sus
// tres dias de entrenamiento. Al final quiere saber el total de tiempo, la
// distancia total recorrida, el tiempo promedio y la distancia promedio.

Algoritmo AtletaPromedios
    Definir tiempos, distancias Como Real
    Definir total_tiempo, total_distancia, prom_tiempo, prom_distancia Como Real
    Definir dia Como Entero

    Dimension tiempos[3]
    Dimension distancias[3]

    Para dia <- 1 Hasta 3 Hacer
        Escribir "Tiempo dia ", dia, " (minutos):"
        Leer tiempos[dia]
        Escribir "Distancia dia ", dia, " (metros):"
        Leer distancias[dia]
    FinPara

    total_tiempo <- 0
    total_distancia <- 0
    Para dia <- 1 Hasta 3 Hacer
        total_tiempo <- total_tiempo + tiempos[dia]
        total_distancia <- total_distancia + distancias[dia]
    FinPara

    prom_tiempo <- total_tiempo / 3
    prom_distancia <- total_distancia / 3

    Escribir ""
    Escribir "=== Resultados del entrenamiento ==="
    Escribir "Tiempo total: ", total_tiempo, " minutos"
    Escribir "Distancia total: ", total_distancia, " metros"
    Escribir "Tiempo promedio por dia: ", prom_tiempo, " minutos"
    Escribir "Distancia promedio por dia: ", prom_distancia, " metros"
FinAlgoritmo
