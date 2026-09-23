from datetime import datetime
from decimal import Decimal

from pos.ticket import ANCHO, formatear_fecha, generar_ticket


def test_formatear_fecha():
    assert formatear_fecha(datetime(2026, 9, 23, 14, 5)) == "23/09/2026 14:05"


def test_ticket_tiene_productos_y_total(carrito, cafe):
    carrito.agregar(cafe, 1)
    ticket = generar_ticket(carrito, 7, datetime(2026, 9, 23, 14, 5), Decimal("5"), Decimal("1.48"))
    assert "1 x Café molido 250g" in ticket
    assert "3,52 €" in ticket
    assert "Ticket 7" in ticket


def test_ticket_no_se_sale_del_papel(carrito, cafe):
    carrito.agregar(cafe, 1)
    ticket = generar_ticket(carrito, 1, datetime(2026, 9, 23), Decimal("5"), Decimal("1.48"))
    assert all(len(fila) <= ANCHO for fila in ticket.splitlines())
