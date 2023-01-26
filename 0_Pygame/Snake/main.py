import pygame
from sys import exit
from random import randint, choice

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill("Red")
        self.rect = self.image.get_rect(topleft = (x, y))


class Snake(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((20, 20))
            self.image.fill((0,255,0))
            self.rect = self.image.get_rect(topleft = (300, 300))
            self.directions = (1, 0)

        def player_input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.directions[1] != 0:
                self.directions = (-1, 0)

            if keys[pygame.K_RIGHT] and self.directions[1] != 0:
                self.directions = (1, 0)

            if keys[pygame.K_RIGHT] and self.directions[1] != 0:
                self.directions = (1, 0)

        def move(self):
            self.rect.x += 20*self.directions[0]
            self.rect.y += 20*self.directions[1]


        def update(self):
            self.player_input()
            self.move()


pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

snake = pygame.sprite.GroupSingle()
snake.add(Snake())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    screen.fill((0,0,0))
    snake.draw(screen)
    snake.update()

    pygame.display.update()
    clock.tick(5)