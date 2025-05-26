# Agente No Informado con IDDFS

# Estado objetivo del puzzle 8
objetivo = [1, 2, 3, 8, 0, 4, 7, 6, 5]  # Estado objetivo del puzzle 8

# Función para obtener vecinos (movimientos válidos) de un estado
def obtener_vecinos(estado):
    vecinos = []  # Lista para guardar los estados vecinos
    idx = estado.index(0)  # Encuentra la posición del espacio vacío (0)
    fila, col = idx // 3, idx % 3  # Calcula la fila y columna del espacio vacío
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos: arriba, abajo, izquierda, derecha

    for df, dc in direcciones:  # Para cada dirección posible
        nueva_fila, nueva_col = fila + df, col + dc  # Calcula la nueva posición del espacio vacío
        if 0 <= nueva_fila < 3 and 0 <= nueva_col < 3:  # Verifica que la nueva posición esté dentro del tablero
            nuevo_idx = nueva_fila * 3 + nueva_col  # Calcula el índice lineal del nuevo espacio
            nuevo_estado = estado.copy()  # Copia el estado actual
            # Intercambia el espacio vacío con la ficha vecina
            nuevo_estado[idx], nuevo_estado[nuevo_idx] = nuevo_estado[nuevo_idx], nuevo_estado[idx]
            vecinos.append(nuevo_estado)  # Agrega el nuevo estado a la lista de vecinos
    return vecinos  # Devuelve la lista de vecinos

nodos_expandidos = 0  # Variable global

# Búsqueda en profundidad limitada (DLS)
def dls(estado, limite, path):
    global nodos_expandidos
    nodos_expandidos += 1
    if estado == objetivo:
        return [estado]
    if limite == 0:
        return None

    for vecino in obtener_vecinos(estado):
        if vecino not in path:  # Evita ciclos en la rama actual
            resultado = dls(vecino, limite - 1, path + [vecino])  # Llama recursivamente a DLS
            if resultado:
                return [estado] + resultado
    return None  # Si no se encontró solución, devuelve None

# Búsqueda por profundización iterativa (IDDFS)
def iddfs(inicial, max_profundidad=30):
    global nodos_expandidos
    nodos_expandidos = 0  # Reinicia el contador antes de cada búsqueda
    for limite in range(max_profundidad):  # Prueba con límites de profundidad crecientes
        resultado = dls(inicial, limite, [inicial])  # Llama a DLS con el límite actual
        if resultado:  # Si se encontró solución
            return resultado  # Devuelve el camino
    return None  # Si no se encontró solución en ningún límite, devuelve None
