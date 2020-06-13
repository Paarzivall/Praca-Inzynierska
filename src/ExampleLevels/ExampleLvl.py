import pygame
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
import src.MainImages as main_img


class ExampleLvl(BaseLevelPlatform):
    def __init__(self, player=Player):
        super().__init__(main_img.platform_background2, player)
        self.surface = pygame.display.get_surface()
        self.is_done = True
        list_platforms = [[420, 70, 750, 350],
                          [980, 70, 0, main_img.HEIGHT - 70],
                          [560, 70, 0, 650],
                          [140, 70, 1240, 600]]

        for w in list_platforms:
            self.set_of_platforms.add(Platforms(main_img.platform_center, *w))

    def get_surface(self):
        return self.surface

"""
player = Player(3, main_img.stand_right)
lvl = ExampleLvl(player)
player.rect.center = lvl.get_surface().get_rect().center
player.level = lvl
lvl.run()"""
