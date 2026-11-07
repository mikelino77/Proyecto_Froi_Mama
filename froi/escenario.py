
# Proyecto Final

#Mapa 12x12
mapa = [
    ["." for columna in range(12)]
    for fila in range(12)
]

# Definimos el punto de inicio y destino
inicio = (0, 0)
destino = (11, 11)

# Definimos los puntos de entrega
entregas = [
    (2, 3),
    (5, 7),
    (8, 4)
]

# Definimos los obstaculos
obstaculos = [
    (1, 2), (2, 2), (3, 2),
    (4, 5), (5, 5), (6, 5),
    (7, 8), (8, 8), (9, 8)
]

# Definimos las zonas con mayor costo
zonas_costosas = [
    (3, 4), (4, 4), (6, 7), (9, 5)
]

# Colocamos los obstaculos en el mapa
for fila, columna in obstaculos:
    mapa[fila][columna] = "ñ"

# Colocamos los puntos de entrega
for fila, columna in entregas:
    mapa[fila][columna] = "N"

# Colocamos las zonas costosas
for fila, columna in zonas_costosas:
    mapa[fila][columna] = "D"

# Colocamos el inicio y destino
mapa[inicio[0]][inicio[1]] = "I"
mapa[destino[0]][destino[1]] = "O"

# Mostramos el mapa
print("Mapa de la ciudad (12x12)")
print("-" * 35)

for fila in mapa:
    print(" ".join(fila))

print("-" * 35)

print("Inicio:", inicio)
print("Destino:", destino)
print("Entregas:", entregas)
print("Obstaculos:", len(obstaculos))
print("Zonas costosas:", len(zonas_costosas))
