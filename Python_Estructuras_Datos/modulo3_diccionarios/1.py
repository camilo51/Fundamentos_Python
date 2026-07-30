contactos = {
    "Ana": "612345678",
    "Carlos": "698765432"
}

print(f"Teléfono de Ana: {contactos['Ana']}")
print(f"Elena: {contactos.get('Elena', 'No encontrado')}")

valido = {
    "nombre": "Juan",
    42: "respuesta",
    (1, 2): "coord"
}

print(f"Diccionario válido: {valido}")

try:
    invalido = {[1, 2]: "x"}
except TypeError as e:
    print(f"Error: {e}")