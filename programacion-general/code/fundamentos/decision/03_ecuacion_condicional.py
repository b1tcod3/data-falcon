# Ejercicio de decision: ecuacion condicional
#
# Dado un valor r se pide hallar el resultado de la ecuación:
#   P = (r - 2) ** 3   si r es diferente de 2
#   P = 1              si r es igual a 2
#
# Datos de entrada: r
# Datos de salida: valor de P


def resultado_ecuacion(r):
    """Calcula P según la condición sobre r."""
    if r != 2:
        return (r - 2) ** 3
    return 1


def main():
    r = float(input("Ingrese el valor de r: "))

    p = resultado_ecuacion(r)

    print(f"\nEl valor de P es: {p:,.2f}")


if __name__ == "__main__":
    main()