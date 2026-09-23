import pytest

from pos import rutas
from pos.impuestos import tasa_de
from pos.inventario import Inventario, ProductoNoEncontrado


@pytest.fixture
def inventario():
    return Inventario.desde_csv(rutas.PRODUCTOS_CSV)


def test_carga_todos_los_productos(inventario):
    assert len(inventario.productos()) == 11


def test_buscar_ignora_espacios_y_minusculas(inventario):
    assert inventario.buscar(" p001 ").nombre == "Pan de barra"


def test_buscar_inexistente(inventario):
    with pytest.raises(ProductoNoEncontrado):
        inventario.buscar("X999")


def test_nombres_con_acentos(inventario):
    assert inventario.buscar("P004").nombre == "Piña"
    assert inventario.buscar("P003").nombre == "Café molido 250g"


def test_todos_los_productos_tienen_iva(inventario):
    for producto in inventario.productos():
        assert tasa_de(producto.categoria_iva) > 0, producto.nombre


def test_descontar(inventario):
    inventario.descontar("P001", 3)
    assert inventario.buscar("P001").stock == 37
