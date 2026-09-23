from decimal import Decimal

from pos.dinero import a_decimal, formatear, redondear


def test_a_decimal_acepta_coma():
    assert a_decimal("1,25") == Decimal("1.25")


def test_a_decimal_no_pasa_por_float():
    assert a_decimal("0.1") + a_decimal("0.2") == Decimal("0.3")


def test_formatear():
    assert formatear(Decimal("3.5")) == "3,50 €"


def test_redondear_mitad_hacia_arriba():
    assert redondear(Decimal("0.125")) == Decimal("0.13")
    assert redondear(Decimal("2.345")) == Decimal("2.35")


def test_redondear_normal():
    assert redondear(Decimal("1.234")) == Decimal("1.23")
    assert redondear(Decimal("1.236")) == Decimal("1.24")
