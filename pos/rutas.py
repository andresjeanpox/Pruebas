"""Rutas de los archivos que usa el TPV."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PRODUCTOS_CSV = RAIZ / "datos" / "productos.csv"
VENTAS_JSON = RAIZ / "datos" / "ventas.json"
LOG = RAIZ / "logs" / "pos.log"
