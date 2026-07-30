tecnologias = {"Python", "JavaScript", "SQL"}

tecnologias.add("Java")
tecnologias.update(["Go", "Rust"])

print(f"Tecnologías: {tecnologias}")

frutas = {"manzana", "naranja", "plátano"}

frutas.remove("naranja")
print(f"Después de remove(): {frutas}")

frutas.discard("kiwi")
print(f"Después de discard(): {frutas}")

elemento = frutas.pop()
print(f"Elemento eliminado: {elemento}")
print(f"Conjunto: {frutas}")

frutas.clear()
print(f"Conjunto vacío: {frutas}")

pares = {2, 4, 6, 8}
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(f"¿pares es subconjunto de numeros?: {pares.issubset(numeros)}")
print(f"¿numeros es superconjunto de pares?: {numeros.issuperset(pares)}")