// Ejercicio secuencial: temperatura de un liquido (version PSeInt)
//
// Un liquido se somete a tres cambios de temperatura en cadena:
//   1. aumenta un 43% con respecto a la inicial
//   2. disminuye un 35% con respecto a la temperatura resultante
//   3. aumenta un 150% con respecto a la temperatura resultante
// Se calcula e imprime la temperatura en cada etapa y la final.

Algoritmo TemperaturaLiquido
    Definir temp_inicial Como Real
    Definir despues_aumento_1, despues_disminucion, temperatura_final Como Real
    Definir aumento_1, disminucion, aumento_2 Como Real

    aumento_1 <- 0.43
    disminucion <- 0.35
    aumento_2 <- 1.50

    Escribir "Temperatura inicial (grados C):"
    Leer temp_inicial

    despues_aumento_1 <- temp_inicial * (1 + aumento_1)
    despues_disminucion <- despues_aumento_1 * (1 - disminucion)
    temperatura_final <- despues_disminucion * (1 + aumento_2)

    Escribir ""
    Escribir "=== Cambios de temperatura ==="
    Escribir "Temperatura inicial: ", temp_inicial, " C"
    Escribir "Tras +43%: ", despues_aumento_1, " C"
    Escribir "Tras -35%: ", despues_disminucion, " C"
    Escribir "Temperatura final (+150%): ", temperatura_final, " C"
FinAlgoritmo
