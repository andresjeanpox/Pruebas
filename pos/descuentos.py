"""Promociones y cupones."""
from decimal import Decimal

from pos.impuestos import precio_con_iva


class DescuentoNoValido(Exception):
    pass


class DescuentoPorcentaje:
    def __init__(self, codigo: str, porcentaje: int):
        self.codigo = codigo
        self.porcentaje = porcentaje

    def calcular(self, carrito) -> Decimal:
        return carrito.total_bruto() * self.porcentaje / 100


class CuponFijo:
    def __init__(self, codigo: str, importe: Decimal):
        self.codigo = codigo
        self.importe = importe

    def calcular(self, carrito) -> Decimal:
        return self.importe


class DosPorUno:
    """Por cada dos unidades del producto, una sale gratis."""

    def __init__(self, codigo: str, codigo_producto: str):
        self.codigo = codigo
        self.codigo_producto = codigo_producto

    def calcular(self, carrito) -> Decimal:
        for linea in carrito.lineas:
            if linea.producto.codigo == self.codigo_producto:
                gratis = linea.cantidad / 2
                return precio_con_iva(linea.producto) * gratis
        return Decimal("0")


CATALOGO = {
    "PROMO10": DescuentoPorcentaje("PROMO10", 10),
    "CUPON5": CuponFijo("CUPON5", Decimal("5")),
    "2X1CAFE": DosPorUno("2X1CAFE", "P003"),
}


def buscar_descuento(codigo: str):
    codigo = codigo.strip().upper()
    try:
        return CATALOGO[codigo]
    except KeyError:
        raise DescuentoNoValido(f"El código {codigo!r} no existe") from None
