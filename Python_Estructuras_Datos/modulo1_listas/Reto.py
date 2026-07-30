def actualizar_precio(inventario, nombre, nuevo_precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[2] = nuevo_precio
            print(f"Se actualizó el precio de {nombre}.")
            return

    print("Producto no encontrado.")

def registrar_venta(inventario, nombre, cantidad):
    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad:
                producto[1] -= cantidad
                print("Venta registrada.")
            else:
                print("No hay suficiente stock.")
            return

    print("Producto no encontrado.")

def añadir_producto(inventario, nombre, cantidad, precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print("Stock actualizado.")
            return

    inventario.append([nombre, cantidad, precio])
    print("Producto agregado.")

def mostrar_inventario(inventario):
    print("\nInventario")

    for producto in inventario:
        print(f"Producto: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio: ${producto[2]}")
        print()

inventario = [
    ["Laptop", 10, 2500],
    ["Mouse", 20, 80],
    ["Teclado", 15, 120]
]

actualizar_precio(inventario, "Mouse", 90)
registrar_venta(inventario, "Laptop", 2)
añadir_producto(inventario, "Monitor", 8, 900)
añadir_producto(inventario, "Mouse", 5, 90)

mostrar_inventario(inventario)