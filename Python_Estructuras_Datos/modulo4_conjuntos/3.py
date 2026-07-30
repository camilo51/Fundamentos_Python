grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Carlos", "Elena", "Fernando"}

comunes = grupo_a.intersection(grupo_b)
todos = grupo_a.union(grupo_b)
solo_en_a = grupo_a.difference(grupo_b)
exclusivos = grupo_a.symmetric_difference(grupo_b)

print(f"Elementos comunes: {comunes}")
print(f"Unión: {todos}")
print(f"Solo en grupo A: {solo_en_a}")
print(f"Elementos exclusivos: {exclusivos}")

vegetales = {"zanahoria", "pepino"}
frutas = {"manzana", "platano"}

print(f"¿No tienen elementos en común?: {vegetales.isdisjoint(frutas)}")

resultado = grupo_a.intersection(grupo_b).difference({"Elena"})

print(f"Resultado del encadenamiento: {resultado}")