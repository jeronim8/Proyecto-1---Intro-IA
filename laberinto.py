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

        #Impresión de datos para verificación:8
        print("Fila salida: ", filaSalida)
        print("Columna salida: ", columnaSalida)
        print("Filas extraídas: ", len(matriz))

        if len(matriz) > 0:
            columnas2 = len(matriz[0])
            for fila in matriz:
                if len(fila) != columnas2:
                    print("Error: existe una fila con un número inadecuado de columnas.")
                    return None #Detiene la lectura de la matriz en caso de que se halle un error con el número de columnas.
            print("Columnas obtenidas: ", len(matriz[0]))

        #Retorno de número de filas, número de columnas y matriz.
        return coordenadaSalida, matriz


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

    for fila in range(filas):
        for columna in range(columnas):

            if matriz[fila][columna] == 1: #Las paredes no han de considerarse como nodos.
                continue

            nodo_actual = (fila, columna) #Se seleccionan las coordenadas de un nodo en el laberinto.
            grafo[nodo_actual] = [] #Se crea una nueva entrada para definir la lista de adyaciencia correspondiente al nodo_actual.

            for movimiento_fila, movimiento_columna in movimientos: #Se evalúan todos los potenciales vecinos del nodo analizado.
                nueva_fila = fila + movimiento_fila
                nueva_columna = columna + movimiento_columna

                if(0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and matriz[nueva_fila][nueva_columna] != 1): #Si su vecino se encuentra dentro de la matriz y no es una pared, entonces, agregarlo a la correspondiente lista de adyacencia.
                    vecino = (nueva_fila, nueva_columna)
                    grafo[nodo_actual].append(vecino)

    #Regresar la lista de adyacencia.
    return grafo