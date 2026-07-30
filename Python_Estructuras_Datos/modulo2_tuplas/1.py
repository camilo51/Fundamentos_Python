coordenadas = (10, 20)

try:
    coordenadas[0] = 15
except TypeError as e:
    print(f"Error: {e}")

config = ("config_v1", [1, 2, 3])

config[1].append(4)

print(f"Configuración: {config}")