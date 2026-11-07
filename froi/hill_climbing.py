
# Busqueda local con Hill Climbing

from escenario import inicio, destino, entregas
import random

# Calculamos la distancia entre dos puntos
def distancia(punto1, punto2):

    fila1, columna1 = punto1
    fila2, columna2 = punto2

    return abs(fila1 - fila2) + abs(columna1 - columna2)


# Calculamos el costo de visitar las entregas
def calcular_costo(orden):

    costo = 0
    posicion = inicio

    for entrega in orden:
        costo += distancia(posicion, entrega)
        posicion = entrega

    costo += distancia(posicion, destino)

    return costo


# Intercambiamos dos entregas para crear una nueva solucion
def cambiar_orden(orden):

    nuevo = orden.copy()

    posicion1 = random.randint(0, len(nuevo) - 1)
    posicion2 = random.randint(0, len(nuevo) - 1)

    nuevo[posicion1], nuevo[posicion2] = nuevo[posicion2], nuevo[posicion1]

    return nuevo


# Funcion principal de Hill Climbing
def hill_climbing():

    mejor_orden = entregas.copy()
    random.shuffle(mejor_orden)

    mejor_costo = calcular_costo(mejor_orden)

    # Probamos diferentes soluciones
    for intento in range(100):

        nuevo_orden = cambiar_orden(mejor_orden)
        nuevo_costo = calcular_costo(nuevo_orden)

        # Conservamos la solucion si mejora el costo
        if nuevo_costo < mejor_costo:

            mejor_orden = nuevo_orden
            mejor_costo = nuevo_costo

    return mejor_orden, mejor_costo


# Realizamos 10 ejecuciones
mejor_resultado = None
mejor_costo = float("inf")

print("RESULTADOS DE HILL CLIMBING")
print("-" * 35)

for i in range(10):

    orden, costo = hill_climbing()

    print("\nEjecucion:", i + 1)
    print("Orden de entregas:", orden)
    print("Costo total:", costo)

    if costo < mejor_costo:

        mejor_costo = costo
        mejor_resultado = orden


# Mostramos la mejor solucion
print("\nMEJOR RESULTADO")
print("-" * 35)

print("Mejor orden:", mejor_resultado)
print("Menor costo:", mejor_costo)
