from src.PlatformsMainPackage.EnemyClass import EnemyClass
from src.PlatformsMainPackage.Platforms import Platforms
import random
import src.MainImages as main_img


"""
Klasa niemal identyczna do src.PlatformsMainPackage.Platforms, 
jednakże zarządzająca również poruszaniem się przeciwnika
"""


class PlatformsWithEnemies(Platforms):
    def __init__(self,  width, height, rect_x, rect_y, start_enemy_img, life=1):
        """

        :param width: pozycja platformy
        :type width: int
        :param height: pozycja platformy
        :type height: int
        :param rect_x: pozycja platformy
        :type rect_x: int
        :param rect_y: pozycja platformy
        :type rect_y: int
        :param start_enemy_img: startowy obrazek przeciwnika
        :type start_enemy_img: pytgame img
        :param life: ilość życia przeciwnika
        :type life: int
        """
        super().__init__(width, height, rect_x, rect_y)
        self.enemy = EnemyClass(start_enemy_img, life, self.rect)
        self.rect.bottom = self.rect.bottom
        self.rect.center = (self.rect.x + random.randint(0, self.width), self.rect.y)

    def update_enemy_platform(self):
        self.enemy.enemy_update()
        if self.rect.left <= self.enemy.rect.x:
            self.enemy.enemy_movement_x *= -1
        elif self.rect.right + self.width <= self.enemy.rect.x:
            self.enemy.enemy_movement_x *= -1
        print(str(self.rect.right + self.width) + "\t" + str(self.enemy.rect.x))

    def draw(self, surface):
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
        self.enemy.set_to_start_position(surface)
        if blocks_counter == 1:
            surface.blit(main_img.single_platform, self.rect)
        else:
            for i in range(blocks_counter):
                if i == 0:
                    surface.blit(main_img.platform_left, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                elif i == blocks_counter - 1:
                    surface.blit(main_img.platform_right, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                else:
                    surface.blit(main_img.platform_center, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
