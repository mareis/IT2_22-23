import pygame
from sys import exit
from random import randint, choice


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((48, 18))
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom = (x, y))

class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 300
        self.y = 650
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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, 560)
        self.y = 300
        self.v = randint(-10,10)
        self.direction = 1

        
        self.image = pygame.Surface((20, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def update(self):
        self.rect.y += 5*self.direction
        self.rect.x += self.v

        if self.rect.x <= 0 or self.rect.right >= 600:
            self.v *= -1

        if self.rect.y < 0:
            self.direction *= -1

pygame.init()
screen = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()

bricks = pygame.sprite.Group()

colors = ['pink', 'purple', 'red', 'blue', 'green', 'orange']
for x in range(12):
    for y in range(len(colors)):
        bricks.add(Brick(25+x*50, 20+y*20, colors[y]))


player = pygame.sprite.GroupSingle()
player.add(Pad())

balls = pygame.sprite.Group()
balls.add(Ball())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    screen.fill((0,0,0))

    bricks.draw(screen)

    player.draw(screen)
    player.update()

    balls.draw(screen)
    balls.update()

    collided_balls = pygame.sprite.spritecollide(player.sprite, balls, False)
    for ball in collided_balls:
        ball.direction *= -1
    
    for ball in balls:
        brick_hit_list = pygame.sprite.spritecollide(ball, bricks, True)
        if brick_hit_list:
            ball.direction *= -1

    pygame.display.update()
    clock.tick(60)