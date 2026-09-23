"""Interfaz de texto del TPV."""
import logging
from datetime import date, datetime
from decimal import InvalidOperation

from pos import rutas
from pos.carrito import Carrito
from pos.descuentos import DescuentoNoValido, buscar_descuento
from pos.dinero import a_decimal, formatear
from pos.impuestos import precio_con_iva
from pos.informes import mas_vendidos, total_del_dia, ventas_del_dia
from pos.inventario import Inventario, ProductoNoEncontrado, StockInsuficiente
from pos.pagos import PagoInsuficiente, cobrar, desglose_cambio
from pos.ticket import generar_ticket
from pos.ventas import RegistroVentas, venta_a_dict

log = logging.getLogger(__name__)

# Errores "normales" del día a día: se avisa al cajero y se sigue.
ERRORES_DE_NEGOCIO = (ProductoNoEncontrado, StockInsuficiente, PagoInsuficiente, DescuentoNoValido)


def leer_cantidad(texto: str):
    """Convierte lo que escribe el cajero en una cantidad. Devuelve None si no vale."""
    return int(texto)


def leer_importe(texto: str):
    """Convierte lo que escribe el cajero en un importe. Devuelve None si no vale."""
    try:
        importe = a_decimal(texto.strip())
        if not importe.is_finite() or importe <= 0:
            return None
    except InvalidOperation:
        return None
    return importe


def mostrar_carrito(carrito: Carrito) -> None:
    if not carrito.lineas:
        print("  (carrito vacío)")
        return
    for linea in carrito.lineas:
        p = linea.producto
        print(f"  {p.codigo}  {p.nombre:<24} x{linea.cantidad:<3} {formatear(linea.total):>10}")
    for descuento in carrito.descuentos:
        print(f"  Dto. {descuento.codigo:<30} {formatear(-descuento.calcular(carrito)):>10}")
    print(f"  TOTAL {formatear(carrito.total()):>38}")


def cerrar_venta(carrito: Carrito, inventario: Inventario, registro: RegistroVentas) -> bool:
    total = carrito.total()
    print(f"Total a pagar: {formatear(total)}")
    entregado = leer_importe(input("Entregado: "))
    if entregado is None:
        print("Importe no válido.")
        return False
    cambio = cobrar(total, entregado)

    for linea in carrito.lineas:
        inventario.descontar(linea.producto.codigo, linea.cantidad)
    momento = datetime.now()
    numero = len(registro.cargar()) + 1
    registro.guardar(venta_a_dict(carrito, numero, momento))
    log.info("Venta %s cobrada: total=%s entregado=%s cambio=%s", numero, total, entregado, cambio)

    print()
    print(generar_ticket(carrito, numero, momento, entregado, cambio))
    if cambio:
        print("\nCambio a devolver:")
        for moneda, unidades in desglose_cambio(cambio).items():
            print(f"  {unidades} x {formatear(a_decimal(moneda))}")
    return True


def nueva_venta(inventario: Inventario, registro: RegistroVentas) -> None:
    carrito = Carrito()
    mostrar_carrito(carrito)
    while True:
        print("\n[a] añadir  [q] quitar  [d] descuento  [v] ver  [c] cobrar  [x] cancelar")
        opcion = input("> ").strip().lower()
        try:
            if opcion == "a":
                producto = inventario.buscar(input("Código: "))
                cantidad = leer_cantidad(input("Cantidad: "))
                if cantidad is None:
                    print("Cantidad no válida.")
                    continue
                carrito.agregar(producto, cantidad)
                mostrar_carrito(carrito)
            elif opcion == "q":
                codigo = input("Código: ").strip().upper()
                cantidad = leer_cantidad(input("Cantidad: "))
                if cantidad is None:
                    print("Cantidad no válida.")
                    continue
                carrito.quitar(codigo, cantidad)
                mostrar_carrito(carrito)
            elif opcion == "d":
                carrito.aplicar_descuento(buscar_descuento(input("Código de descuento: ")))
                mostrar_carrito(carrito)
            elif opcion == "v":
                mostrar_carrito(carrito)
            elif opcion == "c":
                if not carrito.lineas:
                    print("El carrito está vacío.")
                    continue
                if cerrar_venta(carrito, inventario, registro):
                    return
            elif opcion == "x":
                print("Venta cancelada.")
                return
            else:
                print("Opción no válida.")
        except ERRORES_DE_NEGOCIO as error:
            log.warning("%s: %s", type(error).__name__, error)
            print(f"  ! {error}")


def ver_inventario(inventario: Inventario) -> None:
    print(f"\n{'Código':<6} {'Producto':<24} {'PVP':>9} {'Stock':>6}")
    for p in inventario.productos():
        print(f"{p.codigo:<6} {p.nombre:<24} {formatear(precio_con_iva(p)):>9} {p.stock:>6}")


def informe_del_dia(registro: RegistroVentas) -> None:
    hoy = date.today()
    ventas = registro.cargar()
    de_hoy = ventas_del_dia(ventas, hoy)
    print(f"\nInforme del {hoy:%d/%m/%Y}")
    print(f"  Ventas: {len(de_hoy)}")
    print(f"  Caja:   {formatear(total_del_dia(ventas, hoy))}")
    print("  Más vendidos:")
    for nombre, unidades in mas_vendidos(de_hoy):
        print(f"    {unidades:>4}  {nombre}")


def main() -> None:
    inventario = Inventario.desde_csv(rutas.PRODUCTOS_CSV)
    registro = RegistroVentas(rutas.VENTAS_JSON)
    while True:
        print("\n=== TPV La Tiendita ===")
        print("1. Nueva venta")
        print("2. Ver inventario")
        print("3. Informe del día")
        print("0. Salir")
        opcion = input("> ").strip()
        if opcion == "1":
            nueva_venta(inventario, registro)
        elif opcion == "2":
            ver_inventario(inventario)
        elif opcion == "3":
            informe_del_dia(registro)
        elif opcion == "0":
            print("Hasta luego.")
            return
        else:
            print("Opción no válida.")
