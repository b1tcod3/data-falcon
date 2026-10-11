# Ejercicio de seleccion multiple: central telefonica
#
# Una central telefónica cobra por las llamadas de larga distancia según el
# indicativo de la ciudad de destino:
#   indicativo 1 -> Bogotá (tarifa $50 por minuto)
#   indicativo 2 -> Cali (tarifa $70 por minuto)
#   indicativo 4 -> Medellín (tarifa $100 por minuto)
#   indicativo 5 -> Barranquilla (tarifa $160 por minuto)
#   indicativo 6 -> Pereira (tarifa $180 por minuto)
#   indicativo 7 -> Cúcuta (tarifa $190 por minuto)
#
# Datos de entrada: indicativo y número de minutos
# Datos de salida: ciudad, tarifa y valor total de la llamada


TARIFAS = {
    1: ("Bogotá", 50.0),
    2: ("Cali", 70.0),
    4: ("Medellín", 100.0),
    5: ("Barranquilla", 160.0),
    6: ("Pereira", 180.0),
    7: ("Cúcuta", 190.0),
}


def costo_llamada(indicativo, minutos):
    """Retorna (ciudad, tarifa, valor_total) o None si el indicativo no existe."""
    info = TARIFAS.get(indicativo)
    if info is None:
        return None

    ciudad, tarifa = info
    return ciudad, tarifa, tarifa * minutos


def main():
    indicativo = int(input("Indicativo de la ciudad (1, 2, 4, 5, 6 o 7): "))
    minutos = float(input("Número de minutos: "))

    resultado = costo_llamada(indicativo, minutos)

    if resultado is None:
        print("\nIndicativo no contemplado en la central.")
        return

    ciudad, tarifa, valor_total = resultado
    print(f"\nCiudad: {ciudad}")
    print(f"Tarifa por minuto: $ {tarifa:,.2f}")
    print(f"Valor total de la llamada: $ {valor_total:,.2f}")


if __name__ == "__main__":
    main()