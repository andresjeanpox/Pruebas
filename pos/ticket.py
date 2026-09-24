"""Ticket impreso para el cliente."""
from datetime import datetime
from decimal import Decimal

from pos.dinero import formatear

ANCHO = 40


def formatear_fecha(momento: datetime) -> str:
    """datetime(2026, 9, 23, 14, 5) -> '23/09/2026 14:05'"""
    return momento.strftime("%d/%m/%Y %H:%M")


def _fila(izquierda: str, importe: Decimal) -> str:
    derecha = formatear(importe)
    hueco = ANCHO - len(derecha) - 1
    return izquierda[:hueco].ljust(hueco) + " " + derecha


def generar_ticket(carrito, numero: int, momento: datetime, entregado: Decimal, cambio: Decimal) -> str:
    filas = [
        "LA TIENDITA".center(ANCHO),
        "C/ Mayor 1".center(ANCHO),
        "-" * ANCHO,
        f"Ticket {numero}".ljust(ANCHO - 16) + formatear_fecha(momento),
        "-" * ANCHO,
    ]
    for linea in carrito.lineas:
        filas.append(_fila(f"{linea.cantidad} x {linea.producto.nombre}", linea.total))
    filas.append("-" * ANCHO)
    filas.append(_fila("Subtotal", carrito.total_bruto()))
    for descuento in carrito.descuentos:
        filas.append(_fila(f"Dto. {descuento.codigo}", -descuento.calcular(carrito)))
    filas.append(_fila("TOTAL (IVA incluido)", carrito.total()))
    filas.append(_fila("Entregado", entregado))
    filas.append(_fila("Cambio", cambio))
    filas.append("-" * ANCHO)
    filas.append("Gracias por su compra".center(ANCHO))
    return "\n".join(filas)
