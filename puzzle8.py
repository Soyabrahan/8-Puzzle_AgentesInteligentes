#MiniProyecto de trabar con dos inteligencias artificales que resuelvan el puzle 8
#usare la libreria pygame para la interfaz grafica

#--->LIBRERIAS<---
import pygame #Interfaz Grafica
import random #Aleatoriedad
import sys  #sistema

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

#-->Dibujar el tablero<--
def dibujar_tablero(pantalla, tablero, fuente):
    pantalla.fill(blanco)  # Rellena la pantalla de color blanco
    for i in range(9):  # Recorre cada casilla del tablero
        x = (i % tamTablero) * tamCasilla  # Calcula la posición x de la casilla
        y = (i // tamTablero) * tamCasilla  # Calcula la posición y de la casilla
        valor = tablero[i]  # Obtiene el valor de la casilla
        if valor != 0:  # Si la casilla no es el espacio vacío
            pygame.draw.rect(pantalla, rojo, (x, y, tamCasilla, tamCasilla))  # Dibuja el rectángulo azul
            texto = fuente.render(str(valor), True, blanco)  # Renderiza el número en blanco
            rect = texto.get_rect(center=(x + tamCasilla // 2, y + tamCasilla // 2))  # Centra el texto
            pantalla.blit(texto, rect)  # Dibuja el texto en la pantalla
        pygame.draw.rect(pantalla, negro, (x, y, tamCasilla, tamCasilla), 2)  # Dibuja el borde negro
        
def main():
    pygame.init()  # Inicializa pygame
    pantalla = pygame.display.set_mode((ancho, alto))  # Crea la ventana
    pygame.display.set_caption("Puzzle 8")  # Título de la ventana
    fuente = pygame.font.Font(None, tamFuente)  # Fuente para los números

    tablero = CrearTablero()  # Genera un tablero aleatorio resoluble

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False  # Sale del bucle si se cierra la ventana

        dibujar_tablero(pantalla, tablero, fuente)  # Dibuja el tablero
        pygame.display.flip()  # Actualiza la pantalla

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()