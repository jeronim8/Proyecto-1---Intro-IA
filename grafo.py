class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia
        self.heuristica = {}

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    """funcion de calculo de heuristica: construye la tabla Lista_heuristica
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
       #inserte si codigo aqui
        return None
        
    def primero_anchura(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
    