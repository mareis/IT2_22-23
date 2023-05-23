import pygame as pg
import sys
from random import randint, choice

WINDOW_WIDTH = 800
WINDOW_HIGHT = 600

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HIGHT])
        self.clock = pg.time.Clock()

        self.aircrafts = pg.sprite.Group()
        self.aircrafts.add(Boeng())
        self.aircrafts.add(AirBuss())

        #self.ball_timer = pg.USEREVENT + 1
        #pg.time.set_timer(self.ball_timer, 1500) 
    
    def new_game(self):
        pass
    

    def update(self):
        pg.display.update()
        self.clock.tick(60)
        self.aircrafts.update()

    def draw(self):
        self.screen.fill('blue')
        self.aircrafts.draw(self.screen)

      
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
   
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

class Aircraft(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = randint(30, 400)
        
    def drawImage(self):
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def movement(self):
        self.rect.x += self.speed 

    def update(self):
        self.movement()

class Boeng(Aircraft):
    def __init__(self):
        super().__init__()
        self.width = 35
        self.height = 12
        self.color = 'white'
        self.speed = 6
        self.drawImage()
       
class AirBuss(Aircraft):
    def __init__(self):
        super().__init__()
        self.width = 45
        self.height = 29
        self.color = 'yellow'
        self.speed = 4
        self.drawImage()

if __name__ == '__main__':
    game = Game()
    game.run()