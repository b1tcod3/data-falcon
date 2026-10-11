// Ejercicio secuencial: distribucion de un terreno (version PSeInt)
//
// Un terreno se distribuye asi: 40% en cultivos, 25% en viviendas, 15% en
// zonas verdes y el resto queda en otros usos. Se calcula e imprime el area
// en metros cuadrados de cada una de las partes.

Algoritmo TerrenoPolitico
    Definir area_total Como Real
    Definir cultivos, viviendas, zonas_verdes, otros Como Real
    Definir porc_cultivos, porc_viviendas, porc_zonas_verdes Como Real

    porc_cultivos <- 0.40
    porc_viviendas <- 0.25
    porc_zonas_verdes <- 0.15

    Escribir "Area total del terreno (m2):"
    Leer area_total

    cultivos <- area_total * porc_cultivos
    viviendas <- area_total * porc_viviendas
    zonas_verdes <- area_total * porc_zonas_verdes
    otros <- area_total - cultivos - viviendas - zonas_verdes

    Escribir ""
    Escribir "=== Distribucion del terreno ==="
    Escribir "Cultivos (40%): ", cultivos, " m2"
    Escribir "Viviendas (25%): ", viviendas, " m2"
    Escribir "Zonas verdes (15%): ", zonas_verdes, " m2"
    Escribir "Otros usos: ", otros, " m2"
FinAlgoritmo
