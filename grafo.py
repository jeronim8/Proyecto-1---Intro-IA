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
       #inserte si codigo aqui
        return None
    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
    