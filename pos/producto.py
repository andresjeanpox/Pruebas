from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: Decimal  # sin IVA
    categoria_iva: str  # "general", "reducido" o "superreducido"
    stock: int
