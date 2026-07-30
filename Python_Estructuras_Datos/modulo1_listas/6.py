frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(f"Me gusta {fruta}")

print()

for i, fruta in enumerate(frutas, 1):
    print(f"{i}. {fruta}")

print()

nombres = ["Ana", "Carlos", "Elena"]
edades = [28, 35, 23]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")

print()

cuadrados = [n ** 2 for n in range(5)]
pares = [n for n in range(10) if n % 2 == 0]

print(f"Cuadrados: {cuadrados}")
print(f"Pares: {pares}")