import pygame
import math


class Triangulo:
    def __init__(self, x, y, tam, angulo=30):
        self.x = x
        self.y = y
        self.tamano = tam
        self.angulo = angulo

    def dibujar(self, pantalla):
        # Triángulo base (sin rotar)
        puntos = [
            (0, -self.tamano),
            (-self.tamano / 2, self.tamano / 2),
            (self.tamano / 2, self.tamano / 2)
        ]

        puntos_rotados = []
        rad = math.radians(self.angulo)

        for px, py in puntos:
            rx = px * math.cos(rad) - py * math.sin(rad)
            ry = px * math.sin(rad) + py * math.cos(rad)

            puntos_rotados.append((self.x + rx, self.y + ry))

        # Dibujar figura
        pygame.draw.polygon(pantalla, (0, 180, 0), puntos_rotados)
        pygame.draw.polygon(pantalla, (255, 255, 255), puntos_rotados, 2)

        # Punto rojo al frente
        fx, fy = puntos_rotados[0]
        pygame.draw.circle(pantalla, (255, 0, 0), (int(fx), int(fy)), 8)