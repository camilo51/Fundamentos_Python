cuadrados = []

for numero in range(10):
    cuadrados.append(numero ** 2)

print(f"Cuadrados con for: {cuadrados}")

cuadrados = [numero ** 2 for numero in range(10)]

print(f"Cuadrados con list comprehension: {cuadrados}")

pares = [numero for numero in range(10) if numero % 2 == 0]

print(f"Números pares: {pares}")

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(9 / 5) * temperatura + 32 for temperatura in celsius]

print(f"Temperaturas en Fahrenheit: {fahrenheit}")

usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Carlos", "edad": 35}
]

nombres = [usuario["nombre"] for usuario in usuarios]

print(f"Nombres: {nombres}")