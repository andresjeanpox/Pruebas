from decimal import Decimal

import pytest

from pos.impuestos import iva_de, precio_con_iva, tasa_de


def test_tasas_conocidas():
    assert tasa_de("general") == Decimal("0.21")
    assert tasa_de("reducido") == Decimal("0.10")
    assert tasa_de("superreducido") == Decimal("0.04")


def test_iva_de():
    assert iva_de(Decimal("100"), "general") == Decimal("21")


def test_precio_con_iva(cafe):
    assert precio_con_iva(cafe) == Decimal("3.52")


def test_categoria_desconocida_da_error():
    with pytest.raises(ValueError):
        tasa_de("inventada")


def test_categoria_tolera_mayusculas_y_espacios():
    assert tasa_de(" Reducido ") == Decimal("0.10")
