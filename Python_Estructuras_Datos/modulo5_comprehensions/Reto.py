productos = [
    {
        "nombre": "Laptop",
        "categoria": "Tecnología",
        "unidades": 20,
        "precio": 800
    },
    {
        "nombre": "Teclado",
        "categoria": "Accesorios",
        "unidades": 50,
        "precio": 25
    },
    {
        "nombre": "Mouse",
        "categoria": "Accesorios",
        "unidades": 30,
        "precio": 15
    },
    {
        "nombre": "Monitor",
        "categoria": "Tecnología",
        "unidades": 10,
        "precio": 200
    }
]

valor_total = [
    producto["unidades"] * producto["precio"]
    for producto in productos
]

print(f"Valor total: {valor_total}")

productos_alto_valor = [
    producto["nombre"]
    for producto in productos
    if producto["unidades"] * producto["precio"] > 1000
]

print(f"Productos de alto valor: {productos_alto_valor}")

producto_info = {
    producto["nombre"]: {
        "valor": producto["unidades"] * producto["precio"],
        "unidades": producto["unidades"]
    }
    for producto in productos
}

print(f"Información de productos: {producto_info}")

ranking_premium = {
    producto["nombre"]: producto["unidades"] * producto["precio"]
    for producto in sorted(
        [producto for producto in productos if producto["precio"] > 50],
        key=lambda producto: producto["unidades"] * producto["precio"],
        reverse=True
    )
}

print(f"Ranking premium: {ranking_premium}")

categorias_unicas = {
    producto["categoria"]
    for producto in productos
}

productos_baratos = {
    producto["nombre"]
    for producto in productos
    if producto["precio"] <= 50
}

print(f"Categorías únicas: {categorias_unicas}")
print(f"Productos baratos: {productos_baratos}")

resumen_formateado = [
    f"{producto['nombre']} - ${producto['unidades'] * producto['precio']}"
    for producto in productos
]

gran_total = sum(
    producto["unidades"] * producto["precio"]
    for producto in productos
)

print(f"Resumen: {resumen_formateado}")
print(f"Gran total: ${gran_total}")