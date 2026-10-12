# Fundamentos de programación - complementos y práctica completa

Colección de scripts con los ejercicios resueltos de los tutoriales
**Complementos** y **Práctica Completa** de la categoría de **Fundamentos de
Programación y en la plataforma [B1School](https://vivebtc.win/b1s) (Bitácora de Código: https://vivebtc.win).

Estos ejercicios están tomados de un material de clase de Programación Lineal
(pseudocódigo en PSeInt) y fueron traducidos y resueltos en Python.

Cada ejercicio se entrega en **dos versiones**: el pseudocódigo original en
**PSeInt** (`.psc`) y su traducción a **Python** (`.py`), para comparar la
misma lógica en los dos idiomas.

## Tutoriales relacionados

- [Tutorial: complementos](https://vivebtc.win/b1s/school/complementos-fundamentos) — disponible en [B1School](https://vivebtc.win/b1s)
- [Tutorial: práctica completa](https://vivebtc.win/b1s/school/practica-completa-fundamentos) — disponible en [B1School](https://vivebtc.win/b1s)

## Estructura

```
fundamentos/
├── README.md
├── secuenciales/          # 10 ejercicios (solo entrada - proceso - salida)
├── decision/              # 9 ejercicios (condicionales simples y anidadas)
├── seleccion-multiple/    # 5 ejercicios (segun / caso)
└── proyecto-viajes/       # práctica final Decamerón/Avianca (con tests)
```

En cada carpeta conviven los dos formatos: `NN_nombre.psc` (PSeInt) y
`NN_nombre.py` (Python). El proyecto de viajes incluye además `main.psc`.

## Orden de estudio

1. Resuelve primero los ejercicios **secuenciales**.
2. Continúa con los de **decisión** y de **selección múltiple**.
3. Termina con el **proyecto de viajes** (práctica completa), que integra todo
   lo aprendido y se entrega con pruebas unitarias.

## Cómo ejecutar

### En PSeInt (`.psc`)

Cada ejercicio tiene su archivo `.psc` listo para abrir en PSeInt:

```bash
pseint secuenciales/01_llamadas_telefonicas.psc
```

Para revisar la sintaxis o ejecutarlo sin entorno gráfico:

```bash
# solo revisar sintaxis (no ejecuta)
pseint secuenciales/01_llamadas_telefonicas.psc --norun --nouser --rawerrors

# ejecutar pasando las entradas por línea de comandos
pseint secuenciales/03_baldosas_bano.psc --nouser --noinput --input=2 --input=10
```

> La instalación de PSeInt en Linux se describe en el
> [tutorial de Complementos](https://vivebtc.win/b1s/school/complementos-fundamentos).

### En Python (`.py`)

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