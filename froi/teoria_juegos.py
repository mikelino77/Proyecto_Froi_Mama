
# Cada numero representa los puntos de cada empresa

recompensas = {
    ("A", "A"): (5, 5),
    ("A", "B"): (3, 7),
    ("A", "C"): (2, 6),

    ("B", "A"): (7, 3),
    ("B", "B"): (6, 6),
    ("B", "C"): (4, 5),

    ("C", "A"): (6, 2),
    ("C", "B"): (5, 4),
    ("C", "C"): (8, 8)
}

estrategias = ["A", "B", "C"]

# Mostramos la matriz de recompensas
print("MATRIZ DE RECOMPENSAS")
print("-" * 45)

for estrategia1 in estrategias:

    for estrategia2 in estrategias:

        puntos = recompensas[(estrategia1, estrategia2)]

        print("Empresa 1:", estrategia1,
              "| Empresa 2:", estrategia2,
              "| Puntos:", puntos)


# Buscamos las mejores respuestas
print("\nMEJORES RESPUESTAS")
print("-" * 45)

for estrategia2 in estrategias:

    mejor_punto = max(
        recompensas[(estrategia1, estrategia2)][0]
        for estrategia1 in estrategias
    )

    for estrategia1 in estrategias:

        if recompensas[(estrategia1, estrategia2)][0] == mejor_punto:

            print("Empresa 1 prefiere:",
                  estrategia1,
                  "cuando Empresa 2 elige:",
                  estrategia2)


for estrategia1 in estrategias:

    mejor_punto = max(
        recompensas[(estrategia1, estrategia2)][1]
        for estrategia2 in estrategias
    )

    for estrategia2 in estrategias:

        if recompensas[(estrategia1, estrategia2)][1] == mejor_punto:

            print("Empresa 2 prefiere:",
                  estrategia2,
                  "cuando Empresa 1 elige:",
                  estrategia1)


# Buscamos el equilibrio de Nash
print("\nEQUILIBRIO DE NASH")
print("-" * 45)

encontrado = False

for estrategia1 in estrategias:

    for estrategia2 in estrategias:

        puntos = recompensas[(estrategia1, estrategia2)]

        mejor1 = max(
            recompensas[(otra, estrategia2)][0]
            for otra in estrategias
        )

        mejor2 = max(
            recompensas[(estrategia1, otra)][1]
            for otra in estrategias
        )

        # Comprobamos si ninguno quiere cambiar su decision
        if puntos[0] == mejor1 and puntos[1] == mejor2:

            print("Equilibrio encontrado:")
            print("Empresa 1:", estrategia1)
            print("Empresa 2:", estrategia2)
            print("Recompensas:", puntos)

            encontrado = True

if not encontrado:

    print("No existe equilibrio de Nash puro.")
