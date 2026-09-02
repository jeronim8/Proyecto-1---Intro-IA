import laberinto as l
from grafo import Grafo

coordenadaSalida, matriz = l.leer_laberinto("laberinto.txt")

# Buscar en la matriz las celdas reales de salida (2) y meta (3)
nodo_inicio = None
nodo_final = None
for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
        if matriz[fila][columna] == 2:
            nodo_inicio = (fila, columna)
        elif matriz[fila][columna] == 3:
            nodo_final = (fila, columna)

lista_adyacencia = l.matriz_a_grafo(matriz)
grafo = Grafo(lista_adyacencia)

ruta = grafo.primero_profundidad(nodo_inicio, nodo_final)
if ruta:
    print("Ruta encontrada (DFS), longitud:", len(ruta))
    print(ruta)
else:
    print("No se encontró una ruta.")