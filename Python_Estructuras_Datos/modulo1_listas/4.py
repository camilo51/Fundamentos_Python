colores = ["rojo", "verde", "azul", "verde"]

colores.remove("verde")
print(f"Colores: {colores}")

nums = [10, 20, 30, 40]

ultimo = nums.pop()
print(f"Último eliminado: {ultimo}")
print(f"Lista: {nums}")

segundo = nums.pop(1)
print(f"Elemento eliminado en la posición 1: {segundo}")
print(f"Lista: {nums}")

mi_lista = [1, 2, 3, 4]

mi_lista.clear()
print(f"Lista vacía: {mi_lista}")