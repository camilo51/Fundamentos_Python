frase = input("Ingrese una frase o párrafo largo: ")

frase = frase.lower()
frase = frase.replace(",", "")
frase = frase.replace(".", "")
frase = frase.replace(";", "")
frase = frase.replace("!", "")


frecuencias = {}
for palabra in frase.split():
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1


if frecuencias:
    palabra_mas_frecuente = max(frecuencias, key=frecuencias.get)
    conteo_palabra_mas_frecuente = frecuencias[palabra_mas_frecuente]

    print("La palabra más frecuente es:", palabra_mas_frecuente)
    print("Su conteo es:", conteo_palabra_mas_frecuente)

    print("Diccionario de frecuencias:")
    for palabra, frecuencia in frecuencias.items():
        print(palabra, ":", frecuencia)
else:
    print("No ingresó ningún texto.")