#Agente que resuelve el puzzle 8 usando búsqueda primero en profundidad (DFS)
#Busqueda no informada

# Estado objetivo del puzzle 8
objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Función para obtener los vecinos (movimientos posibles) de un estado
def obtenerVecinos(estado):
    vecinos = []  # Lista para guardar los estados vecinos
    idx = estado.index(0)  # Encuentra la posición del espacio vacío (0)
    fila, col = idx // 3, idx % 3  # Calcula la fila y columna del espacio vacío
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos: arriba, abajo, izquierda, derecha

    for dr, dc in direcciones:  # Para cada dirección posible
        nf, nc = fila + dr, col + dc  # Nueva fila y columna después del movimiento
        if 0 <= nf < 3 and 0 <= nc < 3:  # Verifica que la nueva posición esté dentro del tablero
            new_idx = nf * 3 + nc  # Calcula el índice lineal del nuevo espacio
            new_estado = estado.copy()  # Copia el estado actual
            # Intercambia el espacio vacío con la casilla a mover
            new_estado[idx], new_estado[new_idx] = new_estado[new_idx], new_estado[idx]
            vecinos.append(new_estado)  # Agrega el nuevo estado a la lista de vecinos
    return vecinos  # Devuelve la lista de jugadas

# Búsqueda primero en profundidad (DFS) recursiva
def dfs(estado, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(tuple(estado))
    camino.append(estado)

    if estado == objetivo:
        return camino  # Solución encontrada

    for vecino in obtenerVecinos(estado):
        if tuple(vecino) not in visitados:
            resultado = dfs(vecino, visitados, camino.copy())
            if resultado:
                return resultado

    return None  # No se encontró solución desde este camino

