import pygame
import random
from src.PlatformsMainPackage.BaseLevelPlatform import BaseLevelPlatform
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms
from src.PlatformsMainPackage.TransportPlatforms import TransportPlatforms
import src.MainImages as main_img


class ExampleLvl2(BaseLevelPlatform):
    def __init__(self, player=Player):
        super().__init__(main_img.ancient_forrest, player)
        self.surface = pygame.display.get_surface()
        self.is_done = False
        # przy liście platform zakładam że 1 na liście jest zawsze startową platformą
        # zakładam że po dostaniu się na podaną platformę level jest ukończony
        # [długość platformy, punkt startowy, przesunięcie na osi X, przesunięcie na osi Y]
        list_platforms = [[980, 0, 0, main_img.HEIGHT - 170],
                          [140, 737, 1300, main_img.HEIGHT - 170],
                          [350, 170, 1700, main_img.HEIGHT - 170],
                          [70, 220, 2200, main_img.HEIGHT - 170],
                          [70, 240, 2400, main_img.HEIGHT - 170],
                          [70, 260, 2600, main_img.HEIGHT - 170],
                          [70, 290, 2900, main_img.HEIGHT - 170],
                          [70, 320, 3200, main_img.HEIGHT - 170],
                          [70, 350, 3500, main_img.HEIGHT - 170],
                          [70, 350, 3500, main_img.HEIGHT - 170],
                          [70, 350, 3500, main_img.HEIGHT - 170],
                          [490, 400, 4000, 300],  # 9
                          ]
        transport_platforms = [
                               [210, 370, 3700, 210],#8
                               ]
        self.calculate_min_y_of_platforms(list_platforms)
        self.help_image = main_img.helper_platform_2
        platform_for_enemies = [1, 2, 2]
        finish_platform = 11
        dict_with_items = {}

        self.player.rect.x = self.player.start_player_position_x = 20
        self.player.rect.y = self.player.start_player_position_y = 20

        self.platform_with_tip = 1
        self.platform_with_potion = random.randint(0, len(list_platforms))
        self.platforms_with_heart = 6
        for nr_platformy, parametry in enumerate(list_platforms):
            platform = Platforms(*parametry, 'normal', main_img.platforms_stone)
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
                    self.generate_enemies_on_platforms(platform, random.randint(1, 3), random.randint(0, 2))
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