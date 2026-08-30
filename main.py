import laberinto as l
from grafo import Grafo

coordenadaSalida, matriz = l.leer_laberinto("laberinto2.txt") #Lectura de la matriz

#Impresión de datos para verificación:

for fila in matriz:
    print(fila)

lista_adyacencia = l.matriz_a_grafo(matriz)
for nodo, vecinos in lista_adyacencia.items():
    print(nodo, "->", vecinos)

grafo = Grafo(lista_adyacencia)

