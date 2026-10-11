// main.psc - convenio de viajes Decameron / Avianca (version PSeInt)
//
// Version en pseudocodigo del proyecto final. Concentra los datos del
// convenio, la logica de calculo y el reporte de la liquidacion en un solo
// archivo, usando SubProcesos para las operaciones reutilizables.
//
// En Python el proyecto esta separado en planes.py, calculos.py y main.py;
// aqui todo vive en el mismo algoritmo porque PSeInt no tiene modulos.

Algoritmo ConvenioViajes
    Definir codigo, tipo_empresa, ciudad Como Caracter
    Definir num_grupos, mes, trimestre Como Entero
    Definir valor_km, dinero_entregado, trm Como Real
    Definir porcentaje, distancia_km, inicial, descuento Como Real
    Definir real_pesos, real_dolares, devuelto Como Real
    Definir alcanza Como Logico
    Definir pies, brazas, leguas, millas Como Real

    ciudad <- "Desconocida"
    distancia_km <- -1

    Escribir "=== Convenio de viajes Decameron / Avianca ==="
    Escribir "Codigo del plan (P_1 a P_6):"
    Leer codigo

    Segun codigo Hacer
        "P_1":
            ciudad <- "San Andres"
            distancia_km <- 974.0
        "P_2":
            ciudad <- "Cartagena"
            distancia_km <- 460.74
        "P_3":
            ciudad <- "Barranquilla"
            distancia_km <- 535.41
        "P_4":
            ciudad <- "Aruba"
            distancia_km <- 559.28
        "P_5":
            ciudad <- "Tolu"
            distancia_km <- 364.52
        "P_6":
            ciudad <- "Santa Marta"
            distancia_km <- 578.4
        De Otro Modo:
            distancia_km <- -1
    FinSegun

    Si distancia_km < 0 Entonces
        Escribir "Codigo de plan no valido."
    Sino
        Escribir "Tipo de empresa (Privada/Publica):"
        Leer tipo_empresa
        Escribir "Numero de grupos:"
        Leer num_grupos
        Escribir "Mes de salida (1 a 12):"
        Leer mes
        Escribir "Valor de cada kilometro:"
        Leer valor_km
        Escribir "Dinero entregado por el cliente:"
        Leer dinero_entregado
        Escribir "TRM (valor del dolar):"
        Leer trm

        trimestre <- trimestre_del_mes(mes)
        porcentaje <- porcentaje_descuento(tipo_empresa, num_grupos)

        Si trimestre = 0 Entonces
            Escribir "El mes debe estar entre 1 y 12."
        Sino
            Si porcentaje < 0 Entonces
                Escribir "No existe descuento para los datos ingresados."
            Sino
                inicial <- distancia_km * valor_km
                descuento <- inicial * porcentaje
                real_pesos <- inicial - descuento
                real_dolares <- real_pesos / trm
                devuelto <- dinero_entregado - real_pesos
                alcanza <- devuelto >= 0

                pies <- km_a_pies(distancia_km)
                brazas <- pies / 6
                leguas <- km_a_leguas(distancia_km)
                millas <- km_a_millas(distancia_km)

                Escribir ""
                Escribir "=== Reporte de la liquidacion ==="
                Escribir "Ciudad de destino: ", ciudad
                Escribir "Codigo del plan: ", codigo
                Escribir "Distancia: ", distancia_km, " km"
                Escribir "Trimestre de salida: ", nombre_trimestre(trimestre), " trimestre"
                Escribir "Tipo de empresa: ", tipo_empresa, " - grupos: ", num_grupos
                Escribir "Descuento aplicado: ", porcentaje * 100, "%"
                Escribir "Valor inicial del viaje: $ ", inicial
                Escribir "Valor del descuento: $ ", descuento
                Escribir "Valor real en pesos: $ ", real_pesos
                Escribir "Valor real en dolares: US$ ", real_dolares
                Escribir "Dinero entregado: $ ", dinero_entregado
                Escribir "Dinero devuelto: $ ", devuelto
                Si alcanza Entonces
                    Escribir "Alcanza el dinero entregado?: Si"
                Sino
                    Escribir "Alcanza el dinero entregado?: No"
                FinSi

                Escribir ""
                Escribir "=== Conversion de la distancia ==="
                Escribir "Pies: ", pies
                Escribir "Brazas: ", brazas
                Escribir "Leguas: ", leguas
                Escribir "Millas: ", millas
            FinSi
        FinSi
    FinSi
FinAlgoritmo

// Retorna el numero de trimestre (1 a 4) o 0 si el mes es invalido.
SubProceso n <- trimestre_del_mes(mes)
    Si mes >= 1 Y mes <= 3 Entonces
        n <- 1
    Sino
        Si mes >= 4 Y mes <= 6 Entonces
            n <- 2
        Sino
            Si mes >= 7 Y mes <= 9 Entonces
                n <- 3
            Sino
                Si mes >= 10 Y mes <= 12 Entonces
                    n <- 4
                Sino
                    n <- 0
                FinSi
            FinSi
        FinSi
    FinSi
FinSubProceso

// Retorna el porcentaje de descuento segun tipo de empresa y grupos, o -1
// si no existe descuento para los datos ingresados.
SubProceso p <- porcentaje_descuento(tipo_empresa, grupos)
    p <- -1
    Si Mayusculas(tipo_empresa) = "PRIVADA" Entonces
        Si grupos >= 1 Y grupos <= 5 Entonces
            p <- 0.0
        Sino
            Si grupos >= 6 Y grupos <= 10 Entonces
                p <- 0.035
            Sino
                Si grupos >= 11 Entonces
                    p <- 0.085
                FinSi
            FinSi
        FinSi
    Sino
        Si Mayusculas(tipo_empresa) = "PUBLICA" O Mayusculas(tipo_empresa) = "PÚBLICA" Entonces
            Si grupos >= 1 Y grupos <= 5 Entonces
                p <- 0.0255
            Sino
                Si grupos >= 6 Y grupos <= 10 Entonces
                    p <- 0.075
                Sino
                    Si grupos >= 11 Entonces
                        p <- 0.080
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinSubProceso

// 1 pie = 0.3084 m
SubProceso r <- km_a_pies(km)
    r <- (km * 1000) / 0.3084
FinSubProceso

// 1 legua = 5572.7 m
SubProceso r <- km_a_leguas(km)
    r <- (km * 1000) / 5572.7
FinSubProceso

// 1 milla = 1.609 km
SubProceso r <- km_a_millas(km)
    r <- km / 1.609
FinSubProceso

SubProceso nombre <- nombre_trimestre(n)
    Si n = 1 Entonces
        nombre <- "primer"
    Sino
        Si n = 2 Entonces
            nombre <- "segundo"
        Sino
            Si n = 3 Entonces
                nombre <- "tercer"
            Sino
                nombre <- "cuarto"
            FinSi
        FinSi
    FinSi
FinSubProceso
