import pygame
from math import radians
from agente import EntidadMovil

# ─────────────────────────────
# CONFIGURACIÓN GENERAL
# ─────────────────────────────
DIMENSIONES = (800, 600)
FPS = 60

VELOCIDAD_LINEAL = 5
VELOCIDAD_ANGULAR = 3


def iniciar():
    pygame.init()
    ventana = pygame.display.set_mode(DIMENSIONES)
    pygame.display.set_caption("Simulación de Entidad con Colisión")
    temporizador = pygame.time.Clock()
    return ventana, temporizador


def procesar_movimiento(objeto, teclas):
    vector_mov = pygame.Vector2(0, 0)

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        ang = radians(objeto.direccion)
        vector_mov.x += VELOCIDAD_LINEAL * pygame.math.Vector2(1, 0).rotate(-objeto.direccion).x
        vector_mov.y += VELOCIDAD_LINEAL * pygame.math.Vector2(1, 0).rotate(-objeto.direccion).y

    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        ang = radians(objeto.direccion)
        vector_mov.x -= VELOCIDAD_LINEAL * pygame.math.Vector2(1, 0).rotate(-objeto.direccion).x
        vector_mov.y -= VELOCIDAD_LINEAL * pygame.math.Vector2(1, 0).rotate(-objeto.direccion).y

    objeto.posicion += vector_mov


def procesar_rotacion(objeto, teclas):
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        objeto.direccion += VELOCIDAD_ANGULAR

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        objeto.direccion -= VELOCIDAD_ANGULAR

    objeto.direccion %= 360


def verificar_limites(objeto, ancho, alto):
    limite = objeto.radio * 1.1

    if objeto.posicion.x < limite:
        objeto.posicion.x = limite
        objeto.direccion = 180 - objeto.direccion

    if objeto.posicion.x > ancho - limite:
        objeto.posicion.x = ancho - limite
        objeto.direccion = 180 - objeto.direccion

    if objeto.posicion.y < limite:
        objeto.posicion.y = limite
        objeto.direccion = -objeto.direccion

    if objeto.posicion.y > alto - limite:
        objeto.posicion.y = alto - limite
        objeto.direccion = -objeto.direccion

    objeto.direccion %= 360


def main():
    pantalla, reloj = iniciar()
    ancho, alto = DIMENSIONES

    jugador = EntidadMovil(ancho // 2, alto // 2, 60)

    activo = True
    while activo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False

        teclas = pygame.key.get_pressed()

        procesar_rotacion(jugador, teclas)
        procesar_movimiento(jugador, teclas)
        verificar_limites(jugador, ancho, alto)

        pantalla.fill((0, 0, 0))
        jugador.renderizar(pantalla)

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
