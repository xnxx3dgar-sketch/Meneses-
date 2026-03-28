import pygame
import sys


# ====== CONFIGURACIÓN ======
def iniciar():
    pygame.init()


def crear_pantalla():
    ancho = 800
    alto = 600
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Ejercicio 1 - Puntos")
    return ventana


# ====== COLORES ======
def obtener_colores():
    colores = {
        "blanco": (255, 255, 255),
        "rojo": (255, 0, 0),
        "verde": (0, 255, 0),
        "azul": (0, 0, 255),
        "amarillo": (255, 255, 0),
        "negro": (0, 0, 0)
    }
    return colores


# ====== DIBUJO ======
def dibujar_puntos(pantalla, colores):
    pantalla.fill(colores["negro"])

    # lista de puntos (posición, color, tamaño)
    puntos = [
        ((200, 300), colores["blanco"], 5),
        ((600, 300), colores["rojo"], 8),
        ((450, 150), colores["verde"], 6),
        ((400, 300), colores["azul"], 3),
        ((700, 500), colores["amarillo"], 10)
    ]

    for punto in puntos:
        posicion, color, radio = punto
        pygame.draw.circle(pantalla, color, posicion, radio)


# ====== LOOP PRINCIPAL ======
def ejecutar():
    iniciar()
    pantalla = crear_pantalla()
    colores = obtener_colores()

    activo = True

    while activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False

        dibujar_puntos(pantalla, colores)

        pygame.display.update()

    pygame.quit()
    sys.exit()


# ====== EJECUCIÓN ======
if __name__ == "__main__":
    ejecutar()