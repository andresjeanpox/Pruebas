"""Informes de caja."""
from collections import Counter
from datetime import date, datetime
from decimal import Decimal


def ventas_del_dia(ventas: list[dict], dia: date) -> list[dict]:
    return [v for v in ventas if datetime.fromisoformat(v["fecha"]).date() == dia]


def total_del_dia(ventas: list[dict], dia: date) -> Decimal:
    total = Decimal("0")
    for venta in ventas_del_dia(ventas, dia):
        total += venta["total"]
    return total


def mas_vendidos(ventas: list[dict], n: int = 3) -> list[tuple[str, int]]:
    """Los n productos con más unidades vendidas: [(nombre, unidades), ...]"""
    contador = Counter()
    for venta in ventas:
        for linea in venta["lineas"]:
            contador[linea["nombre"]] += linea["cantidad"]
    return sorted(contador.items(), key=lambda par: par[1], reverse=True)[:n]
