
#recocido

from escenario import inicio, destino, entregas
import random
import math
import statistics
import time

# Calculamos la distancia entre dos puntos
def distancia(p1, p2):

    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Calculamos el costo total de las entregas
def calcular_costo(orden):

    costo = 0
    posicion = inicio

    for entrega in orden:
        costo += distancia(posicion, entrega)
        posicion = entrega

    costo += distancia(posicion, destino)

    return costo




def recocido_simulado():

    actual = entregas.copy()
    random.shuffle(actual)

    mejor = actual.copy()

    temperatura = 100
    enfriamiento = 0.95

    evaluaciones = 0

    while temperatura > 1:

        nuevo = actual.copy()

        # Cambiamos dos entregas
        a = random.randint(0, 2)
        b = random.randint(0, 2)

        nuevo[a], nuevo[b] = nuevo[b], nuevo[a]

        costo_actual = calcular_costo(actual)
        costo_nuevo = calcular_costo(nuevo)

        evaluaciones += 1

        # Aceptamos si mejora o mediante una probabilidad
        if costo_nuevo < costo_actual:

            actual = nuevo.copy()

        else:

            probabilidad = math.exp(
                (costo_actual - costo_nuevo) / temperatura
            )

            if random.random() < probabilidad:
                actual = nuevo.copy()

        # Guardamos la mejor solucion
        if calcular_costo(actual) < calcular_costo(mejor):
            mejor = actual.copy()

        # Reducimos la temperatura
        temperatura = temperatura * enfriamiento

    return mejor, calcular_costo(mejor), evaluaciones




def algoritmo_genetico():

    poblacion = []

    # Creamos una poblacion inicial
    for i in range(10):

        individuo = entregas.copy()
        random.shuffle(individuo)

        poblacion.append(individuo)

    evaluaciones = 0

    # Realizamos 50 generaciones
    for generacion in range(50):

        nueva_poblacion = []

        # Ordenamos las soluciones por su costo
        poblacion.sort(key=calcular_costo)

        evaluaciones += len(poblacion)

        # Conservamos la mejor solucion
        nueva_poblacion.append(poblacion[0].copy())

        while len(nueva_poblacion) < 10:

            # Seleccionamos dos padres
            padre1 = random.choice(poblacion[:5])
            padre2 = random.choice(poblacion[:5])

            # Realizamos la cruza
            hijo = [padre1[0]]

            for entrega in padre2:

                if entrega not in hijo:
                    hijo.append(entrega)

            # Realizamos la mutacion
            if random.random() < 0.3:

                a = random.randint(0, 2)
                b = random.randint(0, 2)

                hijo[a], hijo[b] = hijo[b], hijo[a]

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    # Buscamos la mejor solucion final
    poblacion.sort(key=calcular_costo)

    return poblacion[0], calcular_costo(poblacion[0]), evaluaciones


resultados_recocido = []
resultados_genetico = []

tiempo_inicio = time.time()

for i in range(20):

    orden, costo, evaluaciones = recocido_simulado()

    resultados_recocido.append(costo)

tiempo_recocido = time.time() - tiempo_inicio


tiempo_inicio = time.time()

for i in range(20):

    orden, costo, evaluaciones = algoritmo_genetico()

    resultados_genetico.append(costo)

tiempo_genetico = time.time() - tiempo_inicio




print("\nResultados")
print("-" * 40)

print("\nRecocido")

print("Mejor costo:", min(resultados_recocido))
print("Costo promedio:", statistics.mean(resultados_recocido))
print("Desviacion estandar:", statistics.pstdev(resultados_recocido))
print("Tiempo:", round(tiempo_recocido, 5), "segundos")


print("\nAlgoritmo")

print("Mejor costo:", min(resultados_genetico))
print("Costo promedio:", statistics.mean(resultados_genetico))
print("Desviacion estandar:", statistics.pstdev(resultados_genetico))
print("Tiempo:", round(tiempo_genetico, 5), "segundos")


print("\nComparacioN")
print("-" * 40)

if min(resultados_recocido) < min(resultados_genetico):

    print("Recocido simulado encontro el menor costo.")

elif min(resultados_genetico) < min(resultados_recocido):

    print("El algoritmo genetico encontro el menor costo.")

else:

    print("Los dos algoritmos van al mismo.")
