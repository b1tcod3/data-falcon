# Ejercicio de decision: cuadrado condicional
#
# Calcular el cuadrado de un número solo si este es igual a 10, 20, 30 o 40;
# en caso contrario el resultado debe ser cero.
#
# Datos de entrada: numero
# Datos de salida: cuadrado del número o cero


CANDIDATOS = (10, 20, 30, 40)


def calcular_cuadrado(numero):
    """Retorna el cuadrado si el numero esta en la lista, si no, cero."""
    if numero in CANDIDATOS:
        return numero ** 2
    return 0


def main():
    numero = float(input("Ingrese un número (opciones: 10, 20, 30 o 40): "))

    cuadrado = calcular_cuadrado(numero)

    print(f"\nResultado: {cuadrado:,.2f}")


if __name__ == "__main__":
    main()