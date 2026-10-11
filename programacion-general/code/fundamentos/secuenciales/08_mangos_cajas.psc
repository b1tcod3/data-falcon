// Ejercicio secuencial: mangos en cajas (version PSeInt)
//
// Al vender el mango por cajas se aplican descuentos segun el tamano:
//   caja de 6 kg   -> sin descuento
//   caja de 10 kg  -> sin descuento
//   caja de 20 kg  -> 10% de descuento
//   caja de 50 kg  -> 25% de descuento
//   caja de 100 kg -> se paga la mitad del precio
// Se muestra el costo de cada tipo de caja.

Algoritmo MangosCajas
    Definir precio_kilo, descuento, costo Como Real
    Definir i Como Entero
    Dimension cajas[5]

    cajas[1] <- 6
    cajas[2] <- 10
    cajas[3] <- 20
    cajas[4] <- 50
    cajas[5] <- 100

    Escribir "Precio por kilogramo de mango:"
    Leer precio_kilo

    Escribir ""
    Escribir "=== Costo de las cajas de mango ==="
    Para i <- 1 Hasta 5 Hacer
        Si cajas[i] = 20 Entonces
            descuento <- 0.10
        Sino
            Si cajas[i] = 50 Entonces
                descuento <- 0.25
            Sino
                Si cajas[i] = 100 Entonces
                    descuento <- 0.50
                Sino
                    descuento <- 0.0
                FinSi
            FinSi
        FinSi
        costo <- cajas[i] * precio_kilo * (1 - descuento)
        Escribir "Caja de ", cajas[i], " kg: $ ", costo
    FinPara
FinAlgoritmo
