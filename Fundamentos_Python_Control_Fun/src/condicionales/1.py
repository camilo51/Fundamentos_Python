stock = [12, 0, 5, 23, 2, 0, 8]
productos_agotados = []
total_criticos = []
for i in range(len(stock)):
    if stock[i] == 0:
        productos_agotados.append(i)
    elif stock[i] > 0 and stock[i] <= 5:
        total_criticos.append(stock[i])

porcentaje = ((len(stock) - len(productos_agotados)) / len(stock) * 100)
print(f"Porcentaje de disponibilidad del inventario: {porcentaje:.2f}%")
print("Productos agotados: ", productos_agotados)
print("Total de productos criticos: ", total_criticos)

