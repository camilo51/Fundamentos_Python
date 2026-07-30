numeros = [10, 20, 30, 40, 50, 60, 70]

primeros_tres = numeros[0:3]
del_1_al_3 = numeros[1:4]
hasta_tercero = numeros[:3]
desde_tercero = numeros[2:]
pares = numeros[::2]
ultimos_tres = numeros[-3:]
invertida = numeros[::-1]

print(numeros)

print(f"Primeros tres: {primeros_tres}")
print(f"Del 1 al 3: {del_1_al_3}")
print(f"Hasta el tercero: {hasta_tercero}")
print(f"Desde el tercero: {desde_tercero}")
print(f"Pares: {pares}")
print(f"Ultimos tres: {ultimos_tres}")
print(f"Invertida: {invertida}")