// Ejercicio de seleccion multiple: signos zodiacales (version PSeInt)
//
// Dado un signo zodiacal, indicar a que elemento pertenece:
//   Fuego: Aries, Leo, Sagitario
//   Tierra: Tauro, Virgo, Capricornio
//   Aire: Geminis, Libra, Acuario
//   Agua: Cancer, Escorpion, Piscis
// La entrada se normaliza a mayusculas para no depender del uso de
// tildes ni de mayusculas/minusculas.

Algoritmo SignosZodiacales
    Definir signo, elemento Como Caracter

    elemento <- ""

    Escribir "Ingrese su signo zodiacal:"
    Leer signo
    signo <- Mayusculas(signo)

    Segun signo Hacer
        "ARIES":
            elemento <- "Fuego"
        "LEO":
            elemento <- "Fuego"
        "SAGITARIO":
            elemento <- "Fuego"
        "TAURO":
            elemento <- "Tierra"
        "VIRGO":
            elemento <- "Tierra"
        "CAPRICORNIO":
            elemento <- "Tierra"
        "GEMINIS", "GÉMINIS":
            elemento <- "Aire"
        "LIBRA":
            elemento <- "Aire"
        "ACUARIO":
            elemento <- "Aire"
        "CANCER", "CÁNCER":
            elemento <- "Agua"
        "ESCORPION", "ESCORPIÓN":
            elemento <- "Agua"
        "PISCIS":
            elemento <- "Agua"
        De Otro Modo:
            elemento <- ""
    FinSegun

    Escribir ""
    Si elemento = "" Entonces
        Escribir "Signo zodiacal no contemplado."
    Sino
        Escribir "El elemento de ", signo, " es: ", elemento
    FinSi
FinAlgoritmo
