# Ejercicio de seleccion multiple: creditos por plazos
#
# Un almacén otorga créditos a sus clientes. Según el plazo (en meses) el
# cliente recibe un artículo:
#   - 48 meses -> Computadora
#   - 36 meses -> Televisor de 42 pulgadas
#   - 24 meses -> BlackBerry
#   - 12 meses -> Cámara digital
#   - 6 meses  -> Impresora
#
# Datos de entrada: plazo en meses
# Datos de salida: artículo otorgado


ARTICULOS = {48: "Computadora", 36: "Televisor de 42 pulgadas", 24: "BlackBerry", 12: "Cámara digital", 6: "Impresora"}


def articulo_por_plazo(plazo):
    """Retorna el artículo según el número de meses o None si no existe."""
    return ARTICULOS.get(plazo)


def main():
    plazo = int(input("Ingrese el plazo en meses (48, 36, 24, 12 o 6): "))

    articulo = articulo_por_plazo(plazo)

    if articulo is None:
        print("\nPlazo no contemplado en el almacén.")
    else:
        print(f"\nCon {plazo} meses recibe: {articulo}")


if __name__ == "__main__":
    main()