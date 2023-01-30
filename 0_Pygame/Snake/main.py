import pygame
from sys import exit
from random import randint, choice

width, height = size = (600, 600)

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill("Red")
        self.rect = self.image.get_rect(topleft = (x, y))
        self.count = 0


    def update(self):
        self.count += 1
        self.rect.x = randint(0,29)*20
        self.rect.y = randint(0,29)*20

class Snake(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((20, 20))
            self.image.fill((0,255,0))
            self.rect = self.image.get_rect(topleft = (300, 300))
            self.directions = (1, 0)


        def move(self):
            self.rect.x += 20*self.directions[0]
            self.rect.y += 20*self.directions[1]

            if self.rect.x > width - 10:
               self.rect.x = 0

            if self.rect.x < 0:
               self.rect.x = width

            if self.rect.y < 0:
               self.rect.y == height

            if self.rect.y > height - 10:
               self.rect.y = 0
             

        def update(self):
            self.move()

class Tail(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = (x, y))


pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

snake = pygame.sprite.GroupSingle()
snake.add(Snake())

berry = pygame.sprite.GroupSingle()
berry.add(Berry(width/2, height/2))

tail = pygame.sprite.Group()


snake_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snake_timer, 100) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.sprite.directions[1] != 0:
                snake.sprite.directions = (-1, 0)

            if event.key == pygame.K_RIGHT and snake.sprite.directions[1] != 0:
                snake.sprite.directions = (1, 0)

            if event.key == pygame.K_UP and snake.sprite.directions[0] != 0:
                snake.sprite.directions = (0, -1)

            if event.key == pygame.K_DOWN and snake.sprite.directions[0] != 0:
                snake.sprite.directions = (0, 1)

        
        if event.type == snake_timer:
            temp1 = snake.sprite.rect.center
            for t in tail:
                temp2 =  t.rect.center
                t.rect.center = temp1
                temp1 = temp2
            
            snake.update()

            collide_tail = pygame.sprite.spritecollide(snake.sprite, tail, False)
            for t in collide_tail:
                pygame.quit()
                exit()
            

    screen.fill((0,0,0))
    snake.draw(screen)
    berry.draw(screen)
    tail.draw(screen)

    eat_berry = pygame.sprite.spritecollide(snake.sprite, berry, False)
    for b in eat_berry:
        tail.add(Tail(b.rect.x, b.rect.y))
        b.update()


            
    pygame.display.update()
    clock.tick(60)