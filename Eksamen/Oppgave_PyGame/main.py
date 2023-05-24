import pygame as pg
import sys
from random import randint, choice

WINDOW_WIDTH = 800
WINDOW_HIGHT = 600
FPS = 60


class Game:
    """
    En spillklasse.
    ...

    Attributes
    ----------
    screen
        metode fra pygame som setter størelsen på vinduet
    clock
        metode fra pygame som håndterer tid
    aircrafts
        innebygd metode fra pygame som samler alle flyene som "sprites" 

    aircraft_timer
        innebygd håndtering av hendelser i spillet. I dette tilfellet så er settes 
        intervallet til 1 sekund

    Methods
    -------
    update():
        håndterer alt som skal oppdateres i spillet

    draw():
        håndterer alt som skal tegnes til skjerm

    check_event():
        håndterer alle hendelsene i spillet


    run():
        inneholder spilløkken

    """

    def __init__(self):
        self.screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HIGHT])
        self.clock = pg.time.Clock()
        self.aircrafts = pg.sprite.Group()

        # self.aircrafts.add(Boeng())
        # self.aircrafts.add(AirBuss())
        self.aircraft_timer = pg.USEREVENT + 1
        pg.time.set_timer(self.aircraft_timer, 1000)

    def new_game(self):
        pass

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        self.aircrafts.update()

    def draw(self):
        self.screen.fill('blue')
        self.aircrafts.draw(self.screen)

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == self.aircraft_timer:
                ac = [Boeng(), AirBuss()]
                self.aircrafts.add(ac[randint(0, 1)])

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


class Aircraft(pg.sprite.Sprite):
    """
    En overordna flyklasse.
    ...

    Attributes
    ----------
    x : int
        x-koordinat til flyet
    y : int
        y-koordinat til flyet. Tilfeldig mellom 30 og 400

    Methods
    -------
    drawImage():
        tegner flyet som en rektangel

    movement():
        bestemmer bevegelsen til flyet

    update():
        oppdaterer det som treng

    """

    def __init__(self):
        super().__init__()
        self.x = -100
        self.y = randint(30, 400)

    def drawImage(self):
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def movement(self):
        self.rect.x += self.speed

    def update(self):
        self.movement()


class Boeng(Aircraft):
    """
    Spesifikt fly som arver fra Aircraft-klassen
    ...

    Attributes
    ----------
    width : int
        bredden/lengden til flyet
    height : int
        høyden til flyet. Tilfeldig mellom 30 og 400
    color : str
        fargen til flyet
    speed : int
        farten til flyet


    """

    def __init__(self):
        super().__init__()
        self.width = 35
        self.height = 12
        self.color = 'white'
        self.speed = 6
        self.drawImage()


class AirBuss(Aircraft):
    """
    Spesifikt fly som arver fra Aircraft-klassen
    ...

    Attributes
    ----------
    width : int
        bredden/lengden til flyet
    height : int
        høyden til flyet. Tilfeldig mellom 30 og 400
    color : str
        fargen til flyet
    speed : int
        farten til flyet

    Methods
    -------
    drawImage():
        tegner flyet som en rektangel

    movement():
        bestemmer bevegelsen til flyet

    update():
        oppdaterer det som treng

    """

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
