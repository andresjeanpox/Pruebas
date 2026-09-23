# Incidencias abiertas: TPV La Tiendita

Estas incidencias las ha reportado el personal de la tienda. Describen **lo que ven**, no la causa;
averiguar la causa es tu trabajo.

Dificultad: 🟢 fácil · 🟡 media · 🔴 difícil.
Las marcadas con **(sin test)** no tienen prueba automática: escríbela tú antes de arreglarlas.

---

### POS-101 🟢 El programa se cierra si me equivoco con la cantidad
> Estaba añadiendo pan y en vez de "2" escribí "dos". El TPV se cerró de golpe y perdí la venta
> entera. Tampoco debería dejarme poner 0 o una cantidad negativa.
> (Marta, caja 1)

### POS-102 🟢 La hora del ticket no es la real
> Un cliente se queja de que su ticket pone las 18:09 y eran las 18:40. Los minutos del ticket
> no tienen nada que ver con la hora de verdad.
> (Luis, encargado)

### POS-103 🟢 No puedo cobrar cuando me dan el dinero justo
> El total era 7,30 € y la clienta me dio exactamente 7,30 €. El TPV me dice que falta dinero.
> Tuve que pedirle un céntimo más y devolvérselo.
> (Marta, caja 1)

### POS-104 🟢 "Más vendidos" enseña lo que menos se vende
> En el informe del día, en "Más vendidos" salen cosas que apenas vendemos, y el pan, que es lo
> que más sale, no aparece.
> (Luis, encargado)

### POS-105 🟡 Los nombres con acentos salen con símbolos raros
> Desde que pusimos el TPV en los portátiles nuevos con Windows, en el inventario sale
> "PiÃ±a" y "CafÃ© molido". En el ordenador del proveedor se veía bien.
> (Luis, encargado)

### POS-106 🟡 La promoción 2X1CAFE cierra el programa
> Cada vez que meto el código 2X1CAFE el TPV se cierra. Cuando lo arregléis, fijaos en que si el
> cliente lleva 3 paquetes paga 2, no 1,5.
> (Marta, caja 1)

### POS-107 🟡 Las aceitunas se están vendiendo sin IVA
> La gestoría ha visto que las aceitunas rellenas salen al mismo precio en el TPV que en la
> lista de precios sin IVA. Esto nos puede dar un disgusto con Hacienda. ¿Hay más productos así?
> Y si mañana alguien mete mal una categoría en el CSV, prefiero que el TPV avise a que venda sin IVA.
> (Gestoría)

### POS-108 🟡 Al siguiente cliente le salen los productos del anterior
> Cobro una venta, empiezo otra y en el carrito ya aparecen los productos del cliente de antes.
> Si cancelo y empiezo otra, siguen ahí.
> (Marta, caja 1)

### POS-109 🟡 El desglose del cambio a veces se queda corto
> Tengo que dar 2,96 € y el TPV me dice: 2 € + 0,50 € + 0,20 € + 0,20 € + 0,05 €. Eso son 2,95 €.
> No pasa siempre, pero pasa mucho.
> (Marta, caja 1)

### POS-110 🔴 El informe del día siempre dice 0 ventas y 0,00 €
> Hemos vendido toda la mañana y el informe dice que no hay ventas. Además, todos los tickets
> salen con el número 1. El archivo `datos/ventas.json` sí existe.
> (Luis, encargado)

### POS-111 🔴 Un céntimo de diferencia con la calculadora
> Un chicle cuesta 0,50 € + 21 % de IVA = 0,605 €, que en la calculadora es 0,61 €. El TPV
> cobra 0,60 €. Un céntimo no es nada, pero la gestoría quiere que cuadre.
> (Gestoría)

### POS-112 🔴 (sin test) El inventario marca stock negativo
> Solo quedaban 5 botellas de agua. Añadí 3, luego otras 3 porque el cliente cogió más, y me dejó.
> Ahora el inventario dice que tenemos -1 botellas.
> (Marta, caja 1)

### POS-113 🔴 (sin test) Un cliente metió el mismo cupón dos veces
> Un cliente muy listo me pidió que metiera PROMO10 dos veces y el TPV le hizo casi un 20 % de
> descuento.
> (Luis, encargado)

### POS-114 🔴 (sin test) Con el CUPON5 le hemos dado dinero a un cliente
> Compró una barra de pan (0,86 €) y usó el CUPON5 (5 € de descuento). El TPV puso un total negativo
> y al cobrar le dimos más cambio del que nos entregó.
> (Luis, encargado)

---

¿Solo eso? Puede que al arreglar una incidencia aparezca otro error que nadie había visto.
Pasa mucho en la vida real. Si lo encuentras, abre tú la incidencia (POS-115...) y arréglalo.
