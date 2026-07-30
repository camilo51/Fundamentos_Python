colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")

print(f"Colores: {colores}")

claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]

persona = {clave: valor for clave, valor in zip(claves, valores)}

print(f"Persona: {persona}")

usuario = {
    "nombre": "Miguel",
    "edad": 30,
    "direccion": {
        "calle": "Calle Mayor",
        "ciudad": "Madrid"
    }
}

ciudad = usuario["direccion"]["ciudad"]

print(f"Ciudad: {ciudad}")