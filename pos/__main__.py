"""Punto de entrada: python -m pos"""
import logging
import sys

from pos import rutas
from pos.cli import main


def configurar_log() -> None:
    rutas.LOG.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=rutas.LOG,
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
    )


if __name__ == "__main__":
    configurar_log()
    log = logging.getLogger("pos")
    log.info("TPV arrancado")
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nHasta luego.")
    except Exception:
        log.exception("Error inesperado")
        print("\n*** Error inesperado. El TPV se ha cerrado. Detalles en logs/pos.log ***")
        sys.exit(1)
