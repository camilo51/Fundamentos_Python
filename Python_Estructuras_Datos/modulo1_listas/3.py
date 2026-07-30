tareas = ["estudiar", "ejercicio"]

tareas.append("programar")
tareas.insert(0, "llamar médico")
tareas.extend(["lavar ropa", "cocinar"])

print(tareas)

a = [1, 2, 3]
a.append([4, 5])
print(f"Con append: {a}")

a = [1, 2, 3]
a.extend([4, 5])
print(f"Con extend: {a}")