"""Inventario de productos de la tienda."""
import csv

from pos.dinero import a_decimal
from pos.producto import Producto


class ProductoNoEncontrado(Exception):
    pass


class StockInsuficiente(Exception):
    pass


class Inventario:
    def __init__(self):
        self._productos: dict[str, Producto] = {}

    @classmethod
    def desde_csv(cls, ruta) -> "Inventario":
        """Carga el inventario de un CSV separado por ';'."""
        inventario = cls()
        with open(ruta, newline="") as archivo:
            for fila in csv.DictReader(archivo, delimiter=";"):
                inventario.agregar(
                    Producto(
                        codigo=fila["codigo"].strip(),
                        nombre=fila["nombre"].strip(),
                        precio=a_decimal(fila["precio"]),
                        categoria_iva=fila["iva"],
                        stock=int(fila["stock"]),
                    )
                )
        return inventario

    def agregar(self, producto: Producto) -> None:
        self._productos[producto.codigo] = producto

    def buscar(self, codigo: str) -> Producto:
        codigo = codigo.strip().upper()
        try:
            return self._productos[codigo]
        except KeyError:
            raise ProductoNoEncontrado(f"No existe el producto {codigo!r}") from None

    def descontar(self, codigo: str, cantidad: int) -> None:
        # El carrito ya comprueba el stock al añadir, aquí solo restamos.
        self.buscar(codigo).stock -= cantidad

    def productos(self) -> list[Producto]:
        return sorted(self._productos.values(), key=lambda p: p.codigo)
