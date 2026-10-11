# tests/test_calculos.py - pruebas del convenio de viajes
#
# Ejecutar desde la carpeta del proyecto con:
#   python -m pytest tests/test_calculos.py

import pytest

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


def aproximado(esperado, obtenido):
    return abs(esperado - obtenido) < 1e-6


def test_buscar_plan_encuentra_el_plan_correcto():
    plan = buscar_plan("P_1")
    assert plan is not None
    assert plan["ciudad"] == "San Andrés"
    assert aproximado(plan["distancia_km"], 974.0)


def test_buscar_plan_devuelve_none_con_codigo_invalido():
    assert buscar_plan("P_99") is None


def test_trimestre_del_mes():
    assert trimestre_del_mes(2) == "primer"
    assert trimestre_del_mes(6) == "segundo"
    assert trimestre_del_mes(9) == "tercer"
    assert trimestre_del_mes(12) == "cuarto"
    assert trimestre_del_mes(0) is None


@pytest.mark.parametrize(
    "tipo, grupos, esperado",
    [
        ("Privada", 3, 0.000),
        ("Privada", 5, 0.000),
        ("Privada", 7, 0.035),
        ("Privada", 10, 0.035),
        ("Privada", 12, 0.085),
        ("Pública", 4, 0.0255),
        ("Pública", 8, 0.075),
        ("Pública", 15, 0.080),
    ],
)
def test_porcentaje_descuento(tipo, grupos, esperado):
    assert aproximado(porcentaje_descuento(tipo, grupos), esperado)


def test_porcentaje_descuento_tipo_invalido():
    assert porcentaje_descuento("Mixta", 3) is None


def test_valores_financieros_del_viaje():
    inicial = valor_inicial_pesos(500.0, 2000.0)
    assert aproximado(inicial, 1_000_000.0)

    descuento = valor_descuento_pesos(inicial, 0.08)
    assert aproximado(descuento, 80_000.0)

    real = valor_real_pesos(inicial, descuento)
    assert aproximado(real, 920_000.0)

    dolares = valor_real_dolares(real, 4000.0)
    assert aproximado(dolares, 230.0)


def test_conversion_distancias():
    pies, brazas, leguas, millas = conversion_distancias(1.609)

    assert aproximado(pies, 1609 / 0.3084)
    assert aproximado(brazas, (1609 / 0.3084) / 6)
    assert aproximado(leguas, 1609 / 5572.7)
    assert aproximado(millas, 1.0)


def test_liquidar_dinero():
    devuelto, alcanza = liquidar_dinero(1_000_000.0, 920_000.0)
    assert aproximado(devuelto, 80_000.0)
    assert alcanza is True


def test_liquidar_dinero_no_alcanza():
    devuelto, alcanza = liquidar_dinero(500_000.0, 920_000.0)
    assert devuelto < 0
    assert alcanza is False