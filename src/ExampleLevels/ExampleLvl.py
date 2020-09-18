import pygame
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
from src.PlatformsMainPackage.TransportPlatforms import TransportPlatforms
import src.MainImages as main_img


class ExampleLvl(BaseLevelPlatform):
    def __init__(self, player=Player):
        super().__init__(main_img.platform_background2, player)
        self.surface = pygame.display.get_surface()
        self.is_done = False
        # przy liście platform zakładam że 1 na liście jest zawsze startową platformą
        # zakładam że po dostaniu się na podaną platformę level jest ukończony
        # [długość platformy, punkt startowy, przesunięcie na osi X, przesunięcie na osi Y]
        list_platforms = [[980, 0, 0, main_img.HEIGHT - 170],
                          [420, 70, 750, 350],
                          [980, 0, 1600, main_img.HEIGHT - 170]]
        platform_for_enemies = [1]
        transport_platforms = [[280, 0, 1400, 100]]
        finish_platform = 2
        self.calculate_min_y_of_platforms(list_platforms)

        for nr_platformy, parametry in enumerate(list_platforms):
            platform = Platforms(*parametry)
            if finish_platform == nr_platformy:
                self.finish_platform = platform
            for enemy in platform_for_enemies:
                if enemy == nr_platformy:
                    self.set_of_enemies.add(platform)
                    self.generate_enemies_on_platforms(platform, 1)
                else:
                    continue
            self.set_of_platforms.add(platform)

        for transport, parametry in enumerate(transport_platforms):
            platform = TransportPlatforms(*parametry)
            self.set_of_transport_platforms.add(platform)

    def get_surface(self):
        return self.surface