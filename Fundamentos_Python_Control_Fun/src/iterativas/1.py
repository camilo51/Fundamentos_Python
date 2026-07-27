nombre = input("Ingrese su nombre: ")
proyectos = int(input("Ingrese la cantidad de proyectos asignados: "))

total_horas = 0
horas_array = []
for i in range(proyectos):
    horas = int(input(f"Ingrese las horas dedicadas al proyecto {i+1}: "))
    total_horas += horas
    horas_array.append(horas)

promedio_horas = total_horas / proyectos

print("\nReporte de Horas Trabajadas")
print(f"Nombre: {nombre}")
print(f"Total de horas trabajadas: {total_horas}")
print(f"Promedio de horas por proyecto: {promedio_horas}")
print("\nPorcentaje de horas por proyecto:")
for i in range(proyectos):
    porcentaje = (horas_array[i] / total_horas) * 100
    print(f"Proyecto {i+1}: {porcentaje:.2f}%")


