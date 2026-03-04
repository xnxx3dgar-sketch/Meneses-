import pygame
from math import sin, cos, radians

class EntidadMovil:
    def __init__(self, pos_x, pos_y, escala, direccion_inicial=30):
        self.posicion = pygame.Vector2(pos_x, pos_y)
        self.radio = escala
        self.direccion = direccion_inicial

    def _calcular_puntos(self):
        """
        Genera los puntos rotados del triángulo en base
        a la orientación actual.
        """

        base_shape = [
            pygame.Vector2(0, -self.radio),
            pygame.Vector2(-self.radio / 2, self.radio / 2),
            pygame.Vector2(self.radio / 2, self.radio / 2)
        ]

        angulo_rad = radians(self.direccion)

        puntos_transformados = []
        for punto in base_shape:
            rotado = pygame.Vector2(
                punto.x * cos(angulo_rad) - punto.y * sin(angulo_rad),
                punto.x * sin(angulo_rad) + punto.y * cos(angulo_rad)
            )
            puntos_transformados.append(self.posicion + rotado)

        return puntos_transformados

    def renderizar(self, superficie, color_principal=(0,150,0), color_punta=(255,0,0)):
        vertices = self._calcular_puntos()

        pygame.draw.polygon(superficie, color_principal, vertices)
        pygame.draw.polygon(superficie, (255,255,255), vertices, 2)

        punta = vertices[0]
        pygame.draw.circle(superficie, color_punta, (int(punta.x), int(punta.y)), 8)
