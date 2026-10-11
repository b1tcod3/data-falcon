// Ejercicio secuencial: notas ponderadas (version PSeInt)
//
// La nota definitiva se calcula asi:
//   - 15% el promedio de dos talleres
//   - 30% el promedio de tres evaluaciones
//   - 30% el trabajo final (una calificacion)
//   - 25% el promedio de cuatro seguimientos
// Se calcula e imprime la nota definitiva del estudiante.

Algoritmo NotasPonderadas
    Definir peso_talleres, peso_evaluaciones, peso_trabajo, peso_seguimientos Como Real
    Definir prom_talleres, prom_evaluaciones, prom_seguimientos Como Real
    Definir talleres, evaluaciones, seguimientos Como Real
    Definir trabajo, definitiva Como Real
    Definir i Como Entero

    peso_talleres <- 0.15
    peso_evaluaciones <- 0.30
    peso_trabajo <- 0.30
    peso_seguimientos <- 0.25

    Dimension talleres[2]
    Dimension evaluaciones[3]
    Dimension seguimientos[4]

    Para i <- 1 Hasta 2 Hacer
        Escribir "Nota taller ", i, ":"
        Leer talleres[i]
    FinPara
    Para i <- 1 Hasta 3 Hacer
        Escribir "Nota evaluacion ", i, ":"
        Leer evaluaciones[i]
    FinPara
    Escribir "Nota trabajo final:"
    Leer trabajo
    Para i <- 1 Hasta 4 Hacer
        Escribir "Nota seguimiento ", i, ":"
        Leer seguimientos[i]
    FinPara

    prom_talleres <- 0
    Para i <- 1 Hasta 2 Hacer
        prom_talleres <- prom_talleres + talleres[i]
    FinPara
    prom_talleres <- prom_talleres / 2

    prom_evaluaciones <- 0
    Para i <- 1 Hasta 3 Hacer
        prom_evaluaciones <- prom_evaluaciones + evaluaciones[i]
    FinPara
    prom_evaluaciones <- prom_evaluaciones / 3

    prom_seguimientos <- 0
    Para i <- 1 Hasta 4 Hacer
        prom_seguimientos <- prom_seguimientos + seguimientos[i]
    FinPara
    prom_seguimientos <- prom_seguimientos / 4

    definitiva <- prom_talleres * peso_talleres + prom_evaluaciones * peso_evaluaciones + trabajo * peso_trabajo + prom_seguimientos * peso_seguimientos

    Escribir ""
    Escribir "Nota definitiva: ", definitiva
FinAlgoritmo
