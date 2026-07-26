while True:
    print("\n===== MENÚ DE EJERCICIOS =====")
    print("1. Puntaje total de un jugador")
    print("2. Tiempo total de juego")
    print("3. Daño total")
    print("4. Experiencia total")
    print("5. Porcentaje de vida")
    print("6. Oro total")
    print("7. Velocidad promedio")
    print("8. Costo de mejoras")
    print("9. Tiempo restante")
    print("10. Nivel promedio")
    print("11. Daño crítico")
    print("12. Minutos a horas")
    print("13. Porcentaje de misiones")
    print("14. Costo de objetos")
    print("15. Tiempo promedio")
    print("16. Porcentaje de enemigos derrotados")
    print("0. Salir")

    opcion = int(input("\nSeleccione una opción: "))

    match opcion:
        case 1:
            print("\n--- Ejercicio 1 ---")
            nivel1 = int(input("Puntos del nivel 1: "))
            nivel2 = int(input("Puntos del nivel 2: "))
            nivel3 = int(input("Puntos del nivel 3: "))

            total = nivel1 + nivel2 + nivel3
            print("Puntaje total:", total)

        case 2:
            print("\n--- Ejercicio 2 ---")
            horas = int(input("Horas: "))
            minutos = int(input("Minutos: "))
            segundos = int(input("Segundos: "))

            total_segundos = horas * 3600 + minutos * 60 + segundos
            print("Tiempo total en segundos:", total_segundos)

        case 3:
            print("\n--- Ejercicio 3 ---")
            ataque1 = int(input("Daño del ataque 1: "))
            ataque2 = int(input("Daño del ataque 2: "))
            ataque3 = int(input("Daño del ataque 3: "))

            total = ataque1 + ataque2 + ataque3
            print("Daño total:", total)

        case 4:
            print("\n--- Ejercicio 4 ---")
            mision1 = int(input("Experiencia misión 1: "))
            mision2 = int(input("Experiencia misión 2: "))
            mision3 = int(input("Experiencia misión 3: "))

            total = mision1 + mision2 + mision3
            print("Experiencia total:", total)

        case 5:
            print("\n--- Ejercicio 5 ---")
            vida_maxima = float(input("Vida máxima: "))
            vida_actual = float(input("Vida actual: "))

            porcentaje = (vida_actual / vida_maxima) * 100
            print("Porcentaje de vida restante:", round(porcentaje, 2), "%")

        case 6:
            print("\n--- Ejercicio 6 ---")
            oro1 = int(input("Oro misión 1: "))
            oro2 = int(input("Oro misión 2: "))
            oro3 = int(input("Oro misión 3: "))

            total = oro1 + oro2 + oro3
            print("Oro total:", total)

        case 7:
            print("\n--- Ejercicio 7 ---")
            distancia = float(input("Distancia recorrida: "))
            tiempo = float(input("Tiempo empleado: "))

            velocidad = distancia / tiempo
            print("Velocidad promedio:", round(velocidad, 2))

        case 8:
            print("\n--- Ejercicio 8 ---")
            mejora1 = float(input("Costo mejora 1: "))
            mejora2 = float(input("Costo mejora 2: "))
            mejora3 = float(input("Costo mejora 3: "))

            total = mejora1 + mejora2 + mejora3
            print("Costo total:", total)

        case 9:
            print("\n--- Ejercicio 9 ---")
            tiempo_total = int(input("Tiempo total de la misión: "))
            tiempo_transcurrido = int(input("Tiempo transcurrido: "))

            restante = tiempo_total - tiempo_transcurrido
            print("Tiempo restante:", restante)

        case 10:
            print("\n--- Ejercicio 10 ---")
            jugador1 = int(input("Nivel del jugador 1: "))
            jugador2 = int(input("Nivel del jugador 2: "))
            jugador3 = int(input("Nivel del jugador 3: "))

            promedio = (jugador1 + jugador2 + jugador3) / 3
            print("Nivel promedio:", round(promedio, 2))

        case 11:
            print("\n--- Ejercicio 11 ---")
            danio_base = float(input("Daño base: "))
            multiplicador = float(input("Multiplicador crítico: "))

            danio_critico = danio_base * multiplicador
            print("Daño crítico:", danio_critico)

        case 12:
            print("\n--- Ejercicio 12 ---")
            minutos = int(input("Minutos jugados: "))

            horas = minutos // 60
            minutos_restantes = minutos % 60

            print("Horas:", horas)
            print("Minutos:", minutos_restantes)

        case 13:
            print("\n--- Ejercicio 13 ---")
            total_misiones = int(input("Total de misiones: "))
            misiones_completadas = int(input("Misiones completadas: "))

            porcentaje = (misiones_completadas / total_misiones) * 100
            print("Porcentaje completado:", round(porcentaje, 2), "%")

        case 14:
            print("\n--- Ejercicio 14 ---")
            objeto1 = float(input("Costo del objeto 1: "))
            objeto2 = float(input("Costo del objeto 2: "))
            objeto3 = float(input("Costo del objeto 3: "))

            total = objeto1 + objeto2 + objeto3
            print("Costo total:", total)

        case 15:
            print("\n--- Ejercicio 15 ---")
            partida1 = float(input("Tiempo de la partida 1: "))
            partida2 = float(input("Tiempo de la partida 2: "))
            partida3 = float(input("Tiempo de la partida 3: "))

            promedio = (partida1 + partida2 + partida3) / 3
            print("Tiempo promedio:", round(promedio, 2))

        case 16:
            print("\n--- Ejercicio 16 ---")
            total_enemigos = int(input("Total de enemigos: "))
            enemigos_derrotados = int(input("Enemigos derrotados: "))

            porcentaje = (enemigos_derrotados / total_enemigos) * 100
            print("Porcentaje de enemigos derrotados:", round(porcentaje, 2), "%")

        case 0:
            print("¡Hasta luego!")
            break

        case _:
            print("Opción no válida. Intente nuevamente.")