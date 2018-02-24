"""
https://foro.elhacker.net/scripting/python_espiral_de_ulam-t428328.0.html;msg1990590
"""

import sys
import pygame
import pygame.gfxdraw
import time
pygame.init()

# globales
tamano = 2  # tamano del punto, 0 = 1px, 1=3px... etc
separacion = 10  # el desplazamiento entre punto y punto, 1px
niveles = 3  # cuantas capas tendra la espiral
tiempo_maximo = 10  # si no termina de dibujar en este tiempo detiene el trabajo... switch de seguridad si tienen un pc poco potente
PRIMO = (255, 255, 255)  # color si es primo
NO_PRIMO = (64, 64, 64)  # color si no es primo
pantalla = {"w": niveles * 4 + 100, "h": niveles * 4 + 100}  # tamano de la pantalla... suficiente para puntos de 1px + 100px de margen

window = pygame.display.set_mode((pantalla["w"], pantalla["h"]))


def dibujar():
    posicion = {"x": pantalla["w"] / 2, "y": pantalla["h"] / 2}  #cursor en centro de pantalla
    direccion = 1  # 0 derecha, 1 arriba, 2 izquierda, 3 abajo
    control = 2  # variable de control
    cantidad = 1  # cantidad de puntos dibujados
    dibCir(posicion, PRIMO)  # punto central... direccion va por "referencia"

    inicio = time.clock() + tiempo_maximo  # calcular tiempo para finalizar
    for i in range(2):  # dibuja los primeros 2 puntos
        mover_dibujar(direccion, posicion, separacion, PRIMO)
        direccion += 1
        cantidad += 1
    puntos_totales = (niveles * 2 + 1) ** 2 - 1  # cantidad de puntos a dibujar

    detener = False

    for mayor in range(niveles * 2):
        for menor in range(2):
            for punto in range(control):
                if esPrimo(cantidad):  # color a dibujar
                    mover_dibujar(direccion, posicion, separacion, PRIMO)
                else:
                    mover_dibujar(direccion, posicion, separacion)

                if time.clock() > inicio:
                    detener = True  # si se pasa del tiempo
                if (cantidad == puntos_totales):
                    detener = True  # si se dibujaron los puntos necesarios
                cantidad += 1
                if(detener):
                    break
            direccion = (direccion + 1) % 4  # cambia direccion de recorrido
            if(detener):
                break
        control += 1
        if(detener):
            break
        pygame.display.flip()  # dibuja la capa calculada
    print(cantidad)  # imprime los puntos dibujados en la consola
    return 0


def mover_dibujar(direccion, posicion, separacion, color=NO_PRIMO):  # dirije el recorrido y dibuja
    if direccion == 0:
        posicion["x"] -= separacion
    if direccion == 1:
        posicion["y"] += separacion
    if direccion == 2:
        posicion["x"] += separacion
    if direccion == 3:
        posicion["y"] -= separacion
    dibCir(posicion, color)


def dibCir(posicion, color, r=tamano):
    pygame.gfxdraw.filled_circle(window, int(posicion["x"]), int(posicion["y"]), r, color)  # dibuja circulo 
    # pygame.gfxdraw.aacircle(window, posicion["x"],posicion["y"], r, color) #lo suaviza mas


def esPrimo(n):  # calcula si es primo
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


dibujar()  # ejecuta todo


# input handling (somewhat boilerplate code):


while True:  # copypaste para mentener abierta la ventana
    time.sleep(1)  # sin esto se consume todos los recursos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        # else:
        #    print event
