# Ejercicio de seleccion multiple: extensiones telefonicas
#
# Una empresa tiene asignadas las siguientes extensiones para sus empleados:
#   ext 750 -> funcionalidad de calidad
#   ext 751 -> calidad
#   ext 752 -> control total de calidad
#   ext 753 -> recursos humanos
#   ext 754 -> bienestar laboral
#   ext 755 -> sistema de compras
#   ext 756 -> sistemas
#   ext 757 -> mantenimiento de software
#   ext 758 -> inventarios
#   ext 759 -> caja de compensación
#   ext 760 -> contabilidad
#   ext 780 -> gerencia
#
# Datos de entrada: extension
# Datos de salida: nombre del encargado de la extensión
#
# Nota: se modela la dependencia; los nombres de los encargados no fueron
# suministrados, por lo que se imprime la dependencia asignada.


EXTENSIONES = {
    750: "funcionalidad de calidad",
    751: "calidad",
    752: "control total de calidad",
    753: "recursos humanos",
    754: "bienestar laboral",
    755: "sistema de compras",
    756: "sistemas",
    757: "mantenimiento de software",
    758: "inventarios",
    759: "caja de compensación",
    760: "contabilidad",
    780: "gerencia",
}


def encargado_extension(extension):
    """Retorna la dependencia de la extensión o None si no existe."""
    return EXTENSIONES.get(extension)


def main():
    extension = int(input("Ingrese la extensión (750 a 760 o 780): "))

    encargado = encargado_extension(extension)

    if encargado is None:
        print("\nExtensión no asignada o inexistente.")
    else:
        print(f"\nLa extensión {extension} pertenece a: {encargado}")


if __name__ == "__main__":
    main()