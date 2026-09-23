from datetime import date
from decimal import Decimal

from pos.informes import mas_vendidos, total_del_dia

# Así quedan las ventas después de pasar por el JSON: los importes son texto.
VENTAS = [
    {
        "numero": 1,
        "fecha": "2026-09-23T10:00:00",
        "lineas": [
            {"codigo": "P001", "nombre": "Pan de barra", "cantidad": 5, "importe": "4.32"},
            {"codigo": "P003", "nombre": "Café molido 250g", "cantidad": 1, "importe": "3.52"},
        ],
        "total": "7.84",
    },
    {
        "numero": 2,
        "fecha": "2026-09-23T12:30:00",
        "lineas": [
            {"codigo": "P002", "nombre": "Leche entera 1L", "cantidad": 2, "importe": "1.98"},
            {"codigo": "P001", "nombre": "Pan de barra", "cantidad": 1, "importe": "0.86"},
        ],
        "total": "2.84",
    },
    {
        "numero": 3,
        "fecha": "2026-09-22T19:00:00",
        "lineas": [{"codigo": "P007", "nombre": "Chicle de menta", "cantidad": 1, "importe": "0.61"}],
        "total": "0.61",
    },
]


def test_total_del_dia():
    assert total_del_dia(VENTAS, date(2026, 9, 23)) == Decimal("10.68")


def test_dia_sin_ventas():
    assert total_del_dia(VENTAS, date(2026, 1, 1)) == Decimal("0")


def test_mas_vendidos_primero_el_que_mas():
    assert mas_vendidos(VENTAS, 2) == [("Pan de barra", 6), ("Leche entera 1L", 2)]
