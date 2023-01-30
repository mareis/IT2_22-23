import pygame
from sys import exit
from random import randint, choice

class Astroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(10, 760)
        self.y = 50
        radius = choice([(30, 30),(30, 30),(30, 30), (50, 50), (40, 40), (70,70), (100,100)])
        self.v = 13 - radius[0]/10
        
        self.image = pygame.Surface(radius)

        color = choice([ (100,20,20), (20,100,20), (20,20,100) ])
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def update(self):
        self.rect.y += self.v

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('white')
        self.rect = self.image.get_rect(midbottom = player.sprite.rect.midtop)


    def update(self):
        self.rect.y -= 10

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 300
        self.y = 750

        self.image = pygame.Surface((30, 100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 10

        if keys[pygame.K_RIGHT] and self.rect.right <= 800:
            self.rect.x += 10
        
    
    def update(self):
        self.player_input()

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(SpaceShip())

astroids = pygame.sprite.Group()
astroids.add(Astroid())

bullets = pygame.sprite.Group()

astroid_timer = pygame.USEREVENT + 1
pygame.time.set_timer(astroid_timer, 500) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == astroid_timer:
            astroids.add(Astroid())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.add(Bullet())

    screen.fill((0,0,0))
    astroids.draw(screen)
    astroids.update()

    player.draw(screen)
    player.update()

    bullets.draw(screen)
    bullets.update()

    #for bullet in bullets:
    #    astroid_hit_list = pygame.sprite.spritecollide(bullet, astroids, True)
    #
    #    for astroid in astroid_hit_list:
    #        bullets.remove(bullet)

    test = pygame.sprite.groupcollide(astroids, bullets, True, True)

    if test:
        print(test)

    collide_astroids = pygame.sprite.spritecollide(player.sprite, astroids, True)
    for astroid in collide_astroids:
        astroids.empty()


    pygame.display.update()

    clock.tick(60)