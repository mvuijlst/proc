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

    for x in range(1, 5):
        x = int(random.uniform(0, WIDTH))
        y = int(random.uniform(0, HEIGHT))
        xd = int(random.uniform(-5, 5))
        yd = int(random.uniform(-20, 20))
        w = int(random.uniform(1, 4))
        c = int(random.uniform(100, 200))
        pygame.draw.line(SCREEN, (c, c, c), (x, y), (x+xd, y+yd), w)

    pygame.display.flip()
    CLOCK.tick(60)
    pygame.display.set_caption("fps: " + str(int(CLOCK.get_fps())))

