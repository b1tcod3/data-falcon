# planes.py - datos del convenio de viajes Decameron / Avianca
#
# Este módulo contiene únicamente los datos del convenio: los planes de
# viaje disponibles, la tabla de descuentos según el tipo de empresa y el
# número de grupos, y las equivalencias de unidades para el reporte.
#
# La distancia de cada plan está expresada en kilómetros (dato suministrado
# por el convenio).

PLANES = [
    {"codigo": "P_1", "ciudad": "San Andrés", "distancia_km": 974.0},
    {"codigo": "P_2", "ciudad": "Cartagena", "distancia_km": 460.74},
    {"codigo": "P_3", "ciudad": "Barranquilla", "distancia_km": 535.41},
    {"codigo": "P_4", "ciudad": "Aruba", "distancia_km": 559.28},
    {"codigo": "P_5", "ciudad": "Tolú", "distancia_km": 364.52},
    {"codigo": "P_6", "ciudad": "Santa Marta", "distancia_km": 578.4},
]

# Tabla de descuentos. La escala del convenio usa los rangos "entre 1 y 5",
# "entre 5 y 10" y "más de 10" grupos; para evitar la superposición en el
# valor 5 se interpretan como [1,5], (5,10] y (10, en adelante).
DESCUENTOS = [
    {"tipo": "Privada", "min_grupos": 1, "max_grupos": 5, "descuento": 0.000},
    {"tipo": "Privada", "min_grupos": 6, "max_grupos": 10, "descuento": 0.035},
    {"tipo": "Privada", "min_grupos": 11, "max_grupos": None, "descuento": 0.085},
    {"tipo": "Pública", "min_grupos": 1, "max_grupos": 5, "descuento": 0.0255},
    {"tipo": "Pública", "min_grupos": 6, "max_grupos": 10, "descuento": 0.075},
    {"tipo": "Pública", "min_grupos": 11, "max_grupos": None, "descuento": 0.080},
]

TRIMESTRES = {
    1: "primer", 2: "primer", 3: "primer",
    4: "segundo", 5: "segundo", 6: "segundo",
    7: "tercer", 8: "tercer", 9: "tercer",
    10: "cuarto", 11: "cuarto", 12: "cuarto",
}

# Equivalencias de unidades suministradas por el convenio.
METROS_POR_PIE = 0.3084
PIES_POR_BRAZA = 6
METROS_POR_LEGUA = 5572.7
KILOMETROS_POR_MILLA = 1.609