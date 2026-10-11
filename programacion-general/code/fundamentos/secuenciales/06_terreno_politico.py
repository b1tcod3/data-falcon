# Ejercicio secuencial: distribucion de un terreno
#
# Un terreno de cierta extensión se distribuye de la siguiente manera:
#   - 40% en cultivos
#   - 25% en viviendas
#   - 15% en zonas verdes
#   - el resto queda en otros usos
# Se pide calcular e imprimir el área en metros cuadrados de cada una de las
# cinco partes.
#
# Datos de entrada: area_total (metros cuadrados)
# Datos de salida: area de cultivos, viviendas, zonas verdes y otros


PORC_CULTIVOS = 0.40
PORC_VIVIENDAS = 0.25
PORC_ZONAS_VERDES = 0.15


def distribuir_terreno(area_total):
    """Retorna las areas de cultivos, viviendas, zonas verdes y otros usos."""
    cultivos = area_total * PORC_CULTIVOS
    viviendas = area_total * PORC_VIVIENDAS
    zonas_verdes = area_total * PORC_ZONAS_VERDES
    otros = area_total - cultivos - viviendas - zonas_verdes
    return cultivos, viviendas, zonas_verdes, otros


def main():
    area_total = float(input("Área total del terreno (m²): "))

    cultivos, viviendas, zonas_verdes, otros = distribuir_terreno(area_total)

    print("\n=== Distribución del terreno ===")
    print(f"Cultivos (40%): {cultivos:,.2f} m²")
    print(f"Viviendas (25%): {viviendas:,.2f} m²")
    print(f"Zonas verdes (15%): {zonas_verdes:,.2f} m²")
    print(f"Otros usos: {otros:,.2f} m²")


if __name__ == "__main__":
    main()