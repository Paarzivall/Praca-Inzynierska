import pygame
import src.MainImages as main_img


class Platforms(object):

    def __init__(self, platforms_number, platforms_with_enemies, difficulty, list_of_platforms):
        self.platforms_number = platforms_number
        self.platforms_with_enemies = platforms_with_enemies
        self.difficulty = difficulty
        self.single_platform = main_img.single_platform
        self.platform_left = main_img.platform_left
        self.platform_right = main_img.platform_right
        self.platform_center = main_img.platform_center
        self.surface = pygame.display.get_surface()
        self.list_of_platforms = list_of_platforms

    def set_platforms_positions(self):
        # 650 - dolne platformy - przy założeniu że lvl jest easy
        # co 70 ustawianie platform do chodzenia
        if self.difficulty == 'easy':
            pass

    def draw(self):
        tmp = len(self.list_of_platforms)
        for x in self.list_of_platforms:
            if x == 0:
                self.surface.blit(self.platform_left, x)
            elif x == tmp:
                self.surface.blit(self.platform_right, x)
            else:
                self.surface.blit(self.platform_center, x)
        """self.surface.blit(self.platform_left, (0, 650))
        self.surface.blit(self.platform_center, (70, 650))
        self.surface.blit(self.platform_center, (140, 650))
        self.surface.blit(self.platform_center, (210, 650))
        self.surface.blit(self.platform_center, (280, 650))
        self.surface.blit(self.platform_center, (350, 650))
        self.surface.blit(self.platform_center, (420, 650))
        self.surface.blit(self.platform_center, (490, 650))
        self.surface.blit(self.platform_center, (560, 650))
        self.surface.blit(self.platform_right, (630, 650))"""