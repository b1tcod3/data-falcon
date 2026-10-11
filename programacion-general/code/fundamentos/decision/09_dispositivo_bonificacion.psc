// Ejercicio de decision: bonificacion de un dispositivo (version PSeInt)
//
// Segun el monto de la bonificacion el empleado puede comprar:
//   menor a $50,000                       -> camara web
//   entre $50,000 y $200,000              -> subwoofer
//   mas de $200,000 y hasta $500,000      -> disco duro externo
//   mas de $500,000 y hasta $1'000,000    -> impresora multifuncional
//   mas de $1'000,000                     -> proyector

Algoritmo DispositivoBonificacion
    Definir bonificacion Como Real

    Escribir "Valor de la bonificacion:"
    Leer bonificacion

    Escribir ""
    Si bonificacion < 50000 Entonces
        Escribir "El empleado puede comprar un(a) camara web."
    Sino
        Si bonificacion <= 200000 Entonces
            Escribir "El empleado puede comprar un(a) subwoofer."
        Sino
            Si bonificacion <= 500000 Entonces
                Escribir "El empleado puede comprar un(a) disco duro externo."
            Sino
                Si bonificacion <= 1000000 Entonces
                    Escribir "El empleado puede comprar un(a) impresora multifuncional."
                Sino
                    Escribir "El empleado puede comprar un(a) proyector."
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
