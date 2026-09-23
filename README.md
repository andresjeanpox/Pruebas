# TPV La Tiendita: proyecto de práctica

Un terminal punto de venta (TPV) en modo texto, en Python. Funciona, pero **tiene errores**.
Tu papel: eres el programador de la tienda. Te llegan incidencias (`TICKETS.md`), las reproduces,
encuentras la causa, escribes una prueba, lo arreglas y lo entregas.

## Puesta en marcha

Abre una terminal en esta carpeta (`D:\Escritorio\tpv-practica`).

```powershell
# El entorno virtual ya está creado. Si lo borras, se rehace así:
#   python -m venv .venv
#   .venv\Scripts\python -m pip install -r requirements-dev.txt

.venv\Scripts\python -m pos          # arrancar el TPV
.venv\Scripts\python -m pytest       # pasar todas las pruebas
```

Si activas el entorno (`.venv\Scripts\activate`), basta con `python -m pos` y `pytest`.
En VS Code: *Python: Select Interpreter* y eliges `.venv`.

## Cómo está hecho

| Archivo | Qué hace |
|---|---|
| `pos/__main__.py` | Arranque, log y captura de errores inesperados |
| `pos/cli.py` | Menús y lo que teclea el cajero |
| `pos/inventario.py` | Carga `datos/productos.csv`, busca productos y descuenta stock |
| `pos/producto.py` | La clase `Producto` |
| `pos/carrito.py` | La venta en curso: líneas, totales y descuentos |
| `pos/impuestos.py` | Tipos de IVA |
| `pos/descuentos.py` | Promociones (`PROMO10`, `CUPON5`, `2X1CAFE`) |
| `pos/pagos.py` | Cobro y desglose del cambio |
| `pos/ticket.py` | El ticket impreso |
| `pos/ventas.py` | Guarda las ventas en `datos/ventas.json` |
| `pos/informes.py` | Informe del día |
| `pos/dinero.py` | Redondeo y formato de importes |
| `tests/` | Pruebas con pytest |
| `logs/pos.log` | Se crea al usarlo. Si el TPV "peta", aquí está el traceback |

Los precios del CSV van **sin IVA**. El dinero se maneja con `Decimal`, no con `float`.

## Cómo trabajar una incidencia

1. **Reproduce.** Haz en el TPV lo que cuenta la incidencia hasta que veas el fallo con tus ojos.
2. **Lee el error.** Si hay traceback (en pantalla o en `logs/pos.log`), léelo **de abajo arriba**:
   la última línea es el error y las de encima dicen dónde pasó.
3. **Localiza.** ¿Qué archivo y qué función? Usa `print()` o, mejor, pon `breakpoint()` en el
   código y el programa se para ahí (`n` = siguiente línea, `p variable` = ver valor, `c` = seguir).
4. **Prueba que falla.** Busca el test que lo cubre (`pytest -k nombre`) o escríbelo tú.
   El test tiene que fallar **antes** de tu arreglo.
5. **Arregla lo mínimo.** No reescribas medio programa.
6. **Pasa toda la suite.** `pytest` entero, no solo tu test: comprueba que no has roto otra cosa.
7. **Commit.** Un commit por incidencia: `git commit -am "POS-103: permitir pagar el importe exacto"`.

## Comandos útiles de pytest

```powershell
pytest                              # todo
pytest -x                           # para en el primer fallo
pytest tests/test_pagos.py          # un archivo
pytest -k exacto                    # tests cuyo nombre contiene "exacto"
pytest --tb=short                   # tracebacks más cortos
pytest -v                           # un test por línea
```

Al empezar hay **22 tests en rojo**. El objetivo es dejarlos todos en verde, y además arreglar las
incidencias "sin test" escribiendo sus pruebas.

## Git

El proyecto ya es un repositorio con un primer commit. Lo básico:

```powershell
git status                 # qué has cambiado
git diff                   # ver los cambios línea a línea
git switch -c pos-103      # rama para una incidencia (opcional)
git commit -am "POS-103: ..."
git log --oneline          # historial
git restore pos/pagos.py   # deshacer tus cambios en un archivo (¡cuidado!)
```

## Reglas del juego

- No hay soluciones escritas en ningún sitio. Si te atascas, pide **una pista** (no la solución).
- Los tests están bien. Si un test te parece incorrecto, argumenta por qué antes de tocarlo.
- `datos/productos.csv` también forma parte del sistema: a veces el error está en los datos.
