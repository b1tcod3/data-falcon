// Ejercicio secuencial: baldosas del bano (version PSeInt)
//
// Se mide el alto y el largo de los muros y se calcula e imprime el area
// total del bano y el numero de cajas de baldosas necesarias para cubrirla,
// sabiendo que cada caja trae 3.5 metros cuadrados.

Algoritmo BaldosasBano
    Definir alto, largo Como Real
    Definir area, cajas_exactas, cajas Como Real
    Definir metros_por_caja Como Real

    metros_por_caja <- 3.5

    Escribir "Alto del muro (metros):"
    Leer alto
    Escribir "Largo del muro (metros):"
    Leer largo

    area <- alto * largo
    cajas_exactas <- area / metros_por_caja

    // Techo (redondeo hacia arriba): si no es entero, se sube una caja.
    Si cajas_exactas = trunc(cajas_exactas) Entonces
        cajas <- trunc(cajas_exactas)
    Sino
        cajas <- trunc(cajas_exactas) + 1
    FinSi

    Escribir ""
    Escribir "Area total del bano: ", area, " m2"
    Escribir "Cajas de baldosas necesarias: ", cajas
FinAlgoritmo
