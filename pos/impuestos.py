"""Tipos de IVA."""
from decimal import Decimal

from pos.producto import Producto

TASAS = {
    "general": Decimal("0.21"),
    "reducido": Decimal("0.10"),
    "superreducido": Decimal("0.04"),
}


def tasa_de(categoria: str) -> Decimal:
    """Devuelve la tasa de IVA de una categoría (0.21 para "general", etc.)."""
    return TASAS.get(categoria, Decimal("0"))


def iva_de(importe: Decimal, categoria: str) -> Decimal:
    return importe * tasa_de(categoria)


def precio_con_iva(producto: Producto) -> Decimal:
    return producto.precio * (1 + tasa_de(producto.categoria_iva))
