# Ejercicio de decision: números en orden ascendente
#
# Dados dos números, mostrarlos en orden ascendente (de menor a mayor).
#
# Datos de entrada: num1, num2
# Datos de salida: los números en orden ascendente


def ordenar_ascendente(num1, num2):
    """Retorna la tupla (menor, mayor)."""
    if num1 < num2:
        return num1, num2
    return num2, num1


def main():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    menor, mayor = ordenar_ascendente(num1, num2)

    print(f"\nOrden ascendente: {menor:,.2f} - {mayor:,.2f}")


if __name__ == "__main__":
    main()