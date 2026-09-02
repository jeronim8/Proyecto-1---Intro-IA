import laberinto as l
from grafo import Grafo

nombre_archivo = input("Nombre del archivo de laberinto a cargar: ").strip()

try:
    resultado_lectura = l.leer_laberinto(nombre_archivo)
except FileNotFoundError:
    print(f"No se halló el archivo '{nombre_archivo}'.\n")
    raise SystemExit(1)

if resultado_lectura is None: #leer_laberinto ya reportó el motivo del error (columnas o falta de inicio/meta)
    raise SystemExit(1)

nodo_inicio, nodo_final, matriz = resultado_lectura

#Conversión de la matriz a grafo, mediante una lista de adyacencia:

lista_adyacencia = l.matriz_a_grafo(matriz)
grafo = Grafo(lista_adyacencia)

#Recorridos:

print("\nRecorrido DFS:\n")
ruta_dfs = grafo.primero_profundidad(nodo_inicio, nodo_final)
if ruta_dfs:
    print("Ruta encontrada (DFS), longitud:", len(ruta_dfs))
    print(ruta_dfs)
else:
    print("No se encontró una ruta mediante DFS.")

print("\nRecorrido BFS:\n")
ruta_bfs = grafo.primero_anchura(nodo_inicio, nodo_final)
if ruta_bfs:
    print("Ruta encontrada (BFS), longitud:", len(ruta_bfs))
    print(ruta_bfs)
else:
    print("No se encontró una ruta mediante BFS.")

print("\nRecorrido A*:\n")
ruta_a_estrella = grafo.a_estrella(nodo_inicio, nodo_final)
if ruta_a_estrella:
    print("Ruta encontrada (A*), longitud:", len(ruta_a_estrella))
    print(ruta_a_estrella, "\n")
else:
    print("No se encontró una ruta mediante A*.\n")