# Ejercicio secuencial: computadora que procesa tres numeros
#
# Una computadora realiza las siguientes acciones: solicita tres números al
# usuario y muestra la suma de estos números; luego muestra la división de la
# suma de los dos primeros entre la resta de los dos últimos; y finalmente
# muestra la multiplicación de los resultados de la suma y la división.
#
# Datos de entrada: num1, num2, num3
# Datos de salida: suma, division, producto
#
# Nota: la resta de los dos ultimos se interpreta como num2 - num3.


def procesar_numeros(num1, num2, num3):
    """Retorna (suma, division, producto) siguiendo las acciones pedidas."""
    suma = num1 + num2 + num3
    resta = num2 - num3
    division = (num1 + num2) / resta
    producto = suma * division
    return suma, division, producto


def main():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    num3 = float(input("Tercer número: "))

    suma, division, producto = procesar_numeros(num1, num2, num3)

    print(f"\nSuma de los tres números: {suma:,.2f}")
    print(f"División (num1 + num2) / (num2 - num3): {division:,.2f}")
    print(f"Producto suma * división: {producto:,.2f}")


if __name__ == "__main__":
    main()