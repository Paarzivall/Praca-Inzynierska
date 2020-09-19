import os
import pygame
from src.Level1.Level_1_Main import Level_1_Main
from src.ExampleLevels.ExampleLvl import ExampleLvl
from src.PlatformsMainPackage.Player import Player
import src.MainImages as main_img

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()


class GameController(object):
    def __init__(self):
        self.current_level = 1
        self.player_lives = 3
        self.avaliable_levels = []
        self.level_with_lives = {1: 'no', 2: 'yes'}

    def controller(self):
        """lvl1 = Level_1_Main()
        while True:
            if self.current_level == 1 and lvl1.is_done is False:
                lvl1.run()
                if lvl1.is_done:
                    self.current_level = 2
            if self.current_level == 2:"""
        player = Player(3, main_img.stand_right)
        lvl_platform = ExampleLvl(player)
        player.rect.center = lvl_platform.get_surface().get_rect().center
        player.level = lvl_platform
        lvl_platform.update()
        lvl_platform.run()
        while True:
            print(lvl_platform.is_done)
            if lvl_platform.is_done:
                import sys
                sys.exit()


if __name__ == '__main__':
    start_game = GameController()
    start_game.controller()
