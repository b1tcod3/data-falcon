// Ejercicio de seleccion multiple: extensiones telefonicas (version PSeInt)
//
// Una empresa tiene asignadas estas extensiones:
//   750 funcionalidad de calidad      751 calidad
//   752 control total de calidad      753 recursos humanos
//   754 bienestar laboral             755 sistema de compras
//   756 sistemas                      757 mantenimiento de software
//   758 inventarios                   759 caja de compensacion
//   760 contabilidad                  780 gerencia
// Se imprime la dependencia de la extension (los nombres de los encargados
// no fueron suministrados).

Algoritmo Extensiones
    Definir extension Como Entero
    Definir encargado Como Caracter

    encargado <- ""

    Escribir "Ingrese la extension (750 a 760 o 780):"
    Leer extension

    Segun extension Hacer
        750:
            encargado <- "funcionalidad de calidad"
        751:
            encargado <- "calidad"
        752:
            encargado <- "control total de calidad"
        753:
            encargado <- "recursos humanos"
        754:
            encargado <- "bienestar laboral"
        755:
            encargado <- "sistema de compras"
        756:
            encargado <- "sistemas"
        757:
            encargado <- "mantenimiento de software"
        758:
            encargado <- "inventarios"
        759:
            encargado <- "caja de compensacion"
        760:
            encargado <- "contabilidad"
        780:
            encargado <- "gerencia"
        De Otro Modo:
            encargado <- ""
    FinSegun

    Escribir ""
    Si encargado = "" Entonces
        Escribir "Extension no asignada o inexistente."
    Sino
        Escribir "La extension ", extension, " pertenece a: ", encargado
    FinSi
FinAlgoritmo
