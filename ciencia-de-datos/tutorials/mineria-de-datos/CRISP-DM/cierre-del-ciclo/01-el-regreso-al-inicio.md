# El Regreso al Inicio

Sin importar si el despliegue es exitoso o si la evaluación previa revela que los resultados de laboratorio no son suficientes para salir a producción, el proceso CRISP-DM siempre tiende a regresar a la fase de **Comprensión del Negocio**.

## ¿Por qué volver al inicio?

Cada etapa completada aporta un conocimiento profundo sobre:

- Las **dificultades reales** del problema de negocio.
- La **estructura y limitaciones** de la información disponible.
- Los **sesgos y supuestos** que no se identificaron al principio.
- Las **oportunidades** que no eran evidentes antes del análisis.

Este aprendizaje acumulativo hace que la segunda iteración del ciclo sea invariablemente mejor que la primera. El equipo llega a la Comprensión del Negocio con un conocimiento que no tenía cuando empezó.

## Los shortcuts del diagrama

El diagrama de CRISP-DM incluye intencionalmente accesos directos (*shortcuts*) de retorno entre prácticamente todas las etapas, garantizando la flexibilidad necesaria para reajustar definiciones o adquirir nuevos datos ante cualquier descubrimiento sobre la marcha.

```
Entendimiento del Negocio ←──┐
         ↓                    │
Entendimiento de los Datos ←──┤
         ↓                    │
Preparación de los Datos ←────┤
         ↓                    │
Modelado ←────────────────────┤
         ↓                    │
Evaluación ←──────────────────┤
         ↓                    │
Despliegue ───────────────────┘
```

No es un fracaso regresar a una fase anterior. Es la naturaleza del proceso científico aplicado a problemas de negocio.

## El ciclo virtuoso

Cada iteración del ciclo CRISP-DM:

1. **Refina** la definición del problema.
2. **Mejora** la calidad de los datos.
3. **Ajusta** los modelos a la realidad cambiante.
4. **Aumenta** el valor generado para el negocio.

El fin de un ciclo no es el final del proyecto, sino el comienzo del siguiente, ahora con un equipo mucho más informado que al principio.
