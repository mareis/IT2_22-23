import pygame as pg
import sys
from random import randint, choice

WINDOW_WIDTH = 600
WINDOW_HIGHT = 800

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HIGHT])
        self.clock = pg.time.Clock()

        #Til dette spillet
        self.pad = pg.sprite.GroupSingle()
        self.pad.add(Pad())

        self.balls = pg.sprite.Group()
        self.balls.add(Ball())

        self.ball_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.ball_timer, 1500) 
    
    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        pg.display.update()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill('black')

        #Til dette spillet
        self.balls.draw(self.screen)
        self.balls.update()

        self.pad.draw(self.screen)
        self.pad.update()
    
    
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            #Til dette spillet
            if event.type == self.ball_timer:
                self.balls.add(Ball())
        
        #Til dette spillet
        collided_balls = pg.sprite.spritecollide(self.pad.sprite, self.balls, False)
        for ball in collided_balls:
            ball.direction *= -1

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


class Pad(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 300
        self.y = 750
        self.width = 100  

        self.image = pg.Surface((self.width, 10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))


    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 10

        if keys[pg.K_RIGHT] and self.rect.right <= WINDOW_WIDTH:
            self.rect.x += 10

    def update(self):
        self.player_input()


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, WINDOW_WIDTH-30)
        self.y = 50
        self.v = randint(-10,10)
        self.direction = 1
        self.image = pg.Surface((20, 20))
        color = choice([ (255,0,0), (0,255,0), (0,0,255) ])
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def update(self):
        self.rect.y += 5*self.direction
        self.rect.x += self.v

        if self.rect.x <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.v *= -1

        if self.rect.y < 0:
            self.direction *= -1

if __name__ == '__main__':
    game = Game()
    game.run()