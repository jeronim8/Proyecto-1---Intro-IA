"""
Archivo laberinto.py
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

def leer_laberinto(nombre_archivo):

    matriz = []
    with open(nombre_archivo, "r") as archivo:
        #Lectura de la primera línea del arhcivo (las coordenadas de la salida del laberinto):
        coordFinal = archivo.readline().strip()
        coordFinal = coordFinal.strip("()") #Elimina los paréntesis que acompañan a las coordenadas de salida del laberinto.
        filaSalida, columnaSalida = map(int, coordFinal.split(",")) #Separa la dimensión en dos datos, los convierte en enteros y los asigna a las variables -filas- y -columnas-.
        coordenadaSalida = (filaSalida, columnaSalida)

        #Lectura de la matriz laberinto:
        for linea in archivo:
            linea = linea.strip()
            linea = linea.strip("[]")
            fila = list(map(int, linea.split(","))) #Lista con cada uno de los valores (convertidos a enteros) de cada fila de la matriz.
            matriz.append(fila) #Agrega fila por fila a la matriz del laberinto.

        if len(matriz) == 0:
            print("\nNo existe matriz para evaluar.\n")
            return None

        #Impresión de datos para verificación:
        print("\nFilas extraídas: ", len(matriz))

        if len(matriz) > 0:
            columnas2 = len(matriz[0])
            for fila in matriz:
                if len(fila) != columnas2:
                    print("Error: existe una fila con un número inadecuado de columnas.\n")
                    return None #Detiene la lectura de la matriz en caso de que se halle un error con el número de columnas.
            print("Columnas obtenidas: ", len(matriz[0]))

        #Se ubican en la matriz la celda de inicio (2) y la celda de meta (3). Para esa casilla destino, se evalúa si coincide con las coordenadas obtenidas en la primera línea del archivo.
        nodo_inicio = None
        nodo_final = None
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                if matriz[fila][columna] == 2:
                    nodo_inicio = (fila, columna)
                elif matriz[fila][columna] == 3:
                    nodo_final = (fila, columna)

        if nodo_inicio is None or nodo_final is None:
            print("\nError: el laberinto debe contener una celda de inicio (2) y una celda de meta (3).\n")
            return None #Detiene la lectura en caso de que falte la celda de inicio o de meta.

        if nodo_final != coordenadaSalida:
            print("\nError: la coordenada descrita al inicio del archivo como casilla final no coincide con la coordenada de la celda que contiene el número 3 en la matriz.\n")
            return None #Detiene la lectura bajo la situación en que la celda descrita como final y la verdadera casilla destino no sean consistentes.

        print("\nNodo inicio: ", nodo_inicio)
        print("Nodo meta: ", nodo_final)

        #Retorno de número de filas, número de columnas y matriz.
        return nodo_inicio, nodo_final, matriz

def recursion_vecinos(peso_arista, movimientos, matriz, coordenada_actual, coordenada_anterior, grafo):

    if coordenada_actual in grafo:
        return (coordenada_actual, peso_arista) #Si se arriba a otro nodo perteneciente al grafo, entonces se tiende una arista.

    fila_actual, columna_actual = coordenada_actual

    #Buscar la continuación del pasillo
    for movimiento_fila, movimiento_columna in movimientos:
        fila_vecino = fila_actual + movimiento_fila
        columna_vecino = columna_actual + movimiento_columna
        if (0 <= fila_vecino < len(matriz) and 0 <= columna_vecino < len(matriz[0]) and matriz[fila_vecino][columna_vecino] != 1):
            coordenada_vecino = (fila_vecino, columna_vecino)
            if coordenada_vecino == coordenada_anterior:
                continue #No retornar al flujo del que se proviene, para evitar bucles infinitos

            return recursion_vecinos(peso_arista + 1, movimientos, matriz, coordenada_vecino, coordenada_actual, grafo)

    return None

def matriz_a_grafo(matriz):

    grafo = {} #Establecer un diccionario vacío que contendrá las listas de adyacencia de los nodos del grafo.
    filas = len(matriz)
    columnas = len(matriz[0])

    movimientos = [
        (-1, 0), #Arriba
        (1, 0), #Abajo
        (0, -1), #Izquierda
        (0, 1), #Derecha
    ]

    #Cálculo de grados de las casillas de los grafos
    for fila in range(filas):
        for columna in range(columnas):

            if matriz[fila][columna] == 1:
                continue

            numero_vecinos = 0

            for movimiento_fila, movimiento_columna in movimientos:
                nueva_fila = fila + movimiento_fila
                nueva_columna = columna + movimiento_columna

                if (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and matriz[nueva_fila][nueva_columna] != 1):
                    numero_vecinos += 1

            if numero_vecinos != 2 or matriz[fila][columna] == 2 or matriz[fila][columna] == 3:
                grafo[(fila, columna)] = [] #Se incluyen al conjunto de nodos únicamente si son bifurcaciones o espacios terminales, o si se trata del inicio o el final

    #Creación de las listas de adyacencia para cada nodo:
    for nodo_actual in grafo:
        fila_n, columna_n = nodo_actual
        for movimiento_fila, movimiento_columna in movimientos:
            nueva_fila = fila_n + movimiento_fila
            nueva_columna = columna_n + movimiento_columna
            if (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and matriz[nueva_fila][nueva_columna] != 1):
                coordenada_actual = (nueva_fila, nueva_columna)
                nuevo_vecino = recursion_vecinos(1, movimientos, matriz, coordenada_actual, nodo_actual, grafo)
                if nuevo_vecino is not None:
                    grafo[nodo_actual].append(nuevo_vecino)
    
    #Regresar la lista de adyacencia.
    return grafo