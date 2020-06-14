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
        # przy liście platform zakładam że 1 na liście jest zawsze startową platformą
        list_platforms = [[420, 70, 750, 350],
                          [980, 70, 0, main_img.HEIGHT - 170],
                          [350, 70, 1240, 600]]
        self.calculate_min_y_of_platforms(list_platforms)

        for w in list_platforms:
            self.set_of_platforms.add(Platforms(*w))

    def get_surface(self):
        return self.surface
