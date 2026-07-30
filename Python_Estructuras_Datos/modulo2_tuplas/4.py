datos = ("Python", 3.9, 2023, "Tuplas")

print(f"Primer elemento: {datos[0]}")
print(f"Último elemento: {datos[-1]}")

nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"Del índice 2 al 5: {nums[2:6]}")
print(f"Elementos pares: {nums[::2]}")
print(f"Tupla invertida: {nums[::-1]}")

t = (1, 2, 3, 2, 4, 2, 5)

print(f"Cantidad de veces que aparece 2: {t.count(2)}")
print(f"Índice del número 3: {t.index(3)}")