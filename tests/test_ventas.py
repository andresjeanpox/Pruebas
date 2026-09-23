from datetime import datetime

from pos.ventas import RegistroVentas, venta_a_dict


def test_sin_archivo_no_hay_ventas(tmp_path):
    assert RegistroVentas(tmp_path / "ventas.json").cargar() == []


def test_guarda_y_recupera_varias_ventas(tmp_path, carrito, cafe):
    registro = RegistroVentas(tmp_path / "ventas.json")
    carrito.agregar(cafe, 1)
    registro.guardar(venta_a_dict(carrito, 1, datetime(2026, 9, 23, 10, 0)))
    registro.guardar(venta_a_dict(carrito, 2, datetime(2026, 9, 23, 11, 0)))

    ventas = registro.cargar()
    assert [v["numero"] for v in ventas] == [1, 2]
    assert ventas[0]["lineas"][0]["nombre"] == "Café molido 250g"
