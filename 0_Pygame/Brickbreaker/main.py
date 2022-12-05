import pygame
from sys import exit
from random import randint, choice


pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)