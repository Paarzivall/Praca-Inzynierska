import os
import pygame
from src.Level1.Level_1_Main import Level_1_Main
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()


class GameController(object):
    def __init__(self):
        self.current_level = 0
        self.player_lives = 3
        self.avaliable_levels = [Level_1_Main(), BaseLevelPlatform()]
        self.level_with_lives = {1: 'no', 2: 'yes'}

    def controller(self):
        for level in self.avaliable_levels:
            while level.is_done is False:
                level.run()


if __name__ == '__main__':
    start_game = GameController()
    start_game.controller()