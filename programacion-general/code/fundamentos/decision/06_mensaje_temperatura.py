# Ejercicio de decision: mensaje segun la temperatura
#
# Según la temperatura del día se imprime un mensaje:
#   - "Hace frío"  si la temperatura es menor a 23 °C
#   - "Buen día"   si la temperatura está entre 23 °C (incluido) y 30 °C
#   - "Hace calor" si la temperatura es igual o mayor a 30 °C
#
# Datos de entrada: temperatura
# Datos de salida: mensaje del clima


LIMITE_FRIO = 23.0
LIMITE_CALOR = 30.0


def mensaje_clima(temperatura):
    """Retorna el mensaje según el rango de temperatura."""
    if temperatura < LIMITE_FRIO:
        return "Hace frío"
    if temperatura < LIMITE_CALOR:
        return "Buen día"
    return "Hace calor"


def main():
    temperatura = float(input("Temperatura del día (°C): "))

    print(f"\n{mensaje_clima(temperatura)}")


if __name__ == "__main__":
    main()