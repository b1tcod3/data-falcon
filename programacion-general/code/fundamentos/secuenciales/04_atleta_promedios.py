# Ejercicio secuencial: atleta y promedios de entrenamiento
#
# Un atleta mide el tiempo (en minutos) y la distancia (en metros) en sus
# tres días de entrenamiento. Al final quiere saber el total de tiempo, la
# distancia total recorrida, el tiempo promedio y la distancia promedio.
#
# Datos de entrada: tiempo y distancia de cada uno de los 3 días
# Datos de salida: totales y promedios


DIAS = 3


def totales_y_promedios(tiempos, distancias):
    """Calcula totales y promedios de tiempo y distancia."""
    total_tiempo = sum(tiempos)
    total_distancia = sum(distancias)

    promedio_tiempo = total_tiempo / len(tiempos)
    promedio_distancia = total_distancia / len(distancias)

    return total_tiempo, total_distancia, promedio_tiempo, promedio_distancia


def main():
    tiempos = []
    distancias = []

    for dia in range(1, DIAS + 1):
        tiempo = float(input(f"Tiempo día {dia} (minutos): "))
        distancia = float(input(f"Distancia día {dia} (metros): "))
        tiempos.append(tiempo)
        distancias.append(distancia)

    total_tiempo, total_distancia, prom_tiempo, prom_distancia = (
        totales_y_promedios(tiempos, distancias)
    )

    print("\n=== Resultados del entrenamiento ===")
    print(f"Tiempo total: {total_tiempo:,.2f} minutos")
    print(f"Distancia total: {total_distancia:,.2f} metros")
    print(f"Tiempo promedio por día: {prom_tiempo:,.2f} minutos")
    print(f"Distancia promedio por día: {prom_distancia:,.2f} metros")


if __name__ == "__main__":
    main()