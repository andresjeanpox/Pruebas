from decimal import Decimal

import pytest

from pos.carrito import Carrito
from pos.inventario import ProductoNoEncontrado, StockInsuficiente


def test_total_con_iva(carrito, pan):
    carrito.agregar(pan, 2)
    # 0,83 x 2 = 1,66 + 4 % IVA = 1,7264
    assert carrito.total() == Decimal("1.73")


def test_mismo_producto_suma_en_la_misma_linea(carrito, pan):
    carrito.agregar(pan, 1)
    carrito.agregar(pan, 2)
    assert len(carrito.lineas) == 1
    assert carrito.lineas[0].cantidad == 3


def test_quitar_parte(carrito, pan):
    carrito.agregar(pan, 3)
    carrito.quitar("P001", 1)
    assert carrito.lineas[0].cantidad == 2


def test_quitar_todo_borra_la_linea(carrito, pan):
    carrito.agregar(pan, 2)
    carrito.quitar("P001", 2)
    assert carrito.lineas == []


def test_quitar_lo_que_no_esta(carrito):
    with pytest.raises(ProductoNoEncontrado):
        carrito.quitar("P001")


def test_cantidad_cero_no_vale(carrito, pan):
    with pytest.raises(ValueError):
        carrito.agregar(pan, 0)


def test_no_se_puede_pasar_del_stock(carrito, pan):
    with pytest.raises(StockInsuficiente):
        carrito.agregar(pan, 41)


def test_cada_carrito_empieza_vacio(pan):
    primero = Carrito()
    primero.agregar(pan, 1)
    segundo = Carrito()
    assert segundo.lineas == []


def test_total_redondea_como_la_calculadora(carrito, chicle):
    carrito.agregar(chicle, 1)
    # 0,50 + 21 % IVA = 0,605
    assert carrito.total() == Decimal("0.61")
