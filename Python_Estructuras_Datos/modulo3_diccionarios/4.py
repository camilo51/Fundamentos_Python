califs = {
    "Mates": 85,
    "Historia": 72,
    "Ciencias": 90
}

for materia, nota in califs.items():
    print(f"{materia}: {nota}")

print()

for materia in sorted(califs):
    print(f"{materia}: {califs[materia]}")

print()

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

for clave in list(diccionario.keys()):
    if clave == "b":
        del diccionario[clave]

print(f"Diccionario: {diccionario}")