import pygame
from sys import exit
import os
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.LifeController import LifeController

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()


class BaseLevelPlatform(DrawBackground):
    def __init__(self, background, player=Player):
        super().__init__(background)
        self.board = self.get_frame()
        self.player = player
        self.set_of_platforms = set()
        self.life = LifeController.get_instance()

    def update(self):
        for simple_p in self.set_of_platforms:
            simple_p.update()

    def draw(self):
        self.draw_window()
        for simple_p in self.set_of_platforms:
            simple_p.draw(self.board)
        self.player.draw(self.board)
        self.player.update_images()
        self.life.draw_player_life(self.board)

    def run(self):
        while not self.handle_events() and self.life.is_life() is True:
            self.draw()
            pygame.display.flip()
            self.clock.tick(40)

    def handle_events(self):
        # Metoda pozwalająca zamknąć okienko

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    print("HELPER")
            self.player.get_event(event)

