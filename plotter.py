import pygame
from math import sin, tan

HEIGHT = 800
WIDTH = 800
DENSITY = 100
pygame.init()
pygame.display.set_caption("Graph plotter")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def graph(fx, color, surface, fy=lambda y: y):
    for x in range(WIDTH):
        surface.set_at((fy(x), HEIGHT - round(fx(x / DENSITY - WIDTH / (2 * DENSITY)) * DENSITY + HEIGHT / 2)),
                      pygame.Color(color))


running = True
a = 0.1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, pygame.Color("white"), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    pygame.draw.line(screen, pygame.Color("white"), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))
    graph(lambda x: a**x, "red", screen)
    pygame.display.flip()
    clock.tick(60)
    a += 0.01
