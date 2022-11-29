import pygame
from sys import exit

size = width, height = (800, 400)
fps = 60

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             

    pygame.display.update()
    clock.tick(fps)
