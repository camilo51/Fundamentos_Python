def buscar_por_director(catalogo, director_buscar):
    coincidencias = ()

    for pelicula in catalogo:
        if pelicula[1] == director_buscar:
            coincidencias += (pelicula,)

    return coincidencias

def obtener_estadisticas(catalogo):
    puntuaciones = ()

    for pelicula in catalogo:
        puntuaciones += (pelicula[3],)

    minima = min(puntuaciones)
    maxima = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)

    return minima, maxima, promedio

catalogo = (
    ("Interestelar", "Christopher Nolan", 2014, 9.0),
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Parásitos", "Bong Joon-ho", 2019, 8.6),
    ("Avatar", "James Cameron", 2009, 7.9)
)

print("Catálogo")

for titulo, director, año, puntuacion in catalogo:
    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {año}")
    print(f"Puntuación: {puntuacion}")
    print()

primera_pelicula, *resto = catalogo

print(f"Primera película: {primera_pelicula}")
print(f"Resto: {resto}")

coincidencias = buscar_por_director(catalogo, "Bong Joon-ho")

print("\nPelículas del director:")

for pelicula in coincidencias:
    print(pelicula)

minima, maxima, promedio = obtener_estadisticas(catalogo)

print(f"\nPuntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Promedio: {promedio:.2f}")