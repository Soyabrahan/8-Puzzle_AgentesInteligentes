#MiniProyecto de trabar con dos inteligencias artificales que resuelvan el puzle 8
#usare la libreria pygame para la interfaz grafica

#--->LIBRERIAS<---
import pygame #Interfaz Grafica
import random #Aleatoriedad

#--->CONFIGURACION GENERAL<---
tamCasilla = 100 #Tamaño de la casilla
tamTablero = 3 #Tamaño del tablero
ancho = alto = tamCasilla * tamTablero #Ancho y alto del tablero
FPS = 30 #Frames por segundo
tamFuente = 48 #Tamaño de la fuente

#--->COLORES<---
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (197, 29, 52)

#-->Aleatoriedad del tablero<--
def CrearTablero():
    while True:
        tablero = list(range(9)) #Crea una lista de 0 a 8
        random.shuffle(tablero) #Mezcla la lista
        if esResoluble(tablero): #Si el tablero es resoluble
            return tablero #Devuelve el tablero
        
#-->Comprobar si el tablero es resoluble<--
def esResoluble(tablero):
    inv_count = 0 #Contador de inversiones
    for i in range(8): #Recorre el tablero
        for j in range(i + 1, 9): #Recorre el tablero
            if tablero[i] != 0 and tablero[j] != 0 and tablero[i] > tablero[j]: #Si el valor de la casilla es mayor que el de la siguiente
                inv_count += 1 #Aumenta el contador
    return inv_count % 2 == 0 #Devuelve True si el contador es par