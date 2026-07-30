precios = {
    "laptop": 899,
    "tablet": 349
}

rebaja = {
    producto: round(precio * 0.9, 2)
    for producto, precio in precios.items()
}

print(f"Precios con descuento: {rebaja}")

stock = {
    "manzanas": 10,
    "peras": 0,
    "naranjas": 25
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

gran_total = sum(precios.values())

porcentajes = {
    producto: round(precio / gran_total * 100, 1)
    for producto, precio in precios.items()
}

print(f"Porcentaje del total: {porcentajes}")