cuadrados = [numero ** 2 for numero in range(100)]

print(f"Primeros 10 cuadrados: {cuadrados[:10]}")
print(f"Cantidad de elementos: {len(cuadrados)}")

generador = (numero ** 2 for numero in range(1_000_000))

primero = next(generador)
segundo = next(generador)
tercero = next(generador)

print(f"Primer valor: {primero}")
print(f"Segundo valor: {segundo}")
print(f"Tercer valor: {tercero}")

datos = [
    {"activo": True, "valor": 10},
    {"activo": False, "valor": 5},
    {"activo": True, "valor": 20}
]

umbral = 15

def calcular(item):
    return item["valor"] * 2

def transformar(valor):
    return f"Resultado: {valor}"

resultados = []

for item in datos:
    if item["activo"]:
        valor = calcular(item)
        if valor > umbral:
            resultados.append(transformar(valor))

print(f"Resultados: {resultados}")