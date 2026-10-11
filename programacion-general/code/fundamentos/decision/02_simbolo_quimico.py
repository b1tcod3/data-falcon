# Ejercicio de decision: simbolos quimicos
#
# Dado el símbolo de un elemento químico imprimir su nombre:
#   - H -> Hidrógeno
#   - O -> Oxígeno
#   - N -> Nitrógeno
#   - otro símbolo -> "Elemento no contemplado"
#
# Datos de entrada: simbolo (carácter)
# Datos de salida: nombre del elemento o mensaje


SIMBOLOS = {"H": "Hidrógeno", "O": "Oxígeno", "N": "Nitrógeno"}


def nombre_elemento(simbolo):
    """Retorna el nombre del elemento o un mensaje por defecto."""
    if simbolo in SIMBOLOS:
        return SIMBOLOS[simbolo]
    return "Elemento no contemplado"


def main():
    simbolo = input("Ingrese el símbolo del elemento (H, O o N): ").upper()

    print(f"\n{nombre_elemento(simbolo)}")


if __name__ == "__main__":
    main()