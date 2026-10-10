# Árboles de Decisión y Reglas Lógicas

La solución para combinar múltiples atributos informativos es la **Segmentación Supervisada** a través de modelos estructurados en árbol. Los árboles de decisión son uno de los algoritmos más utilizados precisamente por su equilibrio entre potencia predictiva y transparencia.

## Inducción de Árboles de Decisión

### Divide y Vencerás (Recursividad)

El algoritmo sigue un proceso recursivo:

1. Elige el atributo con mayor ganancia de información para la población total y hace el primer corte (Nodo Raíz).
2. Toma cada subgrupo resultante y **repite el proceso de forma independiente**, evaluando nuevamente qué atributo es el mejor para ese subgrupo específico.
3. Continúa hasta que se cumple una condición de parada (pureza máxima, profundidad máxima, o mínimo de registros por hoja).

```
                 ¿Edad > 30?
                /            \
             Sí                No
              ↓                 ↓
        ¿Ingreso > 50k?    ¿Historial > 2 años?
         /        \           /         \
       Sí          No        Sí          No
    Lealtad    Riesgo    Lealtad     Riesgo
    (95%)      (40%)     (80%)       (30%)
```

### La Geometría del Árbol (Espacio de Instancias)

En el espacio matemático, los árboles de decisión no trazan curvas ni líneas diagonales. Cortan el espacio utilizando fronteras ortogonales (perpendiculares a los ejes). En múltiples dimensiones, estos cortes se denominan **hiperplanos**, y cada división encierra a los datos en "cajas" cada vez más pequeñas y puras.

Esta geometría tiene una implicación práctica importante: los árboles funcionan bien cuando las fronteras entre clases son paralelas a los ejes de las variables, pero pueden tener dificultades con relaciones diagonales o curvas complejas (para eso existen otros algoritmos como SVM o redes neuronales).

### ¿Cuándo dejar de crecer?

Un árbol puede seguir dividiendo hasta que cada hoja tenga un solo registro. Esto lleva al [sobreajuste](./04-probabilidades-y-sobreajuste.md). Las técnicas de poda (*pruning*) limitan el crecimiento:

- **Pre-poda:** Detener el crecimiento cuando la ganancia de información es menor a un umbral.
- **Post-poda:** Dejar crecer el árbol completo y luego reemplazar ramas con pocos casos por hojas.

## Interpretabilidad: El Poder de las Reglas Lógicas

Para el negocio y la auditoría algorítmica, los árboles son invaluables por su transparencia.

- Todo árbol de decisión es matemáticamente equivalente a un conjunto de reglas **SI-ENTONCES (IF-THEN)**.
- Al rastrear el camino desde el nodo raíz hasta cualquier hoja (conectando los nodos con el operador lógico `AND`), se extrae la regla exacta que define a ese segmento.

**Ejemplo de regla extraída del árbol anterior:**

```
SI Edad > 30 AND Ingreso > 50k ENTONCES Cliente = Lealtad (95%)
SI Edad ≤ 30 AND Historial > 2 años ENTONCES Cliente = Lealtad (80%)
```

Esta capacidad de extraer reglas elimina el problema de la "caja negra" presente en modelos más complejos como las Redes Neuronales, y es una de las razones por las que los árboles son tan populares en industrias reguladas como banca, salud y seguros. Ver [recomendaciones para stakeholders](../../05-recomendaciones-clave.md#3-sobre-la-evaluación-y-el-despliegue) sobre la importancia de la transparencia.
