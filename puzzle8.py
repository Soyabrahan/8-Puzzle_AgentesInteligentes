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