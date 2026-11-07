
# Proyecto Final
# Minimax y poda alfa-beta

# Valores que representan los recursos disponibles
# MAX intenta conseguir el mayor valor
# MIN intenta conseguir el menor valor

arbol = [
    [3, 5, 6],
    [9, 1, 2],
    [7, 4, 8]
]

nodos_minimax = 0
nodos_alfa = 0
nodos_podados = 0


# ---------------------------------
# ALGORITMO MINIMAX
# ---------------------------------

def minimax(nivel, indice, maximizando):

    global nodos_minimax

    nodos_minimax += 1

    # Revisamos si llegamos al final
    if nivel == 2:
        return arbol[indice // 3][indice % 3]

    if maximizando:

        mejor = float("-inf")

        for i in range(3):

            valor = minimax(nivel + 1, indice * 3 + i, False)

            mejor = max(mejor, valor)

        return mejor

    else:

        mejor = float("inf")

        for i in range(3):

            valor = minimax(nivel + 1, indice * 3 + i, True)

            mejor = min(mejor, valor)

        return mejor


# ---------------------------------
# MINIMAX CON PODA ALFA-BETA
# ---------------------------------

def alfa_beta(nivel, indice, alfa, beta, maximizando):

    global nodos_alfa
    global nodos_podados

    nodos_alfa += 1

    # Revisamos si llegamos al final
    if nivel == 2:
        return arbol[indice // 3][indice % 3]

    if maximizando:

        mejor = float("-inf")

        for i in range(3):

            valor = alfa_beta(
                nivel + 1,
                indice * 3 + i,
                alfa,
                beta,
                False
            )

            mejor = max(mejor, valor)
            alfa = max(alfa, mejor)

            # Realizamos la poda
            if beta <= alfa:

                nodos_podados += 3 - i - 1
                break

        return mejor

    else:

        mejor = float("inf")

        for i in range(3):

            valor = alfa_beta(
                nivel + 1,
                indice * 3 + i,
                alfa,
                beta,
                True
            )

            mejor = min(mejor, valor)
            beta = min(beta, mejor)

            # Realizamos la poda
            if beta <= alfa:

                nodos_podados += 3 - i - 1
                break

        return mejor


# ---------------------------------
# EJECUTAMOS LOS DOS ALGORITMOS
# ---------------------------------

resultado_minimax = minimax(0, 0, True)

resultado_alfa = alfa_beta(
    0,
    0,
    float("-inf"),
    float("inf"),
    True
)


# ---------------------------------
# MOSTRAMOS LOS RESULTADOS
# ---------------------------------

print("RESULTADOS DE MINIMAX")
print("-" * 35)

print("Mejor resultado:", resultado_minimax)
print("Nodos visitados:", nodos_minimax)


print("\nRESULTADOS DE ALFA-BETA")
print("-" * 35)

print("Mejor resultado:", resultado_alfa)
print("Nodos visitados:", nodos_alfa)
print("Nodos podados:", nodos_podados)


# Comparamos los resultados
print("\nCOMPARACION")
print("-" * 35)

if resultado_minimax == resultado_alfa:

    print("Los dos algoritmos encontraron el mismo resultado.")

else:

    print("Los resultados son diferentes.")
