from decimal import Decimal

import pytest

from pos.descuentos import DescuentoNoValido, buscar_descuento


def test_buscar_descuento_ignora_mayusculas():
    assert buscar_descuento(" promo10 ").codigo == "PROMO10"


def test_descuento_inexistente():
    with pytest.raises(DescuentoNoValido):
        buscar_descuento("GRATIS")


def test_promo10(carrito, cafe):
    carrito.agregar(cafe, 1)
    carrito.aplicar_descuento(buscar_descuento("PROMO10"))
    # 3,52 - 0,352 = 3,168
    assert carrito.total() == Decimal("3.17")


def test_dos_por_uno_con_dos_unidades(carrito, cafe):
    carrito.agregar(cafe, 2)
    carrito.aplicar_descuento(buscar_descuento("2X1CAFE"))
    assert carrito.total() == Decimal("3.52")


def test_dos_por_uno_con_tres_unidades(carrito, cafe):
    carrito.agregar(cafe, 3)
    carrito.aplicar_descuento(buscar_descuento("2X1CAFE"))
    # se pagan 2 de 3
    assert carrito.total() == Decimal("7.04")


def test_dos_por_uno_sin_el_producto(carrito, pan):
    carrito.agregar(pan, 2)
    carrito.aplicar_descuento(buscar_descuento("2X1CAFE"))
    assert carrito.total() == Decimal("1.73")
