from classes import Node, Tree

def mejor_movimiento_arbol(tablero, jugador):
    """
    Calcula el mejor movimiento para el jugador dado,
    usando el árbol de juego con algoritmo Minimax.
    
    Parámetros:
        tablero (list): Lista de 9 elementos representando el tablero actual
        jugador (str): 'X' o 'O', el jugador que está tomando la decisión

    Retorna:
        int: índice del movimiento más favorable (0 a 8)
    """
    
    
    
    # Crear nodo raíz con el estado actual del tablero
    raiz = Node(tablero, jugador)
    
    # Construir el árbol completo a partir del nodo raíz
    arbol = Tree(raiz)
    arbol.construir(raiz)
    
    # Inicializar el mejor valor y movimiento
    mejor = None
    mejor_valor = -float("inf") if jugador == "X" else float("inf")
    
    # Evaluar los hijos (posibles movimientos)
    for hijo in raiz.hijos:
        if jugador == "X" and hijo.valor > mejor_valor:
            mejor = hijo
            mejor_valor = hijo.valor
        elif jugador == "O" and hijo.valor < mejor_valor:
            mejor = hijo
            mejor_valor = hijo.valor
    
    # Retornar el movimiento que llevó al mejor hijo
    return mejor.movimiento if mejor else None