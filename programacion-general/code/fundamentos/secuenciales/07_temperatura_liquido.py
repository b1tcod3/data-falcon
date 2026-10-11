# Ejercicio secuencial: temperatura de un liquido
#
# Un líquido se somete a tres cambios de temperatura:
#   1. aumenta un 43% con respecto a la inicial
#   2. disminuye un 35% con respecto a la temperatura resultante
#   3. aumenta un 150% con respecto a la temperatura resultante
# Se pide calcular e imprimir la temperatura final y los cambios aplicados.
#
# Datos de entrada: temperatura_inicial
# Datos de salida: temperatura en cada etapa y temperatura final


AUMENTO_1 = 0.43
DISMINUCION = 0.35
AUMENTO_2 = 1.50


def cambios_temperatura(temp_inicial):
    """Aplica los tres cambios de temperatura en cadena."""
    despues_aumento_1 = temp_inicial * (1 + AUMENTO_1)
    despues_disminucion = despues_aumento_1 * (1 - DISMINUCION)
    temperatura_final = despues_disminucion * (1 + AUMENTO_2)

    return despues_aumento_1, despues_disminucion, temperatura_final


def main():
    temp_inicial = float(input("Temperatura inicial (°C): "))

    etapa_1, etapa_2, temp_final = cambios_temperatura(temp_inicial)

    print("\n=== Cambios de temperatura ===")
    print(f"Temperatura inicial: {temp_inicial:,.2f} °C")
    print(f"Tras +43%: {etapa_1:,.2f} °C")
    print(f"Tras -35%: {etapa_2:,.2f} °C")
    print(f"Temperatura final (+150%): {temp_final:,.2f} °C")


if __name__ == "__main__":
    main()