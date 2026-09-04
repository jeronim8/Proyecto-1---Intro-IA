"""
Archivo grafo.py
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

class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
        self.heuristica = {}

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    """Función de cálculo de heurística: construye la tabla Lista_heuristica
    que contiene la distancia Manhattan de cada nodo del grafo hacia el
    nodo meta. Es admisible y consistente puesto que su cálculo determina
    el número total de desplazamientos que se requieren para arribar al
    destino final. El hecho de haber incorporado un grafo con pesos variables
    en las aristas no modifica este principio esencial."""
    
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
        #Pila con tuplas (nodo_actual, camino_recorrido_hasta_ese_nodo). La inclusión del camino recorrido permite agregar trazabilidad frente a los caminos que se tienden, para luego reconstruir la ruta.
        pila = [(nodo_inicio, [nodo_inicio], 0)] #El 0 refleja el costo circunstancial de la ruta.
        visitados = {nodo_inicio}

        while pila: #Mientras la pila mantenga elementos, de modo que se finalice si no existen más nodos por explorar, aunque aún no se haya identificado la meta (caso grafo no conexo).
            nodo_actual, camino, costo = pila.pop()  #LIFO -> se explora en profundidad

            if nodo_actual == nodo_final:
                return camino, costo  #Se llegó a la meta, se retorna la ruta completa, que fue almacenada en la tupla del nodo objetivo, además del su costo asociado.

            for vecino, peso in self.obtener_vecinos(nodo_actual): #Ahora se concibe también el peso almacenado con cada nodo, dado que se trata de un grafo etiquetado.
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append((vecino, camino + [vecino], costo + peso)) #Expansi+on de los vecinos de cada nodo evaluado. La existencia del set visitados permite que no se ingeresen segmentos que no deberían considerarse, por haberse examinado o incluido a la pila previamente.
                    #La inclusión de un nuevo vecino también incluye el costo asociado para dirigirse a él.
        return None  #No existe una ruta entre inicio y final
        
    def primero_anchura(self, nodo_inicio, nodo_final):

        nodos_expandidos = [] #Se define una lista para la serie de nodos a expandir
        padres = {} #Este diccionario se incluye para mantener trazabilidad de los predecesores de cada nodo tras su expansión, de modo que se pueda reconstruir la ruta del BFS al final.
        costos = {nodo_inicio: 0} #Se involucra un diccionario de costos para preservar el valor real del recorrido efectuado mediante este algoritmo de búsqueda.

        from collections import deque #Se incluye esta librería para el manejo de colas correspondiente al BFS.
        cola = deque()
        cola.append(nodo_inicio) #Se crea la cola a utilizar para el BFS, y se agrega el primer nodo.

        while len(cola) != 0: #Esta condición es fundamental para continuar evaluando, porque si la cola se encuentra vacía, no existen más nodos por expandir. En otras palabras, si se
            #vació la estructura y aún no se arriba al nodo final, entonces el laberinto no cuenta con solución, ya sea porque no existe salida o porque el laberinto genera un grafo no conexo.
            nodo_expansion = cola.popleft()
            nodos_expandidos.append(nodo_expansion) #Se expande el nodo siguiente de la cola.
            if nodo_expansion == nodo_final: #Si el nodo a expandir ya es la salida del laberinto, el bucle debe finalizar, puesto que se concluyó la búsqueda mediante BFS.
                break
            for vecino, peso in self.obtener_vecinos(nodo_expansion):
                if vecino not in nodos_expandidos and vecino not in cola:
                    cola.append(vecino) #Se agregan a la cola todos los vecinos del nodo expandido que no hayan sido evaluados previamente, ni incluidos en la estructura FIFO.
                    padres[vecino] = nodo_expansion #Se asocia a cada nodo hijo con el padre del que se obtuvo, para luego reconstruir la ruta BFS.
                    costos[vecino] = costos[nodo_expansion] + peso #Se actualiza el costo de las rutas hasta cada nodo, para mantener trazabilidad de las longitudes de los caminos.

        recorridoBFS_invertido = []
        if(nodos_expandidos[-1] == nodo_final): #Si efectivamente el BFS logró encontrar el nodo final, se reconstruye la ruta hacia él. De lo contrario, la lista de recorridoBFS_invertido permanece vacía, puesto que no existe ruta.
            nodo_actual = nodo_final
            while nodo_actual != nodo_inicio:
                recorridoBFS_invertido.append(nodo_actual)
                nodo_actual = padres[nodo_actual] #Sucesivamente, se comienza a reconstruir la ruta BFS desde el nodo final, a través de la sucesión almacenada en el diccionario de padres.
            recorridoBFS_invertido.append(nodo_inicio) #Al final se incluye el nodo inicio a la ruta.

            recorridoBFS = recorridoBFS_invertido[::-1] #Se invierte la lista obtenida para que que se retorne el recorrido en el orden adecuado.
            return recorridoBFS, costos[nodo_final] #Únicamente si se identificó una ruta hasta el destino, se realiza este retorno, dado que depende de la existencia de una entrada asociada al nodo de cierre para su adecuada ejecución.
        
        return None #En caso de que no se haya identificado una ruta válida hasta nodo_final
    
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
                return ruta[::-1], g[nodo_final] #Se invierte para entregarla desde el inicio hasta la meta. Para la modificación de código solicitada, ahora también se retorna la longitud real del camino constituido por el algoritmo A*.

            if nodo_actual in cerrados: #El heap puede contener entradas obsoletas del mismo nodo con peor f(n); se ignoran.
                continue
            cerrados.add(nodo_actual)

            for vecino, peso in self.obtener_vecinos(nodo_actual):
                g_tentativo = g[nodo_actual] + peso #El costo del tramo ahora es el peso de la arista (longitud del pasillo hasta el siguiente nodo relevante).

                if vecino not in g or g_tentativo < g[vecino]: #Se encontró un camino más corto hacia vecino.
                    g[vecino] = g_tentativo
                    padres[vecino] = nodo_actual
                    heapq.heappush(heap, (g_tentativo + self.h(vecino), vecino))

        return None #Se agotó el heap sin alcanzar la meta: no existe ruta entre inicio y final.
    