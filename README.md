# Puzzle 8 - Agentes Inteligentes

Este proyecto resuelve el clásico **Puzzle 8** utilizando dos tipos de agentes inteligentes:
- **Agente No Informado:** Búsqueda por Profundización Iterativa (IDDFS)
- **Agente Informado:** Búsqueda A* con heurística de Manhattan

Incluye una interfaz gráfica desarrollada con **Pygame** para interactuar y visualizar el proceso de resolución.

---

## Requisitos

- Python 3.8 o superior
- [Pygame](https://www.pygame.org/)  
  Instala con:
  ```
  pip install pygame
  ```

---

## Estructura del proyecto

- `puzzle8.py` — Interfaz gráfica y lógica principal del juego.
- `IDDFS.py` — Implementación del agente no informado (IDDFS).
- `AgenteInformado.py` — Implementación del agente informado (A*).

---

## Cómo ejecutar

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias.
3. Ejecuta el archivo principal:
   ```
   python puzzle8.py
   ```

---

## Cómo jugar

- Al iniciar, elige el agente con el que deseas resolver el puzzle.
- El tablero se genera aleatoriamente (solo si es resoluble).
- Observa cómo el agente resuelve el puzzle paso a paso.
- Al finalizar, puedes volver al menú y probar con otro agente o tablero.

---

## Notas

- El objetivo del puzzle es:  
  `[1, 2, 3, 8, 0, 4, 7, 6, 5]`
- El programa detecta automáticamente si un tablero es irresoluble y lo indica en pantalla.
- Puedes modificar el objetivo o el tablero inicial en el código si lo deseas.

---

## Autor

Abrahan Ramírez

---

¡Disfruta resolviendo el Puzzle 8 con inteligencia artificial!
