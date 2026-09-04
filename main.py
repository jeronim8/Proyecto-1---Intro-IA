"""
Archivo main.py
--------------------------
Proyecto 1
Introducción a la IA
--------------------------
Presentado por:
Jerónimo Ochoa Cruz
Valeria Herrera
Gustavo Aguilar
Pedro Cristos
--------------------------
2 de septiembre del 2026
"""

import laberinto as l
from grafo import Grafo

nombre_archivo = input("Nombre del archivo de laberinto a cargar: ").strip() #Se solicita al usuario, a través de la líniea de comandos, que ingrese el nombre del archivo a partir del cual se desea realizar la búsqueda de senderos solución.

try:
    resultado_lectura = l.leer_laberinto(nombre_archivo)
except FileNotFoundError:
    print(f"\nNo se halló el archivo '{nombre_archivo}'.\n") #Si el archivo referenciado no se encuentra, se emite un mensaje de error y finaliza el programa.
    raise SystemExit(1)
except ValueError:
    print(f"\nError: '{nombre_archivo}' no contiene los datos en el formato esperado.\n") #Si la lectura de la matriz falla porque el formato de los datos no es pertinente, se comunica la falla al usuario y se culmina la ejecución del sistema.
    raise SystemExit(1)

if resultado_lectura is None: #leer_laberinto ya reportó el motivo del error (columnas o falta de inicio/meta)
    raise SystemExit(1)

nodo_inicio, nodo_final, matriz = resultado_lectura

#Conversión de la matriz a grafo, mediante una lista de adyacencia:

lista_adyacencia = l.matriz_a_grafo(matriz)
grafo = Grafo(lista_adyacencia)

for nodo, vecinos in grafo.lista_adyacencia.items():
    print(f"{nodo}: {vecinos}")


#Aplicación de los algoritmos de recorrido:
#En cada uno, si no se obtiene una ruta desde el nodo inicio al nodo final, se presenta una línea que establece la inexistencia de solución.

print("\nRecorrido DFS:\n")
ruta_dfs, longitud_dfs = grafo.primero_profundidad(nodo_inicio, nodo_final)
if ruta_dfs:
    print("Ruta encontrada (DFS) - longitud:", longitud_dfs, "- número de nodos relevantes transitados:", len(ruta_dfs))
    print(ruta_dfs)
else:
    print("No se encontró una ruta mediante DFS.")

print("\nRecorrido BFS:\n")
ruta_bfs, longitud_bfs = grafo.primero_anchura(nodo_inicio, nodo_final)
if ruta_bfs:
    print("Ruta encontrada (BFS) - longitud:", longitud_bfs, "- número de nodos relevantes recorridos:", len(ruta_bfs))
    print(ruta_bfs)
else:
    print("No se encontró una ruta mediante BFS.")

print("\nRecorrido A*:\n")
ruta_a_estrella, longitud_a_estrella = grafo.a_estrella(nodo_inicio, nodo_final)
if ruta_a_estrella:
    print("Ruta encontrada (A*) - longitud:", longitud_a_estrella, "- número de nodos relevantes frecuentados:", len(ruta_a_estrella))
    print(ruta_a_estrella, "\n")
else:
    print("No se encontró una ruta mediante A*.\n")