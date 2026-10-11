// Ejercicio de decision: mensaje segun la temperatura (version PSeInt)
//
// Segun la temperatura del dia se imprime un mensaje:
//   "Hace frio"  si la temperatura es menor a 23 C
//   "Buen dia"   si la temperatura esta entre 23 C y menos de 30 C
//   "Hace calor" si la temperatura es igual o mayor a 30 C

Algoritmo MensajeTemperatura
    Definir temperatura Como Real

    Escribir "Temperatura del dia (grados C):"
    Leer temperatura

    Escribir ""
    Si temperatura < 23 Entonces
        Escribir "Hace frio"
    Sino
        Si temperatura < 30 Entonces
            Escribir "Buen dia"
        Sino
            Escribir "Hace calor"
        FinSi
    FinSi
FinAlgoritmo
