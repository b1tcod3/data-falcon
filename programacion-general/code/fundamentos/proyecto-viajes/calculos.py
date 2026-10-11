# calculos.py - logica del convenio de viajes Decameron / Avianca
#
# Este módulo concentra los cálculos del convenio: búsqueda del plan,
# trimestre según el mes, porcentaje de descuento, valoración del viaje,
# conversión de unidades y liquidación del dinero entregado.
#
# Todos los valores monetarios se manejan en pesos colombianos salvo que se
# indique lo contrario (por ejemplo, el valor en dólares).

from planes import (
    PLANES,
    DESCUENTOS,
    TRIMESTRES,
    METROS_POR_PIE,
    PIES_POR_BRAZA,
    METROS_POR_LEGUA,
    KILOMETROS_POR_MILLA,
)


def buscar_plan(codigo):
    """Retorna el plan que coincide con el código o None si no existe."""
    for plan in PLANES:
        if plan["codigo"] == codigo:
            return plan
    return None


def trimestre_del_mes(mes):
    """Retorna la palabra del trimestre (primer, segundo, tercer o cuarto)."""
    return TRIMESTRES.get(mes)


def porcentaje_descuento(tipo_empresa, num_grupos):
    """Retorna el porcentaje de descuento según el tipo de empresa y grupos."""
    for regla in DESCUENTOS:
        if regla["tipo"] != tipo_empresa:
            continue

        dentro_del_minimo = num_grupos >= regla["min_grupos"]
        maximo = regla["max_grupos"]
        dentro_del_maximo = maximo is None or num_grupos <= maximo

        if dentro_del_minimo and dentro_del_maximo:
            return regla["descuento"]
    return None


def valor_inicial_pesos(distancia_km, valor_km):
    """Calcula el valor inicial del viaje: distancia por valor del kilómetro."""
    return distancia_km * valor_km


def valor_descuento_pesos(valor_inicial, porcentaje):
    """Calcula cuánto se descuenta del valor inicial."""
    return valor_inicial * porcentaje


def valor_real_pesos(valor_inicial, descuento_pesos):
    """Calcula el valor final después de aplicar el descuento."""
    return valor_inicial - descuento_pesos


def valor_real_dolares(valor_pesos, trm):
    """Convierte un valor en pesos a dólares según la TRM."""
    return valor_pesos / trm


def conversion_distancias(km):
    """Convierte kilómetros a pies, brazas, leguas y millas."""
    metros = km * 1000

    pies = metros / METROS_POR_PIE
    brazas = pies / PIES_POR_BRAZA
    leguas = metros / METROS_POR_LEGUA
    millas = km / KILOMETROS_POR_MILLA

    return pies, brazas, leguas, millas


def liquidar_dinero(entregado, valor_real):
    """Retorna el dinero devuelto y si el valor entregado alcanza."""
    devuelto = entregado - valor_real
    alcanza = devuelto >= 0
    return devuelto, alcanza