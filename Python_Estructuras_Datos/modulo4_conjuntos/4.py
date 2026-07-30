u1 = {"acción", "comedia", "ciencia ficción", "aventura"}
u2 = {"drama", "comedia", "romance", "documental"}
u3 = {"acción", "aventura", "fantasía", "ciencia ficción"}

comunes_1_3 = u1 & u3
todos_1_2 = u1 | u2
solo_u1 = u1 - u2
excl_2_3 = u2 ^ u3

print(f"Comunes entre u1 y u3: {comunes_1_3}")
print(f"Unión de u1 y u2: {todos_1_2}")
print(f"Solo en u1: {solo_u1}")
print(f"Exclusivos entre u2 y u3: {excl_2_3}")

print(f"¿u3 es subconjunto de u1?: {u3 <= u1}")
print(f"¿{{2, 4}} es subconjunto de {{1, 2, 3, 4, 5}}?: { {2, 4} <= {1, 2, 3, 4, 5} }")