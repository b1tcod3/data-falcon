WITH Calculo_Total AS (
    -- Paso 1: Calculamos el valor total de cada fila (Venta * Cantidad).
    SELECT
        fecha_transaccion,
        producto,
        (monto * cantidad) AS total_venta_por_item
    FROM
        ventas
)
-- Paso 2: Usamos el resultado del CTE para calcular la venta promedio.
SELECT
    fecha_transaccion,
    AVG(total_venta_por_item) AS promedio_venta_diaria
FROM
    Calculo_Total
GROUP BY
    fecha_transaccion
ORDER BY
    fecha_transaccion
