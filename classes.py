class Node:
    def __init__(self, tablero, jugador, movimiento=None):
        self.tablero = tablero[:]              # Copia del estado actual del tablero (lista de 9 posiciones)
        self.jugador = jugador                 # 'X' o 'O', el jugador que generó este nodo
        self.movimiento = movimiento           # Posición del movimiento que llevó a este nodo (0-8)
        self.hijos = []                        # Lista de nodos hijos (jugadas siguientes posibles)
        self.valor = None                      # Valor evaluado por el algoritmo Minimax

    def es_hoja(self):
        # Un nodo es hoja si ya hay ganador o no hay espacios libres
        return self.ganador('X') or self.ganador('O') or ' ' not in self.tablero

    def ganador(self, jugador):
        # Comprobaciones de victoria: filas, columnas y diagonales
        combos = [(0,1,2), (3,4,5), (6,7,8),     # 3 Filas
                  (0,3,6), (1,4,7), (2,5,8),     # 3 Columnas
                  (0,4,8), (2,4,6)]              # 2 Diagonales
        return any(all(self.tablero[i] == jugador for i in combo) for combo in combos)
    
class Tree:
    def __init__(self, root):
        self.root = root
    
    def evaluar(self, node):
        # Valor numérico del estado: 1 si gana X, -1 si gana O, 0 si empate
        if node.ganador("X"):
            return 1
        elif node.ganador("O"):
            return -1
        else:
            return 0
    
    def construir(self, node):
        # Si el nodo actual es terminal (hoja), se evalúa directamente
        if node.es_hoja():
            node.valor = self.evaluar(node)
            return node.valor
        
        siguiente = "O" if node.jugador == "X" else "X" # Cambiar de jugador, es decir, alterna entre X y O
        
        # Generar todos los hijos posibles desde este nodo (cada jugada legal)
        for i in range(9):
            if node.tablero[i] == " ":
                nuevo_tablero = node.tablero[:]
                nuevo_tablero[i] = node.jugador
                hijo = Node(nuevo_tablero, siguiente, movimiento=i)
                self.construir(hijo)
                node.hijos.append(hijo)
        
        # Aplicar Minimax: seleccionar el mejor valor de los hijos
        valores = [h.valores for h in node.hijos]
        node.valor = max(valores) if node.jugador == "X" else min(valores)
        return node.valor