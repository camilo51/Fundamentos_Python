a = [1, 2, 3]

b = a
b[0] = 100

print(f"Lista a: {a}")
print(f"Lista b: {b}")

a = [1, 2, 3]

b = a.copy()
b[0] = 100

print(f"Lista a con copy(): {a}")
print(f"Lista b con copy(): {b}")

import copy

anidada = [[1, 2], [3, 4]]

deep = copy.deepcopy(anidada)
deep[0][0] = 99

print(f"Lista original: {anidada}")
print(f"Copia profunda: {deep}")