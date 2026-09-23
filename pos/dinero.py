"""Utilidades para trabajar con importes.

Todo el dinero del TPV va en Decimal, nunca en float.
"""
from decimal import ROUND_HALF_EVEN, Decimal

CENTIMO = Decimal("0.01")


def a_decimal(valor) -> Decimal:
    """Convierte texto o número a Decimal sin pasar por float. Acepta coma decimal."""
    if isinstance(valor, Decimal):
        return valor
    return Decimal(str(valor).replace(",", "."))


def redondear(importe: Decimal) -> Decimal:
    """Redondea al céntimo, como lo haría una calculadora."""
    return importe.quantize(CENTIMO, rounding=ROUND_HALF_EVEN)


def formatear(importe: Decimal) -> str:
    """3.5 -> '3,50 €'"""
    return f"{redondear(importe):.2f} €".replace(".", ",")
