import os
import pygame
from src.BinaryConvert.BinaryConvertMain import Level_1_Main
from src.ExampleLevels.ExampleLvl import ExampleLvl
from src.ExampleLevels.ExampleLvl2 import ExampleLvl2
from src.PlatformsMainPackage.Player import Player
from src.BreakingClass import BreakingClass
import src.MainImages as main_img
import sys
from src.BubbleSortLevel.BubbleSortLevelMain import BubbleSortLevelMain
from src.BinarySearch.BinarySearchMain import BinarySearchMain
from src.PlayFair.PlayFairMain import PlayFairMain
from src.Menu.MenuClass import MenuClass

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()
pygame.display.set_caption('Tree of Life')
pygame.display.set_icon(main_img.wiking_icon)


class GameController(object):
    def __init__(self):
        self.current_level = 1

    def controller(self):
        menu = MenuClass('start')
        if menu.run():
            cutscena1 = BreakingClass(main_img.cutscena_1)
            cutscena1.run()
            if cutscena1.is_done is True:
                lvl1 = Level_1_Main()
                player = Player(3, main_img.stand_right, False)
                while True:
                    if self.current_level == 1 and lvl1.is_done is False:
                        lvl1.run()
                        if lvl1.is_done:
                            self.current_level = 2
                            cutscena2 = BreakingClass(main_img.cutscena_2)
                            cutscena2.run()
                    if self.current_level == 2 and cutscena2.is_done is True:
                        lvl_platform = ExampleLvl(player)
                        player.rect.center = lvl_platform.get_surface().get_rect().center
                        player.level = lvl_platform
                        lvl_platform.update()
                        if lvl_platform.run() and player.life.player_life != 0:
                            self.current_level = 3
                            cutscena3 = BreakingClass(main_img.cutscena_3)
                            cutscena3.run()
                    if self.current_level == 3 and cutscena3.is_done and player.life.player_life != 0:
                        bubble = BubbleSortLevelMain()
                        if bubble.run():
                            self.current_level = 4
                            cutscena4 = BreakingClass(main_img.cutscena_4)
                            cutscena4.run()
                    if self.current_level == 4 and cutscena4.is_done and player.life.player_life != 0:
                        lvl_platform2 = ExampleLvl2(player)
                        player.rect.center = lvl_platform2.get_surface().get_rect().center
                        player.level = lvl_platform2
                        lvl_platform2.update()
                        if lvl_platform2.run():
                            self.current_level = 5
                            cutscena5 = BreakingClass(main_img.cutscena_5)
                            cutscena5.run()
                    if self.current_level == 5 and cutscena5.is_done and player.life.player_life != 0:
                        playfair = PlayFairMain()
                        if playfair.run():
                            self.current_level = 5
                            cutscena6 = BreakingClass(main_img.cutscena_6)
                            cutscena6.run()
                    if self.current_level == 5 and cutscena6.is_done and player.life != 0:
                        binary_search = BinarySearchMain(playfair.crypto.output_text)
                        if binary_search.run():
                            self.current_level = 6
                            cutscena7 = BreakingClass(main_img.cutscena_7)
                            cutscena7.run()
                    if self.current_level == 6 and cutscena7.is_done and player.life.player_life != 0:
                        menu2 = MenuClass("finish")
                        if menu2.run():
                            self.current_level = 1
                            lvl1 = Level_1_Main()
                    if player.life.player_life == 0:
                        menu3 = MenuClass("finish")
                        if menu3.run():
                            self.current_level = 1
                            lvl1 = Level_1_Main()
