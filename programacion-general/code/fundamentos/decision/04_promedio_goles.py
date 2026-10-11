# Ejercicio de decision: promedio de goles
#
# Un equipo de fútbol registra el número de goles anotados en cuatro
# encuentros. Se debe calcular e imprimir el promedio de goles solo si la
# suma de los goles es mayor que 10; en caso contrario se imprime que no se
# debe calcular el promedio.
#
# Datos de entrada: goles de los 4 encuentros
# Datos de salida: promedio de goles o mensaje


ENCUENTROS = 4
LIMITE_SUMA = 10


def promedio_goles(goles):
    """Retorna el promedio si la suma supera el límite, si no, None."""
    suma = sum(goles)
    if suma > LIMITE_SUMA:
        return suma / len(goles)
    return None


def main():
    goles = []
    for encuentro in range(1, ENCUENTROS + 1):
        goles.append(int(input(f"Goles del encuentro {encuentro}: ")))

    promedio = promedio_goles(goles)

    if promedio is None:
        print("\nLa suma no supera los 10 goles, no se pide calcular promedio.")
    else:
        print(f"\nPromedio de goles: {promedio:,.2f}")


if __name__ == "__main__":
    main()