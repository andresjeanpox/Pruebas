"""Cobro y cambio."""
from decimal import Decimal

MONEDAS = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]


class PagoInsuficiente(Exception):
    pass


def cobrar(total: Decimal, entregado: Decimal) -> Decimal:
    """Devuelve el cambio. Lanza PagoInsuficiente si no llega."""
    if entregado <= total:
        raise PagoInsuficiente(f"Faltan {total - entregado} €")
    return entregado - total


def desglose_cambio(cambio) -> dict:
    """Cuántos billetes/monedas de cada valor hay que dar. {moneda: unidades}"""
    resto = float(cambio)
    desglose = {}
    for moneda in MONEDAS:
        while resto >= moneda:
            resto -= moneda
            desglose[moneda] = desglose.get(moneda, 0) + 1
    return desglose
