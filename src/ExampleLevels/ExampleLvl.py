import pygame
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
from src.PlatformsMainPackage.MainItem import MainItem
import src.MainImages as main_img


class ExampleLvl(BaseLevelPlatform):
    def __init__(self, player=Player):
        super().__init__(main_img.platform_background2, player)
        self.surface = pygame.display.get_surface()
        self.is_done = True
        # przy liście platform zakładam że 1 na liście jest zawsze startową platformą
        # [długość platformy, punkt startowy, przesunięcie na osi X, przesunięcie na osi Y]
        list_platforms = [[980, 0, 0, main_img.HEIGHT - 170],
                          [420, 70, 750, 350]]
        platform_for_enemies = [1]
        self.calculate_min_y_of_platforms(list_platforms)

        for nr_platformy, parametry in enumerate(list_platforms):
            platform = Platforms(*parametry)
            for enemy in platform_for_enemies:
                if enemy == nr_platformy:
                    self.set_of_enemies.add(platform)
                    self.generate_enemies_on_platforms(platform)
                else:
                    continue
            self.set_of_platforms.add(platform)

    def get_surface(self):
        return self.surface

                            #[420, 70, 750, 350],
                            #[350, 70, 1240, 600]]

        # list_of_enemies = [[420, 70, 750, 350]]
                    #[320, 70, -450, -320]]
                           #[560, 70, 0, 170]]