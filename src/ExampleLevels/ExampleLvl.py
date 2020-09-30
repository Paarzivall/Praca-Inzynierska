import pygame
import random
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
from src.PlatformsMainPackage.TransportPlatforms import TransportPlatforms
from src.PlatformsMainPackage.MapStaticElements import MapStaticElements
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
        transport_platforms = [[280, 0, 1400, 210]]
        finish_platform = 2
        self.calculate_min_y_of_platforms(list_platforms)
        self.calculate_len_of_ceiling(list_platforms)
        # list_of_ceiling = [[0, self.len_of_level, -100, -10]]
        list_of_ceiling = [[self.len_of_level + 700, 0, 0, -10]]
        self.create_ceiling(list_of_ceiling)
        self.platform_with_tip = random.randint(0, len(list_platforms))
        for nr_platformy, parametry in enumerate(list_platforms):
            platform = Platforms(*parametry)
            if self.platform_with_tip == nr_platformy:
                self.items(platform)
                self.platform_with_tip = platform
            if finish_platform == nr_platformy:
                self.finish_platform = platform
                self.portal = platform
            for enemy in platform_for_enemies:
                if enemy == nr_platformy:
                    self.set_of_enemies.add(platform)
                    self.generate_enemies_on_platforms(platform, 2, 2)
                else:
                    continue
            self.set_of_platforms.add(platform)
        self.generate_portal()

        for transport, parametry in enumerate(transport_platforms):
            platform = TransportPlatforms(*parametry)
            self.set_of_transport_platforms.add(platform)

    def get_surface(self):
        return self.surface