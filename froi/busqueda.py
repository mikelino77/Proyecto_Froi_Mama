
# Busqueda de rutas con Greedy y A*

from escenario import mapa, inicio, destino

# Calculamos la distancia Manhattan
def heuristica(posicion):
    fila, columna = posicion
    return abs(fila - destino[0]) + abs(columna - destino[1])


# Funcion para buscar una ruta
def buscar_ruta(algoritmo):

    abiertos = [inicio]
    cerrados = []

    costos = {inicio: 0}
    padres = {}

    nodos = 0

    while abiertos:

        # Elegimos el siguiente punto
        if algoritmo == "Greedy":
            actual = min(abiertos, key=heuristica)
        else:
            actual = min(
                abiertos,
                key=lambda punto: costos[punto] + heuristica(punto)
            )

        abiertos.remove(actual)
        nodos += 1

        # Revisamos si llegamos al destino
        if actual == destino:

            ruta = []
            punto = destino

            while punto != inicio:
                ruta.append(punto)
                punto = padres[punto]

            ruta.append(inicio)
            ruta.reverse()

            return ruta, costos[destino], nodos

        cerrados.append(actual)

        fila, columna = actual

        # Movimientos permitidos: arriba, abajo, izquierda y derecha
        movimientos = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for movimiento in movimientos:

            nueva_fila = fila + movimiento[0]
            nueva_columna = columna + movimiento[1]

            vecino = (nueva_fila, nueva_columna)

            # Verificamos que el movimiento este dentro del mapa
            if 0 <= nueva_fila < 12 and 0 <= nueva_columna < 12:

                # Evitamos pasar por obstaculos
                if mapa[nueva_fila][nueva_columna] != "X":

                    if vecino not in cerrados:

                        # Calculamos el costo del movimiento
                        costo = 3 if mapa[nueva_fila][nueva_columna] == "$" else 1

                        nuevo_costo = costos[actual] + costo

                        if vecino not in costos or nuevo_costo < costos[vecino]:

                            costos[vecino] = nuevo_costo
                            padres[vecino] = actual

                            if vecino not in abiertos:
                                abiertos.append(vecino)

    return None, 0, nodos


# Ejecutamos Greedy
ruta_greedy, costo_greedy, nodos_greedy = buscar_ruta("Greedy")

# Ejecutamos A*
ruta_a, costo_a, nodos_a = buscar_ruta("A*")


# Mostramos los resultados
print("\nResultados de la busqueda de rutas")
print("-" * 35)

print("\nGreddy")

if ruta_greedy:
    print("Ruta encontrada:", ruta_greedy)
    print("Costo:", costo_greedy)
    print("Nodos revisados:", nodos_greedy)
else:
    print("No se encontro una ruta")


print("\nALGORITMO A*")

if ruta_a:
    print("Ruta encontrada:", ruta_a)
    print("Costo:", costo_a)
    print("Nodos revisados:", nodos_a)
else:
    print("No se encontro una ruta")


# Comparamos los resultados
print("\nCOMPARACION")
print("-" * 35)

if ruta_greedy and ruta_a:

    if costo_a <= costo_greedy:
        print("A* encontro una ruta de menor o igual costo.")
    else:
        print("Greedy encontro una ruta de menor costo.")

print("Greedy reviso:", nodos_greedy, "nodos")
print("A* reviso:", nodos_a, "nodos")
