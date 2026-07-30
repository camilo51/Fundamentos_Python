numeros = (1, 2, 3, 4, 5)
coords = (10, 20, 30)
vacia = ()
singleton = (42,)

desde_lista = tuple([1, 2, 3])
desde_str = tuple("Python")
desde_rango = tuple(range(5))

print(f"Números: {numeros}")
print(f"Coordenadas: {coords}")
print(f"Tupla vacía: {vacia}")
print(f"Singleton: {singleton}")

print(f"Desde lista: {desde_lista}")
print(f"Desde cadena: {desde_str}")
print(f"Desde rango: {desde_rango}")

print(type((42)))
print(type((42,)))