import csv

# Importamos todos los programas
import busqueda
import hill_climbing
import recocido_genetico
import teoria_juegos
import minimax


print(" Sistemas")

print("\nTodos los programas se ejecutaron.")


# Creamos el archivo para guardar resultados
with open("resultados.csv", "w", newline="", encoding="utf-8-sig") as archivo:

    escritor = csv.writer(archivo)

    # Encabezados del archivo CSV
    escritor.writerow([
        "Algoritmo",
        "Mejor costo",
        "Promedio",
        "Desviacion estandar",
        "Nodos visitados",
        "Tiempo en segundos",
        "Resultado"
    ])

    # Resultados de Greedy
    escritor.writerow([
        "Greedy",
        busqueda.costo_greedy,
        "",
        "",
        busqueda.nodos_greedy,
        "",
        str(busqueda.ruta_greedy)
    ])

    # Resultados de A*
    escritor.writerow([
        "A*",
        busqueda.costo_a,
        "",
        "",
        busqueda.nodos_a,
        "",
        str(busqueda.ruta_a)
    ])

    # Resultados de Hill Climbing
    escritor.writerow([
        "Hill Climbing",
        hill_climbing.mejor_costo,
        "",
        "",
        "",
        "",
        str(hill_climbing.mejor_resultado)
    ])

    # Resultados de Recocido Simulado
    escritor.writerow([
        "Recocido Simulado",
        min(recocido_genetico.resultados_recocido),
        sum(recocido_genetico.resultados_recocido) / 20,
        "",
        "",
        recocido_genetico.tiempo_recocido,
        "20 ejecuciones"
    ])

    # Resultados del Algoritmo Genetico
    escritor.writerow([
        "Algoritmo Genetico",
        min(recocido_genetico.resultados_genetico),
        sum(recocido_genetico.resultados_genetico) / 20,
        "",
        "",
        recocido_genetico.tiempo_genetico,
        "20 ejecuciones"
    ])

    # Buscamos el equilibrio de Nash
    equilibrios = []

    for estrategia1 in teoria_juegos.estrategias:

        for estrategia2 in teoria_juegos.estrategias:

            puntos = teoria_juegos.recompensas[
                (estrategia1, estrategia2)
            ]

            mejor1 = max(
                teoria_juegos.recompensas[(otra, estrategia2)][0]
                for otra in teoria_juegos.estrategias
            )

            mejor2 = max(
                teoria_juegos.recompensas[(estrategia1, otra)][1]
                for otra in teoria_juegos.estrategias
            )

            if puntos[0] == mejor1 and puntos[1] == mejor2:

                equilibrios.append(
                    (estrategia1, estrategia2, puntos)
                )

    escritor.writerow([
        "Teoria de juegos",
        "",
        "",
        "",
        "",
        "",
        str(equilibrios)
    ])

    # Resultados de Minimax
    escritor.writerow([
        "Minimax",
        minimax.resultado_minimax,
        "",
        "",
        minimax.nodos_minimax,
        "",
        "Resultado de la busqueda"
    ])

    # Resultados de Alfa-Beta
    escritor.writerow([
        "Alfa-Beta",
        minimax.resultado_alfa,
        "",
        "",
        minimax.nodos_alfa,
        "",
        "Nodos podados: " + str(minimax.nodos_podados)
    ])


# Mensaje final
print(" PROYECTO FROI")

