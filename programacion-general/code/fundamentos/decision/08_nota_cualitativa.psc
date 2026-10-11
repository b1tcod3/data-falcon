// Ejercicio de decision: nota cualitativa (version PSeInt)
//
// A partir de una nota cuantitativa (entre 0.0 y 5.0) se obtiene la
// calificacion cualitativa:
//   4.5 a 5.0  -> Excelente
//   4.0 a 4.49 -> Bueno
//   3.5 a 3.99 -> Aceptable
//   2.5 a 3.49 -> Insuficiente
//   0.0 a 2.49 -> Deficiente

Algoritmo NotaCualitativa
    Definir nota Como Real

    Escribir "Ingrese la nota (0.0 a 5.0):"
    Leer nota

    Escribir ""
    Si nota >= 0 Y nota <= 5 Entonces
        Si nota >= 4.5 Entonces
            Escribir "Calificacion: Excelente"
        Sino
            Si nota >= 4.0 Entonces
                Escribir "Calificacion: Bueno"
            Sino
                Si nota >= 3.5 Entonces
                    Escribir "Calificacion: Aceptable"
                Sino
                    Si nota >= 2.5 Entonces
                        Escribir "Calificacion: Insuficiente"
                    Sino
                        Escribir "Calificacion: Deficiente"
                    FinSi
                FinSi
            FinSi
        FinSi
    Sino
        Escribir "La nota debe estar entre 0.0 y 5.0."
    FinSi
FinAlgoritmo
