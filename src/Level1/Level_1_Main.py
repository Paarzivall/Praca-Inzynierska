import pygame
import os
from src.Level1.DrawBackground import DrawBackground
from src.ResizeClass import resize
from src.Level1.Numbers import Numbers
from src.Level1.Pins import Pins


class Level_1_Main(DrawBackground):
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.background = resize(pygame.image.load("../../img/Level1/otwieranie_zamka.png"))
        super().__init__(self.background)
        self.board = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.numbers = Numbers()
        self.pins = Pins()
        print(self.numbers.binary)

    def draw(self):
        self.draw_window()
        self.numbers.draw_numbers()
        self.pins.draw_pins()

    def run(self):
        while not self.handle_events():
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True


lvl1 = Level_1_Main()
lvl1.run()
