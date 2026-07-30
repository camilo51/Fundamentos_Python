ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

valor_por_producto = [
    producto["unidades"] * producto["precio"]
    for producto in ventas
]

print(f"Valor por producto: {valor_por_producto}")

alto_valor = [
    producto["producto"]
    for producto in ventas
    if producto["unidades"] * producto["precio"] > 1000
]

print(f"Productos de alto valor: {alto_valor}")

resumen = {
    producto["producto"]: producto["unidades"] * producto["precio"]
    for producto in ventas
}

print(f"Resumen: {resumen}")

gran_total = sum(valor_por_producto)

print(f"Gran total: {gran_total}")