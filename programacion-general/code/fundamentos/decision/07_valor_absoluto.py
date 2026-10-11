# Ejercicio de decision: valor absoluto
#
# Dado un número entero, calcular e imprimir su valor absoluto.
#
# Datos de entrada: numero
# Datos de salida: valor absoluto del número


def valor_absoluto(numero):
    """Retorna el valor absoluto usando una condición."""
    if numero < 0:
        return -numero
    return numero


def main():
    numero = int(input("Ingrese un número entero (puede ser negativo): "))

    print(f"\nValor absoluto: {valor_absoluto(numero)}")


if __name__ == "__main__":
    main()