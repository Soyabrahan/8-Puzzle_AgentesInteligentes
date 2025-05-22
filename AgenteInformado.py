#Agente informado usando A*
# AGENTE DE BUSQUEDA INFORMADA *A
#--->Importaciones<---
from IDDFS import obtener_vecinos  # Importa la función obtener_vecinos del archivo iddfs.py

objetivo = [1, 2, 3, 8, 0, 4, 7, 6, 5]   # Estado objetivo del puzzle

def heuristica_manhattan(estado):
    distancia = 0  # Inicializa la distancia total en 0
    for i, valor in enumerate(estado):  # Recorre cada casilla y su valor
        if valor == 0:  # Si es el espacio vacío, lo ignora
            continue
        objetivo_i = objetivo.index(valor)  # Busca la posición real del valor en el objetivo
        x1, y1 = i // 3, i % 3  # Coordenadas actuales del valor
        x2, y2 = objetivo_i // 3, objetivo_i % 3  # Coordenadas objetivo del valor
        distancia += abs(x1 - x2) + abs(y1 - y2)  # Suma la distancia de Manhattan
    return distancia  # Devuelve la distancia total

import heapq  # Importa heapq para la cola de prioridad

nodos_expandidos = 0  # Variable global

def a_estrella(inicial):
    global nodos_expandidos
    nodos_expandidos = 0  # Reinicia el contador
    frontera = []  # Cola de prioridad para los nodos a explorar
    heapq.heappush(frontera, (heuristica_manhattan(inicial), 0, inicial, []))  # Inserta el estado inicial en la frontera (f, g, estado, camino)
    visitados = set()  # Conjunto de estados visitados

    while frontera:  # Mientras haya nodos por explorar
        f, g, actual, camino = heapq.heappop(frontera)  # Extrae el nodo con menor costo f
        nodos_expandidos += 1  # Cuenta cada vez que expandes un nodo

        if actual == objetivo:  # Si el estado actual es el objetivo
            return camino + [actual]  # Devuelve el camino hasta el objetivo

        visitados.add(tuple(actual))  # Marca el estado actual como visitado

        for vecino in obtener_vecinos(actual):  # Para cada vecino del estado actual
            if tuple(vecino) not in visitados:  # Si el vecino no ha sido visitado
                nuevo_camino = camino + [actual]  # Crea el nuevo camino agregando el estado actual
                nuevo_g = g + 1  # Incrementa el costo g (profundidad)
                nuevo_f = nuevo_g + heuristica_manhattan(vecino)  # Calcula el nuevo costo f
                heapq.heappush(frontera, (nuevo_f, nuevo_g, vecino, nuevo_camino))  # Inserta el vecino en la frontera

    return None  # Si no se encuentra solución, devuelve None
