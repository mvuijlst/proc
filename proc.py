"""
Ik dacht, ik probeer eens iets te maken dat dingen op het scherm toont.
"""

import sys
import random
import pygame


pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255

SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()
RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(WHITE)

    for x in range(1, 10000):
        SCREEN.set_at((int(random.uniform(0, WIDTH)), int(random.uniform(0, HEIGHT))), BLACK)

    pygame.display.flip()
