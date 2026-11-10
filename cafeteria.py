UMBRAL_DESCUENTO = 50000
PORCENTAJE_DESCUENTO = 0.10


def mostrar_productos(productos):
    print()
    print(f"{'Codigo':<8}{'Producto':<16}{'Precio':<10}{'Existencias'}")
    print("-" * 45)
    for codigo, (nombre, precio, existencias) in productos.items():
        print(f"{codigo:<8}{nombre:<16}${precio:<9}{existencias}")
    print()


def registrar_producto(productos, pedido, codigo, cantidad):
    if codigo not in productos:
        print("Producto no encontrado.")
        return False

    if cantidad <= 0:
        print("Cantidad no valida.")
        return False

    nombre, precio, existencias = productos[codigo]

    if cantidad > existencias:
        print("No hay suficientes unidades disponibles.")
        return False

    subtotal = precio * cantidad
    pedido.append((codigo, nombre, cantidad, subtotal))
    productos[codigo] = (nombre, precio, existencias - cantidad)
    print(f"Agregado: {cantidad} x {nombre} = ${subtotal}")
    return True


def calcular_total(pedido):
    total = 0
    for codigo, nombre, cantidad, subtotal in pedido:
        total += subtotal
    return total


def calcular_descuento(total):
    if total >= UMBRAL_DESCUENTO:
        return total * PORCENTAJE_DESCUENTO
    return 0


def mostrar_resumen(pedido):
    total = calcular_total(pedido)
    descuento = calcular_descuento(total)
    total_final = total - descuento

    print()
    print("========== RESUMEN DEL PEDIDO ==========")
    print(f"{'Producto':<20}{'Cantidad':<12}{'Subtotal'}")
    print("-" * 41)
    for codigo, nombre, cantidad, subtotal in pedido:
        print(f"{nombre:<20}{cantidad:<12}{subtotal}")
    print("-" * 41)
    print(f"Total : ${total:.0f}")
    print(f"Descuento : ${descuento:.0f}")
    print(f"TOTAL A PAGAR : ${total_final:.0f}")
    print("=" * 40)


def leer_entero(mensaje):
    texto = input(mensaje).strip()
    try:
        return int(texto)
    except ValueError:
        return None


def main():
    productos = {
        1: ("Cafe", 3000, 20),
        2: ("Jugo natural", 5000, 15),
        3: ("Sandwich", 8000, 10),
        4: ("Empanada", 2500, 25),
        5: ("Hamburguesa", 12000, 8),
    }
    pedido = []

    opcion = 0
    while opcion != 3:
        print("========== CAFETERIA ==========")
        print("1. Mostrar productos")
        print("2. Agregar producto al pedido")
        print("3. Finalizar pedido")
        opcion = leer_entero("Seleccione una opcion: ")

        if opcion == 1:
            mostrar_productos(productos)
        elif opcion == 2:
            codigo = leer_entero("Codigo del producto: ")
            if codigo is None:
                print("Producto no encontrado.")
            else:
                cantidad = leer_entero("Cantidad: ")
                if cantidad is None:
                    print("Cantidad no valida.")
                else:
                    registrar_producto(productos, pedido, codigo, cantidad)
        elif opcion == 3:
            if len(pedido) == 0:
                print("No se registraron productos en el pedido.")
            else:
                mostrar_resumen(pedido)
        else:
            print("Opcion no valida.")

#INTEGRANTES:
#Manuel David Galvis Olarte
#Valery Velandia Bernal

main()
