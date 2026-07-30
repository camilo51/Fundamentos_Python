tienda_centro = {
    "Laptop",
    "Mouse",
    "Teclado",
    "Monitor"
}

tienda_norte = {
    "Mouse",
    "Monitor",
    "Impresora",
    "Tablet"
}

tienda_sur = {
    "Monitor",
    "Tablet",
    "Audífonos",
    "Laptop"
}

catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

print(f"Catálogo completo: {catalogo_completo}")
print(f"Productos comunes: {productos_comunes}")

exclusivos_centro = tienda_centro.difference(tienda_norte).difference(tienda_sur)
exclusivos_norte = tienda_norte.difference(tienda_centro).difference(tienda_sur)
exclusivos_sur = tienda_sur.difference(tienda_centro).difference(tienda_norte)

print(f"Exclusivos centro: {exclusivos_centro}")
print(f"Exclusivos norte: {exclusivos_norte}")
print(f"Exclusivos sur: {exclusivos_sur}")

print(f"¿Centro y Norte no comparten productos?: {tienda_centro.isdisjoint(tienda_norte)}")
print(f"¿Norte y Sur no comparten productos?: {tienda_norte.isdisjoint(tienda_sur)}")

usuario1 = {
    "Acción",
    "Comedia",
    "Ciencia ficción",
    "Aventura"
}

usuario2 = {
    "Comedia",
    "Drama",
    "Romance",
    "Documental"
}

usuario3 = {
    "Acción",
    "Aventura",
    "Fantasía",
    "Ciencia ficción"
}

comunes = usuario1 & usuario3
universo = usuario1 | usuario2 | usuario3
exclusivos = usuario1 - usuario2
diferencias = usuario2 ^ usuario3

print(f"Géneros comunes: {comunes}")
print(f"Todos los géneros: {universo}")
print(f"Exclusivos de usuario1: {exclusivos}")
print(f"Diferencias entre usuario2 y usuario3: {diferencias}")

print(f"¿Los géneros comunes son subconjunto de usuario1?: {comunes <= usuario1}")

print("\nResumen")
print(f"Productos diferentes: {catalogo_completo}")
print(f"Productos en las tres tiendas: {productos_comunes}")
print(f"Géneros compartidos: {comunes}")
print(f"Todos los géneros: {universo}")