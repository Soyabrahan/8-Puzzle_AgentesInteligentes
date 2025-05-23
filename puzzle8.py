#MiniProyecto de trabar con dos inteligencias artificales que resuelvan el puzle 8
#usare la libreria pygame para la interfaz grafica

#--->LIBRERIAS<---
import pygame #Interfaz Grafica
import random #Aleatoriedad
import sys  #sistema
import time
import IDDFS
import AgenteInformado
#--->Importaciones<---
from IDDFS import iddfs  # Importa la función IDDFS del archivo iddfs.py
from AgenteInformado import a_estrella  # Agente informado (debes tener este archivo)


#--->CONFIGURACION GENERAL<---
tamCasilla = 120  # Más grande para mejor visualización
tamTablero = 3
ancho = tamCasilla * tamTablero
alto = tamCasilla * tamTablero + 120  # Espacio extra para menú/info
FPS = 30
tamFuente = 28  # Más pequeño para que quepa mejor

#--->COLORES<---
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (197, 29, 52)
azul = (0, 102, 204)
verde = (0, 200, 70)
gris = (220, 220, 220)

#-->Aleatoriedad del tablero<--
def CrearTablero():
    while True:
        tablero = list(range(9)) #Crea una lista de 0 a 8
        random.shuffle(tablero) #Mezcla la lista
        if esResoluble(tablero, objetivo): #Si el tablero es resoluble
            return tablero #Devuelve el tablero
        
#-->Comprobar si el tablero es resoluble<--
objetivo = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def esResoluble(tablero, objetivo):
    # Quita el 0 (espacio vacío) de ambos
    t = [x for x in tablero if x != 0]
    o = [x for x in objetivo if x != 0]
    # Calcula la permutación necesaria para convertir t en o
    inv = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            # Compara la posición de los valores en el objetivo
            if o.index(t[i]) > o.index(t[j]):
                inv += 1
    return inv % 2 == 0

