from decimal import Decimal

import pytest

from pos.cli import leer_cantidad, leer_importe


def test_leer_cantidad_valida():
    assert leer_cantidad("3") == 3
    assert leer_cantidad(" 12 ") == 12


@pytest.mark.parametrize("texto", ["abc", "", "0", "-2", "1.5"])
def test_leer_cantidad_no_valida(texto):
    assert leer_cantidad(texto) is None


def test_leer_importe():
    assert leer_importe("5,50") == Decimal("5.50")


@pytest.mark.parametrize("texto", ["abc", "", "0", "-5", "nan", "inf"])
def test_leer_importe_no_valido(texto):
    assert leer_importe(texto) is None
