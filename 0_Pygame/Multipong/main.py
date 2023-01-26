import pygame
from sys import exit
from random import randint, choice

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, 560)
        self.y = 50
        self.v = randint(-10,10)
        self.direction = 1

        
        self.image = pygame.Surface((20, 20))
        color = choice([ (255,0,0), (0,255,0), (0,0,255) ])
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def update(self):
        self.rect.y += 5*self.direction
        self.rect.x += self.v

        if self.rect.x <= 0 or self.rect.right >= 600:
            self.v *= -1

        if self.rect.y < 0:
            self.direction *= -1

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 300
        self.y = 750
        self.width = 100  

        self.image = pygame.Surface((self.width, 10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 10

        if keys[pygame.K_RIGHT] and self.rect.right <= 600:
            self.rect.x += 10

    def update(self):
        self.player_input()

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()

balls = pygame.sprite.Group()
balls.add(Ball())

ball_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ball_timer, 1500) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == ball_timer:
            balls.add(Ball())

    screen.fill((0,0,0))
    balls.draw(screen)
    balls.update()

    player.draw(screen)
    player.update()
    
    collided_balls = pygame.sprite.spritecollide(player.sprite, balls, False)
    for ball in collided_balls:
        ball.direction *= -1
        

    pygame.display.update()
    clock.tick(60)