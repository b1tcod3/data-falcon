# main.py - interfaz interactiva del convenio de viajes Decameron / Avianca
#
# Recibe los datos del usuario (código del plan, tipo de empresa, número de
# grupos, dinero entregado, mes, valor por kilómetro y TRM) y muestra el
# reporte completo de la liquidación del viaje.

from calculos import (
    buscar_plan,
    trimestre_del_mes,
    porcentaje_descuento,
    valor_inicial_pesos,
    valor_descuento_pesos,
    valor_real_pesos,
    valor_real_dolares,
    conversion_distancias,
    liquidar_dinero,
)

TIPOS_EMPRESA = ("Privada", "Pública")


def pedir_tipo_empresa():
    """Pide el tipo de empresa y lo normaliza a las opciones del convenio."""
    tipo = input("Tipo de empresa (Privada/Pública): ").strip().capitalize()
    if tipo not in TIPOS_EMPRESA:
        raise ValueError("El tipo de empresa debe ser Privada o Pública.")
    return tipo


def main():
    print("=== Convenio de viajes Decamerón / Avianca ===")

    codigo = input("Código del plan (P_1 a P_6): ").strip()
    plan = buscar_plan(codigo)
    if plan is None:
        print("Código de plan no válido.")
        return

    try:
        tipo_empresa = pedir_tipo_empresa()
        num_grupos = int(input("Número de grupos: "))
        mes = int(input("Mes de salida (1 a 12): "))
        valor_km = float(input("Valor de cada kilómetro: "))
        dinero_entregado = float(input("Dinero entregado por el cliente: "))
        trm = float(input("TRM (valor del dólar): "))

        porcentaje = porcentaje_descuento(tipo_empresa, num_grupos)
        trimestre = trimestre_del_mes(mes)
        if porcentaje is None:
            print("No existe descuento para los datos ingresados.")
            return
        if trimestre is None:
            print("El mes debe estar entre 1 y 12.")
            return
    except ValueError:
        print("Dato inválido. Verifique que escribió números correctamente.")
        return

    distancia_km = plan["distancia_km"]

    inicial = valor_inicial_pesos(distancia_km, valor_km)
    descuento = valor_descuento_pesos(inicial, porcentaje)
    real_pesos = valor_real_pesos(inicial, descuento)
    real_dolares = valor_real_dolares(real_pesos, trm)
    devuelto, alcanza = liquidar_dinero(dinero_entregado, real_pesos)
    pies, brazas, leguas, millas = conversion_distancias(distancia_km)

    print("\n=== Reporte de la liquidación ===")
    print(f"Ciudad de destino: {plan['ciudad']}")
    print(f"Código del plan: {codigo}")
    print(f"Distancia: {distancia_km:,.2f} km")
    print(f"Trimestre de salida: {trimestre} trimestre")
    print(f"Tipo de empresa: {tipo_empresa} - grupos: {num_grupos}")
    print(f"Descuento aplicado: {porcentaje * 100:.2f}%")
    print(f"Valor inicial del viaje: $ {inicial:,.2f}")
    print(f"Valor del descuento: $ {descuento:,.2f}")
    print(f"Valor real en pesos: $ {real_pesos:,.2f}")
    print(f"Valor real en dólares: US$ {real_dolares:,.2f}")
    print(f"Dinero entregado: $ {dinero_entregado:,.2f}")
    print(f"Dinero devuelto: $ {devuelto:,.2f}")
    print(f"¿Alcanza el dinero entregado?: {'Sí' if alcanza else 'No'}")

    print("\n=== Conversión de la distancia ===")
    print(f"Pies: {pies:,.2f}")
    print(f"Brazas: {brazas:,.2f}")
    print(f"Leguas: {leguas:,.2f}")
    print(f"Millas: {millas:,.2f}")


if __name__ == "__main__":
    main()