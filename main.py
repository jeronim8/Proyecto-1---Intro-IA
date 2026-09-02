import laberinto as l
from grafo import Grafo

nombre_archivo = input("Nombre del archivo de laberinto a cargar: ").strip()

try:
    resultado = l.leer_laberinto(nombre_archivo)
except FileNotFoundError:
    print(f"No se encontró el archivo '{nombre_archivo}'.")
    raise SystemExit(1)

if resultado is None: #leer_laberinto ya reportó el motivo del error (columnas o falta de inicio/meta).
    raise SystemExit(1)

coordenadaSalida, matriz = resultado

# Buscar en la matriz las celdas reales de inicio (2) y meta (3); leer_laberinto ya garantizó que ambas existen.
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

print("\nRecorrido DFS:\n")
ruta_dfs = grafo.primero_profundidad(nodo_inicio, nodo_final)
if ruta_dfs:
    print("Ruta encontrada (DFS), longitud:", len(ruta_dfs))
    print(ruta_dfs)
else:
    print("No se encontró una ruta.")

print("\nRecorrido BFS:\n")
ruta_bfs = grafo.primero_anchura(nodo_inicio, nodo_final)
if ruta_bfs:
    print("Ruta encontrada (BFS), longitud:", len(ruta_bfs))
    print(ruta_bfs)
else:
    print("No se encontró una ruta.")

print("\nRecorrido A*:\n")
ruta_a_estrella = grafo.a_estrella(nodo_inicio, nodo_final)
if ruta_a_estrella:
    print("Ruta encontrada (A*), longitud:", len(ruta_a_estrella))
    print(ruta_a_estrella)
else:
    print("No se encontró una ruta.")
