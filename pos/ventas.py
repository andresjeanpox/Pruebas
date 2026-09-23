"""Registro de ventas en un archivo JSON."""
import json
from datetime import datetime
from pathlib import Path

from pos.dinero import redondear


def venta_a_dict(carrito, numero: int, momento: datetime) -> dict:
    return {
        "numero": numero,
        "fecha": momento.isoformat(timespec="seconds"),
        "lineas": [
            {
                "codigo": linea.producto.codigo,
                "nombre": linea.producto.nombre,
                "cantidad": linea.cantidad,
                "importe": redondear(linea.total),
            }
            for linea in carrito.lineas
        ],
        "total": carrito.total(),
    }


class RegistroVentas:
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def cargar(self) -> list[dict]:
        try:
            with open(self.ruta, encoding="utf-8") as archivo:
                datos = json.load(archivo)
            return datos["ventas"]
        except Exception:
            return []

    def guardar(self, venta: dict) -> None:
        ventas = self.cargar()
        ventas.append(venta)
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(ventas, archivo, ensure_ascii=False, indent=2, default=str)
