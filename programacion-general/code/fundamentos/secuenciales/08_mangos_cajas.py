# Ejercicio secuencial: mangos en cajas
#
# El kilogramo de mango tiene un precio establecido. Al venderlo por cajas se
# aplican descuentos según el tamaño:
#   - caja de 6 kg       -> sin descuento
#   - caja de 10 kg      -> sin descuento
#   - caja de 20 kg      -> 10% de descuento
#   - caja de 50 kg      -> 25% de descuento
#   - caja de 100 kg     -> se paga la mitad del precio
# Se pide mostrar el costo de cada tipo de caja.
#
# Datos de entrada: precio_por_kilo
# Datos de salida: costo de cada caja (6, 10, 20, 50 y 100 kg)


CAJAS_KG = [6, 10, 20, 50, 100]
DESCUENTO_20 = 0.10
DESCUENTO_50 = 0.25


def costo_cajas(precio_kilo):
    """Retorna el costo de cada caja segun el descuento aplicado."""
    costos = {}
    for kg in CAJAS_KG:
        if kg == 20:
            descuento = DESCUENTO_20
        elif kg == 50:
            descuento = DESCUENTO_50
        elif kg == 100:
            descuento = 0.50
        else:
            descuento = 0.0

        costo = kg * precio_kilo * (1 - descuento)
        costos[kg] = costo

    return costos


def main():
    precio_kilo = float(input("Precio por kilogramo de mango: "))

    costos = costo_cajas(precio_kilo)

    print("\n=== Costo de las cajas de mango ===")
    for kg in CAJAS_KG:
        print(f"Caja de {kg} kg: $ {costos[kg]:,.2f}")


if __name__ == "__main__":
    main()