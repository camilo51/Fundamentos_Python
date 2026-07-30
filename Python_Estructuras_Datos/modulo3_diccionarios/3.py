califs = {
    "Mates": 85,
    "Historia": 72
}

califs.update({
    "Inglés": 88,
    "Mates": 87,
    "Arte": 95
})

print(f"Calificaciones: {califs}")

vendido = califs.pop("Inglés")
print(f"Valor eliminado: {vendido}")
print(f"Diccionario: {califs}")

par_final = califs.popitem()
print(f"Último par eliminado: {par_final}")
print(f"Diccionario: {califs}")

contador = {}

contador.setdefault("hola", 0)
contador["hola"] += 1

print(f"Contador: {contador}")

materias = ["Mates", "Historia", "Arte"]

notas = dict.fromkeys(materias, 0)

print(f"Notas: {notas}")

d1 = {
    "nombre": "Carlos",
    "edad": 28
}

d2 = {
    "email": "c@e.com"
}

unido = d1 | d2

print(f"Diccionario unido: {unido}")