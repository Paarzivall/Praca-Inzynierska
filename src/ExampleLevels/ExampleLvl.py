import pygame
import random
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
from src.PlatformsMainPackage.TransportPlatforms import TransportPlatforms
import src.MainImages as main_img


class ExampleLvl(BaseLevelPlatform):
    def __init__(self, player=Player):
        super().__init__(main_img.platform_background2, main_img.draug_blue, player)
        self.surface = pygame.display.get_surface()
        self.is_done = False
        # przy liście platform zakładam że 1 na liście jest zawsze startową platformą
        # zakładam że po dostaniu się na podaną platformę level jest ukończony
        # [długość platformy, punkt startowy, przesunięcie na osi X, przesunięcie na osi Y]
        list_platforms = [[980, 0, 0, main_img.HEIGHT - 170],  #1
                          [420, 70, 1050, 500],  #2
                          [420, 70, 1750, 300],  #4
                          [140, 70, 2400, 300],  #5
                          [280, 70, 2950, 300],  #6
                          [490, 70, 4000, 300],  #9
                          [70, 70, 750, 300],  # extra life
                          ]
        transport_platforms = [[140, 0, 1600, 210],#3
                               [210, 0, 3300, 210],#7
                               [210, 0, 3700, 210],#8
                               ]
        self.help_image = main_img.helper_platform_1
        self.calculate_min_y_of_platforms(list_platforms)
        platform_for_enemies = [1, 1, 3, 5]
        finish_platform = 5
        dict_with_items = {}
        self.platform_with_tip = 2
        self.platform_with_potion = random.randint(0, len(list_platforms))
        self.platforms_with_heart = 6
        for nr_platformy, parametry in enumerate(list_platforms):
            platform = Platforms(*parametry, 'normal', main_img.platforms_grass)
            if self.platform_with_tip == nr_platformy:
                dict_with_items['tip'] = platform
            if self.platform_with_potion == nr_platformy:
                dict_with_items['potion_max_life'] = platform
            if self.platforms_with_heart == nr_platformy:
                dict_with_items['heart'] = platform
            if finish_platform == nr_platformy:
                self.finish_platform = platform
                self.portal = platform
            for enemy in platform_for_enemies:
                if enemy == nr_platformy:
                    self.set_of_enemies.add(platform)
                    self.generate_enemies_on_platforms(platform, 1, random.randint(0, 1))
                else:
                    continue
            self.set_of_platforms.add(platform)
        self.generate_portal()
        self.generate_items_on_map(dict_with_items)

        for transport, parametry in enumerate(transport_platforms):
            platform = TransportPlatforms(*parametry)
            self.set_of_transport_platforms.add(platform)

    def get_surface(self):
        return self.surface