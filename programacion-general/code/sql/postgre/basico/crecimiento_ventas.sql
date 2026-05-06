SELECT
    id_ventas,
    fecha_transaccion,
    monto,
    -- 1. Obtenemos el monto de la venta anterior (offset=1).
    LAG(monto, 1) OVER (ORDER BY fecha_transaccion) AS monto_venta_anterior,
    -- 2. Calculamos la diferencia/crecimiento entre la venta actual y la anterior.
    monto - LAG(monto, 1) OVER (ORDER BY fecha_transaccion) AS crecimiento_diario
FROM
    ventas
ORDER BY
    fecha_transaccion;
