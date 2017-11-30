import sys, pygame, random
pygame.init()

size = width, height = 800, 600

black = 0, 0, 0
white = 255,255,255
x=y=0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    
    x=int(random.uniform(0,width))
    y=int(random.uniform(0,height))
    
    for x in range(300,400):
        print(x)
        screen.set_at((x,x),black)
    
    pygame.display.flip()
