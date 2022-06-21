import numpy as np


def numberOfAvailableDifferentPaths(board, snake, depth):
    # Crear y rellenar la matriz que representa el tablero
    n, m = board
    board_matrix = [[0]*m for i in range(n)]     # board_matrix = np.zeros([n, m], dtype=int)
    for body_part in snake:
        board_matrix[body_part[0]][body_part[1]] = 1

    # Funcion auxiliar con más parámetros
    return numberOfAvailableDifferentPaths_aux(board, snake, depth, board_matrix, 0)


def numberOfAvailableDifferentPaths_aux(board, snake, depth, board_matrix, current_depth):
    n, m = board
    head = snake[0]
    tail = snake[len(snake)-1]

    # Si se ha alcanzado un camino de longitud = depth, se suma un camino encontrado al total
    if current_depth == depth:
        return 1

    else:
        different_paths = 0
        # Se calculan los 4 posibles movimientos (L, R, U, D)
        movements = [[head[0]-1, head[1]], [head[0]+1, head[1]], [head[0], head[1]+1], [head[0], head[1]-1]]

        # Se mueve la serpiente en las direcciones posibles
        for new_head in movements:
            board_matrix[tail[0]][tail[1]] = 0
            if n > new_head[0] and new_head[0] >= 0 and m > new_head[1] and new_head[1] >= 0 and board_matrix[new_head[0]][new_head[1]] == 0:
                # Efectuar movimiento
                board_matrix[new_head[0]][new_head[1]] = 1
                old_tail = snake[-1]
                snake = [new_head] + snake[:-1]

                # Calcular el resto del camino
                different_paths += numberOfAvailableDifferentPaths_aux(board, snake, depth, board_matrix, current_depth+1)

                # Deshacer este movimiento para poder hacer otras llamadas recursivas
                board_matrix[new_head[0]][new_head[1]] = 0
                snake = snake[1:] + [old_tail]
            board_matrix[tail[0]][tail[1]] = 1

        # Devolver el número de caminmos encontrados desde esta posición
        return different_paths
