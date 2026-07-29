# Reto 3: Motor de Análisis de Frecuencia de Texto
# Tema: Bucles, Cadenas y Diccionarios.
# Contexto: El análisis de texto es fundamental para procesamiento de datos en servicios API.
# Requerimientos:Solicitar al usuario una frase o párrafo largo.Limpiar el texto: convertir a minúsculas y remover signos de puntuación básicos (,, ., ;, !).Crear un diccionario de frecuencias donde las llaves sean las palabras únicas y los valores sean la cantidad de veces que aparece cada palabra.Identificar e imprimir la palabra con mayor frecuencia y su conteo.


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