import os
import pygame
from src.Level1.Level_1_Main import Level_1_Main
from src.ExampleLevels.ExampleLvl import ExampleLvl
from src.PlatformsMainPackage.Player import Player
from src.BreakingClass import BreakingClass
import src.MainImages as main_img
import sys
from src.BubbleSortLevel.BubbleSortLevelMain import BubbleSortLevelMain

from src.PlayFair.PlayFairMain import PlayFairMain

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
                    first_break = BreakingClass(main_img.break_1)
                    first_break.run()
            if self.current_level == 2 and first_break.is_done is True:
                player = Player(3, main_img.stand_right)
                lvl_platform = ExampleLvl(player)
                player.rect.center = lvl_platform.get_surface().get_rect().center
                player.level = lvl_platform
                lvl_platform.update()
                lvl_platform.run()
                if lvl_platform.is_done:
                    self.current_level = 3
                    second_break = BreakingClass(main_img.break_2)
                    second_break.run()
            if self.current_level == 3 and second_break.is_done:
                bubble = BubbleSortLevelMain()
                if bubble.run():
                    self.current_level = 4
                    third_break = BreakingClass(main_img.break_2)
                    third_break.run()
            if self.current_level == 4 and third_break.is_done:
                playfair = PlayFairMain()
                if playfair.run():
                    self.current_level = 5
                    fourth_break = BreakingClass(main_img.break_2)
                    fourth_break.run()
            if self.current_level == 5 and fourth_break.is_done:
                sys.exit()"""
        playfair = PlayFairMain()
        playfair.run()



if __name__ == '__main__':
    start_game = GameController()
    start_game.controller()
