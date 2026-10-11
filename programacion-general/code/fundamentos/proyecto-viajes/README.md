# Proyecto: convenio de viajes Decamerón / Avianca

Proyecto final de la categoría de Fundamentos de Programación. Modela la
liquidación de un viaje grupal según el convenio entre las cadenas **Decamerón**
y **Avianca**.

## Estructura

```
proyecto-viajes/
├── planes.py            # datos del convenio (planes, descuentos, equivalencias)
├── calculos.py          # lógica de cálculos (funciones puras)
├── main.py              # interfaz interactiva en consola
├── tests/
│   └── test_calculos.py # pruebas unitarias con pytest
└── README.md
```

## Enunciado resumido

La agencia ofrece seis planes de viaje, cada uno con su ciudad de destino y la
distancia en kilómetros:

| Código | Ciudad | Distancia (km) |
| ------ | ------ | -------------- |
| P_1    | San Andrés | 974.00 |
| P_2    | Cartagena  | 460.74 |
| P_3    | Barranquilla | 535.41 |
| P_4    | Aruba      | 559.28 |
| P_5    | Tolú       | 364.52 |
| P_6    | Santa Marta | 578.40 |

El descuento depende del tipo de empresa y del número de grupos:

| Tipo de empresa | Entre 1 y 5 grupos | Entre 5 y 10 grupos | Más de 10 grupos |
| --------------- | ------------------ | ------------------- | ---------------- |
| Privada         | 0.0%               | 3.5%                | 8.5%             |
| Pública         | 2.55%              | 7.5%                | 8.0%             |

El reporte muestra: ciudad de destino, distancia, trimestre de salida (según
el mes), valor inicial (distancia × valor del kilómetro), valor del descuento,
valor real en pesos y en dólares (según la TRM), dinero entregado, dinero
devuelto y si el monto entregado alcanza. Como complemento se convierte la
distancia a pies, brazas, leguas y millas usando las equivalencias del
convenio: 1 pie = 0.3084 m, 1 braza = 6 pies, 1 legua = 5572.7 m y
1 milla = 1.609 km.

## Supuestos documentados

- Las figuras del documento original no son visibles, por lo que el valor del
  kilómetro y la TRM se piden como entrada del usuario.
- El rango "entre 5 y 10" se interpreta de forma excluyente con "entre 1 y 5"
  en el valor 5 para evitar superposición: `[1,5]`, `(5,10]` y `>10`.
- Las conversiones de distancia se muestran como un bloque complementario del
  reporte, tal como las suministra el convenio.

## Uso

```bash
python main.py
```

## Pruebas

```bash
python -m pytest tests/test_calculos.py
```