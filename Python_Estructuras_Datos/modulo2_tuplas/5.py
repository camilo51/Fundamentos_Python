producto = ("Laptop XPS", 1299.99, "Dell")

nombre, precio, fabricante = producto

print(f"Nombre: {nombre}")
print(f"Precio: {precio}")
print(f"Fabricante: {fabricante}")

a, b = 5, 10

a, b = b, a

print(f"a: {a}, b: {b}")

numeros = (1, 2, 3, 4, 5)

primero, *resto = numeros
print(f"Primero: {primero}")
print(f"Resto: {resto}")

primero, *medio, ultimo = numeros
print(f"Primero: {primero}")
print(f"Medio: {medio}")
print(f"Último: {ultimo}")

*iniciales, ultimo = numeros
print(f"Iniciales: {iniciales}")
print(f"Último: {ultimo}")