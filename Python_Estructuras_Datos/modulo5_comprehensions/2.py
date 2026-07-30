cuadrados = {
    numero: numero ** 2
    for numero in range(5)
}

print(f"Cuadrados: {cuadrados}")

stock = {
    "manzanas": 10,
    "platanos": 3,
    "naranjas": 25,
    "peras": 0
}

disponibles = {
    fruta: cantidad
    for fruta, cantidad in stock.items()
    if cantidad > 0
}

print(f"Productos disponibles: {disponibles}")

original = {
    "a": 1,
    "b": 2,
    "c": 3
}

invertido = {
    valor: clave
    for clave, valor in original.items()
}

print(f"Diccionario invertido: {invertido}")

estudiantes = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Carlos"}
]

id_nombre = {
    estudiante["id"]: estudiante["nombre"]
    for estudiante in estudiantes
}

print(f"ID y nombre: {id_nombre}")