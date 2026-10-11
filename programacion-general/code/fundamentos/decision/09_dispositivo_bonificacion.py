# Ejercicio de decision: bonificacion de un dispositivo
#
# Una empresa decide entregar una bonificación en dinero a sus empleados.
# Con esa bonificación el empleado puede comprar un dispositivo según el
# valor recibido:
#   - menor a $50,000          -> cámara web
#   - entre $50,000 y $200,000 -> subwoofer
#   - más de $200,000 y hasta $500,000 -> disco duro externo
#   - más de $500,000 y hasta $1'000,000 -> impresora multifuncional
#   - más de $1'000,000        -> proyector
#
# Datos de entrada: bonificacion
# Datos de salida: dispositivo que puede adquirir


def dispositivo_por_bonificacion(bonificacion):
    """Retorna el dispositivo según el monto de la bonificación."""
    if bonificacion < 50_000:
        return "cámara web"
    if bonificacion <= 200_000:
        return "subwoofer"
    if bonificacion <= 500_000:
        return "disco duro externo"
    if bonificacion <= 1_000_000:
        return "impresora multifuncional"
    return "proyector"


def main():
    bonificacion = float(input("Valor de la bonificación: "))

    print(f"\nEl empleado puede comprar un(a) {dispositivo_por_bonificacion(bonificacion)}.")


if __name__ == "__main__":
    main()