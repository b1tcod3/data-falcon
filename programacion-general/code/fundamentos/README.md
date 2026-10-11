# Fundamentos de programación - complementos y práctica completa

Colección de scripts con los ejercicios resueltos de los tutoriales
**Complementos** y **Práctica Completa** de la categoría de **Fundamentos de
Programación** del sitio web [Bitácora de Código](https://vivebtc.win).

Estos ejercicios están tomados de un material de clase de Programación Lineal
(pseudocódigo en PSeInt) y fueron traducidos y resueltos en Python.

## Tutoriales relacionados

- [Tutorial: complementos](https://vivebtc.win/b1s/school/complementos-fundamentos)
- [Tutorial: práctica completa](https://vivebtc.win/b1s/school/practica-completa-fundamentos)

## Estructura

```
fundamentos/
├── README.md
├── secuenciales/          # 10 ejercicios (solo entrada - proceso - salida)
├── decision/              # 9 ejercicios (condicionales simples y anidadas)
├── seleccion-multiple/    # 5 ejercicios (segun / caso)
└── proyecto-viajes/       # práctica final Decamerón/Avianca (con tests)
```

## Orden de estudio

1. Resuelve primero los ejercicios **secuenciales**.
2. Continúa con los de **decisión** y de **selección múltiple**.
3. Termina con el **proyecto de viajes** (práctica completa), que integra todo
   lo aprendido y se entrega con pruebas unitarias.

## Cómo ejecutar

Cada script es autocontenido y se ejecuta con:

```bash
python3 secuenciales/01_llamadas_telefonicas.py
python3 decision/06_mensaje_temperatura.py
python3 seleccion-multiple/02_central_telefonica.py
```

El proyecto de viajes tiene su propio [README](./proyecto-viajes/README.md) con
instrucciones de ejecución y pruebas:

```bash
cd proyecto-viajes
python main.py
python -m pytest tests/test_calculos.py
```