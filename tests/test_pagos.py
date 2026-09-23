from decimal import Decimal

import pytest

from pos.pagos import PagoInsuficiente, cobrar, desglose_cambio


def suma_desglose(desglose):
    return sum(Decimal(str(moneda)) * unidades for moneda, unidades in desglose.items())


def test_cobrar_con_billete_grande():
    assert cobrar(Decimal("7.30"), Decimal("20")) == Decimal("12.70")


def test_cobrar_con_poco_dinero():
    with pytest.raises(PagoInsuficiente):
        cobrar(Decimal("7.30"), Decimal("5"))


def test_cobrar_importe_exacto():
    assert cobrar(Decimal("7.30"), Decimal("7.30")) == Decimal("0")


def test_desglose_redondo():
    assert desglose_cambio(Decimal("15")) == {10: 1, 5: 1}


@pytest.mark.parametrize("cambio", ["0.30", "12.70", "18.63", "0.07"])
def test_desglose_suma_el_cambio_exacto(cambio):
    assert suma_desglose(desglose_cambio(Decimal(cambio))) == Decimal(cambio)
