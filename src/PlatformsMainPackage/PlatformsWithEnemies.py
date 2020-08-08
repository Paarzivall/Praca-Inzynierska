from src.PlatformsMainPackage.EnemyClass import EnemyClass
from src.PlatformsMainPackage.Platforms import Platforms
import random
import src.MainImages as main_img


class PlatformsWithEnemies(Platforms):
    def __init__(self,  width, height, rect_x, rect_y, start_enemy_img, life=1):
        super().__init__(width, height, rect_x, rect_y)
        self.enemy = EnemyClass(start_enemy_img, life, self.rect)
        self.rect.bottom = self.rect.bottom
        self.rect.center = (self.rect.x + random.randint(0, self.width), self.rect.y)

    def update_enemy_platform(self):
        # super().update()
        self.enemy.enemy_update()
        if self.rect.left <= self.enemy.rect.x:
            self.enemy.enemy_movement_x *= -1
        elif self.rect.right + self.width <= self.enemy.rect.x:
            self.enemy.enemy_movement_x *= -1
        print(str(self.rect.right + self.width) + "\t" + str(self.enemy.rect.x))

    def draw(self, surface):
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
        self.enemy.set_to_start_position(surface)
        for i in range(blocks_counter):
            if i == 0:
                surface.blit(main_img.platform_left, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
            elif i == blocks_counter - 1:
                surface.blit(main_img.platform_right, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
            else:
                surface.blit(main_img.platform_center, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))