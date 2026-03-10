import pygame
import math
from agente import Triangulo

# Tamaño ventana
ANCHO = 800
ALTO = 600

# Velocidades
VEL_MOV = 5
VEL_ROT = 4


def mover(tri, teclas):
    rad = math.radians(tri.angulo)

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        tri.x += VEL_MOV * math.cos(rad)
        tri.y -= VEL_MOV * math.sin(rad)

    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        tri.x -= VEL_MOV * math.cos(rad)
        tri.y += VEL_MOV * math.sin(rad)


def rotar(tri, teclas):
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        tri.angulo += VEL_ROT

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        tri.angulo -= VEL_ROT

    tri.angulo %= 360


def rebotar(tri):
    margen = tri.tamano * 1.1

    if tri.x < margen:
        tri.x = margen
        tri.angulo = 180 - tri.angulo

    if tri.x > ANCHO - margen:
        tri.x = ANCHO - margen
        tri.angulo = 180 - tri.angulo

    if tri.y < margen:
        tri.y = margen
        tri.angulo = -tri.angulo

    if tri.y > ALTO - margen:
        tri.y = ALTO - margen
        tri.angulo = -tri.angulo

    tri.angulo %= 360


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Movimiento de Triángulo")
    reloj = pygame.time.Clock()

    jugador = Triangulo(400, 300, 60)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        teclas = pygame.key.get_pressed()

        rotar(jugador, teclas)
        mover(jugador, teclas)
        rebotar(jugador)

        pantalla.fill((0, 0, 0))
        jugador.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()