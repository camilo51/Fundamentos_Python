numeros = [1, 2, 2, 3, 4, 3, 5, 5, 1]

unicos = {numero for numero in numeros}

print(f"Números únicos: {unicos}")

palabras = ["manzana", "banana", "mango", "mora", "naranja"]

iniciales = {palabra[0] for palabra in palabras}

print(f"Iniciales únicas: {iniciales}")

texto = "python es un lenguaje versátil"

vocales = {
    letra
    for letra in texto.lower()
    if letra in "aeiou"
}

print(f"Vocales únicas: {vocales}")

pares_cuadrados = {
    numero ** 2
    for numero in range(10)
    if numero % 2 == 0
}

print(f"Cuadrados de números pares: {pares_cuadrados}")