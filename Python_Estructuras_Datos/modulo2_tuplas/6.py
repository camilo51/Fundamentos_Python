datos = ("Juan", "Pérez", 35, "Madrid", "Ingeniero")

nombre, _, edad, _, profesion = datos

print(f"{nombre}, {edad}, {profesion}")

estudiantes = [
    ("Ana", 22, 9.5),
    ("Carlos", 20, 8.7)
]

for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")

def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minima, maxima, promedio = estadisticas([4, 7, 2, 9, 5])

print(f"Mínimo: {minima}")
print(f"Máximo: {maxima}")
print(f"Promedio: {promedio:.2f}")