import pygame
from sys import exit
from random import randint, choice

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.v = 0
        self.image = pygame.Surface((80, 50))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(midbottom = (160, 300))

    def update(self):
        self.v += 0.3
        self.rect.y += self.v


class Pipe(pygame.sprite.Sprite):
    def __init__(self, upper, mid):
        super().__init__() 
        self.upper = upper
        self.mid = mid

        if self.upper:
            self.start = 0
            self.end = self.mid - 100

        else:
            self.start = self.mid + 100
            self.end = 600

        
        self.image = pygame.Surface((80, self.end - self.start))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(midbottom = (900, self.end))

    def update(self):
        self.rect.x -= 4


pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

bird = pygame.sprite.GroupSingle()
bird.add(Bird())

pipes = pygame.sprite.Group()
pipes.add(Pipe(True, 300))
pipes.add(Pipe(False,300))

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 1000) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                bird.sprite.v = -5
        
        if event.type == pipe_timer:
            mid = randint(100,500)
            pipes.add(Pipe(True, mid))
            pipes.add(Pipe(False, mid))

    screen.fill((0,0,0))
    bird.draw(screen)
    bird.update()

    pipes.draw(screen)
    pipes.update()

    collide_pipes = pygame.sprite.spritecollide(bird.sprite, pipes, True)
    if collide_pipes:
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)