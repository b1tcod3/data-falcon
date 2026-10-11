# Ejercicio secuencial: conversiones de un gimnasio
#
# Una persona tiene un peso inicial. Para ingresar al gimnasio se aplican dos
# cambios sucesivos: primero el peso disminuye un 28.5% y luego aumenta un 5%
# con respecto al peso resultante. El objetivo es expresar el peso final en
# las siguientes unidades:
#   - miligramos (1 kg = 1,000,000 mg)
#   - libras (1 kg = 2.2205 lb)
#   - onzas (1 lb = 16 onzas)
#   - quintales (1 quintal = 100 kg)
#
# Datos de entrada: peso_inicial (kg)
# Datos de salida: peso final en kg, mg, lb, onzas y quintales


DISMINUCION = 0.285
AUMENTO = 0.05
MG_POR_KG = 1_000_000
LB_POR_KG = 2.2205
ONZAS_POR_LB = 16
KG_POR_QUINTAL = 100


def peso_final(peso_inicial):
    """Aplica la disminucion del 28.5% y el aumento del 5%."""
    peso_tras_bajar = peso_inicial * (1 - DISMINUCION)
    return peso_tras_bajar * (1 + AUMENTO)


def convertir_unidades(peso_kg):
    """Convierte un peso en kg a mg, lb, onzas y quintales."""
    miligramos = peso_kg * MG_POR_KG
    libras = peso_kg * LB_POR_KG
    onzas = libras * ONZAS_POR_LB
    quintales = peso_kg / KG_POR_QUINTAL

    return miligramos, libras, onzas, quintales


def main():
    peso_inicial = float(input("Peso inicial (kg): "))

    peso = peso_final(peso_inicial)
    miligramos, libras, onzas, quintales = convertir_unidades(peso)

    print("\n=== Peso final y sus equivalentes ===")
    print(f"Kilogramos: {peso:,.2f} kg")
    print(f"Miligramos: {miligramos:,.2f} mg")
    print(f"Libras: {libras:,.2f} lb")
    print(f"Onzas: {onzas:,.2f} onzas")
    print(f"Quintales: {quintales:,.4f} quintales")


if __name__ == "__main__":
    main()