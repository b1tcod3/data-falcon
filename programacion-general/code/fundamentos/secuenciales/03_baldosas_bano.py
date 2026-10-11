# Ejercicio secuencial: baldosas del bano
#
# El propietario de una vivienda necesita renovar su baño. Se mide el alto y
# el largo de los muros y se pide calcular e imprimir el área total del baño
# y el número de cajas de baldosas necesarias para cubrirla, sabiendo que
# cada caja trae 3.5 metros cuadrados.
#
# Datos de entrada: alto, largo (en metros)
# Datos de salida: area_total, cajas_necesarias


import math

METROS_POR_CAJA = 3.5


def area_y_cajas(alto, largo):
    """Retorna el area del muro y las cajas de baldosas necesarias."""
    area = alto * largo
    cajas = math.ceil(area / METROS_POR_CAJA)
    return area, cajas


def main():
    alto = float(input("Alto del muro (metros): "))
    largo = float(input("Largo del muro (metros): "))

    area, cajas = area_y_cajas(alto, largo)

    print(f"\nÁrea total del baño: {area:,.2f} m²")
    print(f"Cajas de baldosas necesarias: {cajas}")


if __name__ == "__main__":
    main()