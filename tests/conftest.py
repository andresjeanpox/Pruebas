from decimal import Decimal

import pytest

from pos.carrito import Carrito
from pos.producto import Producto


@pytest.fixture
def pan():
    return Producto("P001", "Pan de barra", Decimal("0.83"), "superreducido", 40)


@pytest.fixture
def cafe():
    return Producto("P003", "Café molido 250g", Decimal("3.20"), "reducido", 15)


@pytest.fixture
def chicle():
    return Producto("P007", "Chicle de menta", Decimal("0.50"), "general", 50)


@pytest.fixture
def carrito():
    return Carrito(lineas=[])
