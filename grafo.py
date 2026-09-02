class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
        self.heuristica = {}

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    """Función de cálculo de heurística: construye la tabla Lista_heuristica
    que contiene la distancia Manhattan de cada nodo del grafo hacia el
    nodo meta. Es admisible y consistente porque solo se permiten
    movimientos ortogonales (arriba, abajo, izquierda, derecha) con costo
    1, por lo que nunca sobreestima el costo real restante."""
    
    def calcular_heuristica(self, meta):
        fila_meta, columna_meta = meta
        self.heuristica = {
            nodo: abs(nodo[0] - fila_meta) + abs(nodo[1] - columna_meta)
            for nodo in self.lista_adyacencia
        }
        return self.heuristica

    # funcion heuristica: consulta la tabla ya calculada para el nodo n.
    def h(self, n):
        return self.heuristica[n]

    def primero_profundidad(self, nodo_inicio, nodo_final):
       # Pila con tuplas (nodo_actual, camino_recorrido_hasta_ese_nodo)
        pila = [(nodo_inicio, [nodo_inicio])]
        visitados = {nodo_inicio}

        while pila:
            nodo_actual, camino = pila.pop()  # LIFO -> se explora en profundidad

            if nodo_actual == nodo_final:
                return camino  # se llegó a la meta, se retorna la ruta completa

            for vecino in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append((vecino, camino + [vecino]))

        return None  # no existe una ruta entre inicio y final
        
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
        import heapq #Cola de prioridad: siempre extrae el nodo con menor f(n) = g(n) + h(n).

        self.calcular_heuristica(nodo_final) #Se asegura que la tabla de heurística esté calculada hacia el nodo_final actual.

        g = {nodo_inicio: 0} #Costo real acumulado desde el inicio hasta cada nodo conocido.
        padres = {} #Predecesores de cada nodo, para reconstruir la ruta al finalizar.
        cerrados = set() #Nodos ya expandidos de forma definitiva (con su menor costo confirmado).

        heap = [(self.h(nodo_inicio), nodo_inicio)] #Se inicia el heap con el nodo de inicio, priorizado por f(n).

        while heap:
            f_actual, nodo_actual = heapq.heappop(heap) #Se extrae el nodo con menor f(n) disponible.

            if nodo_actual == nodo_final: #Al expandir la meta con el menor f(n), se garantiza la ruta óptima.
                ruta = [nodo_actual]
                while nodo_actual != nodo_inicio:
                    nodo_actual = padres[nodo_actual]
                    ruta.append(nodo_actual) #Se reconstruye la ruta retrocediendo por los padres.
                return ruta[::-1] #Se invierte para entregarla desde el inicio hasta la meta.

            if nodo_actual in cerrados: #El heap puede contener entradas obsoletas del mismo nodo con peor f(n); se ignoran.
                continue
            cerrados.add(nodo_actual)

            for vecino in self.obtener_vecinos(nodo_actual):
                g_tentativo = g[nodo_actual] + 1 #Cada movimiento en el laberinto cuesta 1.

                if vecino not in g or g_tentativo < g[vecino]: #Se encontró un camino más corto hacia vecino.
                    g[vecino] = g_tentativo
                    padres[vecino] = nodo_actual
                    heapq.heappush(heap, (g_tentativo + self.h(vecino), vecino))

        return None #Se agotó el heap sin alcanzar la meta: no existe ruta entre inicio y final.
    