#-->Dibujar el tablero<--
def dibujar_tablero(pantalla, tablero, fuente):
    pantalla.fill(gris) # Rellena la pantalla de color gris
    for i in range(9):  # Recorre cada casilla del tablero
        x = (i % tamTablero) * tamCasilla  # Calcula la posición x de la casilla
        y = (i // tamTablero) * tamCasilla + 60  # Deja espacio arriba para info
        valor = tablero[i]  # Obtiene el valor de la casilla
        if valor != 0:  # Si la casilla no es el espacio vacío
            pygame.draw.rect(pantalla, rojo, (x+5, y+5, tamCasilla-10, tamCasilla-10), border_radius=10)  # Dibuja el rectángulo azul
            texto = fuente.render(str(valor), True, blanco)  # Renderiza el número en blanco
            rect = texto.get_rect(center=(x + tamCasilla // 2, y + tamCasilla // 2))  # Centra el texto
            pantalla.blit(texto, rect)  # Dibuja el texto en la pantalla
        pygame.draw.rect(pantalla, negro, (x, y, tamCasilla, tamCasilla), 2, border_radius=10)  # Dibuja el borde negro

def mostrar_menu(pantalla, fuente):
    pantalla.fill(gris)
    titulo = fuente.render("Puzzle 8 - Selecciona el agente", True, azul)
    pantalla.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 30))

    btn_iddfs = pygame.Rect(ancho // 2 - 160, 120, 320, 60)
    btn_astar = pygame.Rect(ancho // 2 - 160, 210, 320, 60)
    pygame.draw.rect(pantalla, azul, btn_iddfs, border_radius=15)
    pygame.draw.rect(pantalla, verde, btn_astar, border_radius=15)

    txt_iddfs = fuente.render("Agente No Informado (IDDFS)", True, blanco)
    txt_astar = fuente.render("Agente Informado (A*)", True, blanco)
    pantalla.blit(txt_iddfs, (btn_iddfs.x + 20, btn_iddfs.y + 15))
    pantalla.blit(txt_astar, (btn_astar.x + 20, btn_astar.y + 15))

    pygame.display.flip()
    return btn_iddfs, btn_astar

def mostrar_info(pantalla, fuente, tiempo, movimientos):
    info = f"Tiempo: {tiempo:.2f}s  Movimientos: {movimientos}"
    texto = fuente.render(info, True, azul)
    pantalla.blit(texto, (10, 10))

def mostrar_info_final(pantalla, fuente, tiempo, movimientos, nodos):
    pantalla.fill(gris)
    texto1 = fuente.render(f"Tiempo: {tiempo:.2f}s", True, azul)
    texto2 = fuente.render(f"Movimientos: {movimientos}", True, azul)
    texto3 = fuente.render(f"Nodos expandidos: {nodos}", True, azul)
    pantalla.blit(texto1, (ancho // 2 - texto1.get_width() // 2, alto // 2 - 90))
    pantalla.blit(texto2, (ancho // 2 - texto2.get_width() // 2, alto // 2 - 40))
    pantalla.blit(texto3, (ancho // 2 - texto3.get_width() // 2, alto // 2 + 10))
    btn_menu = pygame.Rect(ancho // 2 - 100, alto // 2 + 60, 200, 50)
    pygame.draw.rect(pantalla, verde, btn_menu, border_radius=10)
    txt_menu = fuente.render("Volver al menú", True, blanco)
    pantalla.blit(txt_menu, (btn_menu.x + 10, btn_menu.y + 10))
    pygame.display.flip()
    return btn_menu



def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Puzzle 8/Abrahan Ramirez")
    fuente = pygame.font.Font(None, tamFuente)
    reloj = pygame.time.Clock()

    while True:
        # Menú de selección
        seleccion = None
        while seleccion is None:
            btn_iddfs, btn_astar = mostrar_menu(pantalla, fuente)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if btn_iddfs.collidepoint(evento.pos):
                        seleccion = "iddfs"
                    elif btn_astar.collidepoint(evento.pos):
                        seleccion = "astar"
            reloj.tick(FPS)

        tablero = CrearTablero()
        dibujar_tablero(pantalla, tablero, fuente)
        pygame.display.flip()
        time.sleep(0.5)

        t0 = time.time()
        if seleccion == "iddfs":
            solucion = IDDFS.iddfs(tablero, max_profundidad=30)
            agente = "No informado (IDDFS)"
            nodos = IDDFS.nodos_expandidos
        else:
            solucion = AgenteInformado.a_estrella(tablero)
            agente = "Informado (A*)"
            nodos = AgenteInformado.nodos_expandidos
        t1 = time.time()
        tiempo = t1 - t0
        movimientos = len(solucion) - 1 if solucion else 0

        # Animación de la solución encontrada
        if solucion:
            for paso in solucion:
                dibujar_tablero(pantalla, paso, fuente)
                mostrar_info(pantalla, fuente, tiempo, movimientos)
                pygame.display.flip()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.time.wait(300)

            # --- Pausa hasta que el usuario haga click ---
            esperando_click = True
            while esperando_click:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        esperando_click = False
                reloj.tick(FPS)
        else:
            # Mostrar mensaje en pantalla
            pantalla.fill(gris)
            texto = fuente.render("¡No se encontró solución!", True, rojo)
            pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, alto // 2))
            pygame.display.flip()
            print("¡No se encontró solución!")  # Mensaje en terminal

            # Espera a que el usuario haga click o cierre la ventana
            esperando_click = True
            while esperando_click:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        esperando_click = False
                reloj.tick(FPS)

        print(f"Agente: {agente}")
        print(f"Tiempo de búsqueda: {tiempo:.2f} segundos")
        print(f"Movimientos: {movimientos}")
        print(f"Nodos expandidos: {nodos}")

        # Pantalla final con botón para volver al menú
        esperando = True
        while esperando:
            btn_menu = mostrar_info_final(pantalla, fuente, tiempo, movimientos, nodos)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if btn_menu.collidepoint(evento.pos):
                        esperando = False
            reloj.tick(FPS)

if __name__ == "__main__":
    main()