import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 40))
        self.image.fill((64,64,64))
        self.rect = self.image.get_rect(midbottom = (380, 720))


class Wall(pygame.sprite.Sprite):
    def __init__(self, left, mid, h):
        super().__init__() 
        self.left = left
        self.mid = mid

        if self.left:
            self.start = 0
            self.end = self.mid - 40

        else:
            self.start = self.mid + 40
            self.end = 760

        
        self.image = pygame.Surface((self.end - self.start, 40))
        self.image.fill((241,229,89))
        self.rect = self.image.get_rect(topleft = (self.start, h))




class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.d = choice([-1, 1])
        
        if self.d == 1:
            h = choice([400, 440, 480, 520, 560])
            start = -30

        else:
            h = choice([380, 420, 460, 500, 540, 580])
            start = 720

        self.image = pygame.Surface((30, 5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(midbottom = (start, h))

    def update(self):
        self.rect.x += 5*self.d



class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 40))
        self.image.fill((255,99,99))

        h = choice([80, 120, 160, 200, 240, 280, 320])
        self.rect = self.image.get_rect(midbottom = (0, h))

        self.v = choice([8,10,12])

    def update(self):
        self.rect.x += self.v


pygame.init()
screen = pygame.display.set_mode((760, 720))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

sharks = pygame.sprite.Group()
boats = pygame.sprite.Group()
walls = pygame.sprite.Group()


walls.add(Wall(True, 480, 0))
walls.add(Wall(False, 480, 0))

walls.add(Wall(True, 200, 320))
walls.add(Wall(False, 200, 320))

walls.add(Wall(True, 560, 600))
walls.add(Wall(False, 560, 600))



shark_timer = pygame.USEREVENT + 1
pygame.time.set_timer(shark_timer, 400) 

boat_timer = pygame.USEREVENT + 2
pygame.time.set_timer(boat_timer, 600) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                player.sprite.rect.y -= 40

            if event.key == pygame.K_DOWN and player.sprite.rect.bottom < 700:
                player.sprite.rect.y += 40

            if event.key == pygame.K_LEFT  and player.sprite.rect.x > 0:
                player.sprite.rect.x -= 40

            if event.key == pygame.K_RIGHT and player.sprite.rect.right < 760:
                player.sprite.rect.x += 40 

        
        if event.type == shark_timer:
            sharks.add(Shark())

        if event.type == boat_timer:
            boats.add(Boat())


    screen.fill((52,166,251))
    player.draw(screen)
    
    sharks.draw(screen)
    sharks.update()
    
    boats.draw(screen)
    boats.update()

    walls.draw(screen)

    collide_walls = pygame.sprite.spritecollide(player.sprite, walls, False)
    collide_sharks = pygame.sprite.spritecollide(player.sprite, sharks, False)
    collide_boats = pygame.sprite.spritecollide(player.sprite, boats, False)

    

    if collide_walls or collide_sharks or collide_boats:
        player.sprite.rect.midbottom = (380, 720)


    pygame.display.update()
    clock.tick(60)