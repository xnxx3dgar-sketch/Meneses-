# Proyecto de Graficación – Triángulo en Movimiento

## Descripción

Este programa muestra un triángulo que se puede mover y rotar dentro de una ventana.

El triángulo:
- Gira sobre su centro
- Avanza y retrocede según hacia dónde apunta
- Rebota cuando toca los bordes de la pantalla

---

## Archivos

### agente.py
Contiene la clase `Triangulo`.

Se encarga de:
- Guardar posición
- Guardar tamaño
- Guardar ángulo de rotación
- Dibujar el triángulo rotado

---

### main.py
Controla todo el programa:

- Crear ventana
- Detectar teclado
- Mover figura
- Rotar figura
- Detectar colisiones con bordes
- Actualizar pantalla

---

## Controles

W / Flecha arriba → Avanzar  
S / Flecha abajo → Retroceder  
A / Flecha izquierda → Girar izquierda  
D / Flecha derecha → Girar derecha  

---

## Librerías usadas

- pygame
- math

---

## Posibles mejoras

- Agregar más figuras
- Agregar disparos
- Agregar velocidad variable
- Colisiones entre objetos