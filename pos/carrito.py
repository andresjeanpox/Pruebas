"""Carrito de la venta en curso."""
from dataclasses import dataclass
from decimal import Decimal

from pos.dinero import redondear
from pos.impuestos import iva_de
from pos.inventario import ProductoNoEncontrado, StockInsuficiente
from pos.producto import Producto


@dataclass
class Linea:
    producto: Producto
    cantidad: int

    @property
    def base(self) -> Decimal:
        return self.producto.precio * self.cantidad

    @property
    def iva(self) -> Decimal:
        return iva_de(self.base, self.producto.categoria_iva)

    @property
    def total(self) -> Decimal:
        return self.base + self.iva


class Carrito:
    def __init__(self, lineas=[]):
        self.lineas: list[Linea] = lineas
        self.descuentos = []

    def agregar(self, producto: Producto, cantidad: int = 1) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad tiene que ser positiva")
        if cantidad > producto.stock:
            raise StockInsuficiente(f"Solo quedan {producto.stock} de {producto.nombre}")
        for linea in self.lineas:
            if linea.producto.codigo == producto.codigo:
                linea.cantidad += cantidad
                return
        self.lineas.append(Linea(producto, cantidad))

    def quitar(self, codigo: str, cantidad: int = 1) -> None:
        for linea in self.lineas:
            if linea.producto.codigo == codigo:
                linea.cantidad -= cantidad
                if linea.cantidad <= 0:
                    self.lineas.remove(linea)
                return
        raise ProductoNoEncontrado(f"{codigo} no está en el carrito")

    def aplicar_descuento(self, descuento) -> None:
        self.descuentos.append(descuento)

    def base_imponible(self) -> Decimal:
        return sum((linea.base for linea in self.lineas), Decimal("0"))

    def total_iva(self) -> Decimal:
        return sum((linea.iva for linea in self.lineas), Decimal("0"))

    def total_bruto(self) -> Decimal:
        """Total con IVA antes de descuentos."""
        return self.base_imponible() + self.total_iva()

    def importe_descuentos(self) -> Decimal:
        return sum((d.calcular(self) for d in self.descuentos), Decimal("0"))

    def total(self) -> Decimal:
        """Lo que paga el cliente, redondeado al céntimo."""
        return redondear(self.total_bruto() - self.importe_descuentos())
