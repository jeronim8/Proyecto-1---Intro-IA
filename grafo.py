class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n):
        #inserte su codigo aqui
        return H[n] # puede retornar una lista con el calculo de la heuristica para cada estado

    def primero_profundidad(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
        
    def primero_anchura(self, nodo_inicio, nodo_final):

        nodos_expandidos = [] #Se define una lista para la serie de nodos a expandir
        padres = {} #Este diccionario se incluye para mantener trazabilidad de los predecesores de cada nodo tras su expansión, de modo que se pueda reconstruir la ruta del BFS al final.

        from collections import deque #Se incluye esta librería para el manejo de colas correspondiente al BFS.
        cola = deque()
        cola.append(nodo_inicio) #Se crea la cola a utilizar para el BFS, y se agrega el primer nodo.

        while len(cola) != 0: #Esta condición es fundamental para continuar evaluando, porque si la cola se encuentra vacía, no existen más nodos por expandir. En otras palabras, si se
            #vació la estructura y aún no se arriba al nodo final, entonces el laberinto no cuenta con solución, ya sea porque no existe salida o porque el laberinto genera un grafo no conexo.
            nodo_expansion = cola.popleft()
            nodos_expandidos.append(nodo_expansion) #Se expande el nodo siguiente de la cola.
            if nodo_expansion == nodo_final: #Si el nodo a expandir ya es la salida del laberinto, el bucle debe finalizar, puesto que se concluyó la búsqueda mediante BFS.
                break
            for vecino in self.obtener_vecinos(nodo_expansion):
                if vecino not in nodos_expandidos and vecino not in cola:
                    cola.append(vecino) #Se agregan a la cola todos los vecinos del nodo expandido que no hayan sido evaluados previamente, ni incluidos en la estructura FIFO.
                    padres[vecino] = nodo_expansion #Se asocia a cada nodo hijo con el padre del que se obtuvo, para luego reconstruir la ruta BFS.

        recorridoBFS_invertido = []
        if(nodos_expandidos[-1] == nodo_final): #Si efectivamente el BFS logró encontrar el nodo final, se reconstruye la ruta hacia él. De lo contrario, la lista de recorridoBFS_invertido permanece vacía, puesto que no existe ruta.
            nodo_actual = nodo_final
            while nodo_actual != nodo_inicio:
                recorridoBFS_invertido.append(nodo_actual)
                nodo_actual = padres[nodo_actual] #Sucesivamente, se comienza a reconstruir la ruta BFS desde el nodo final, a través de la sucesión almacenada en el diccionario de padres.
            recorridoBFS_invertido.append(nodo_inicio) #Al final se incluye el nodo inicio a la ruta.

        recorridoBFS = recorridoBFS_invertido[::-1] #Se invierte la lista obtenida para que que se retorne el recorrido en el orden adecuado.
        return recorridoBFS
    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
    