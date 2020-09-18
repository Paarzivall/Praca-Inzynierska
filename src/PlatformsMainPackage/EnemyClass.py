import pygame
import src.MainImages as main_img

"""
Główna klasa Przeciwników, która definiuje ich zachowania, położenie etc.
"""


class EnemyClass(pygame.sprite.Sprite):
    def __init__(self, start_img, life, platform):
        """

        :param start_img: obraz od którego będzie rysowana animacja na ekranie
        :type start_img: pygame img
        :param life: ilość życia przeciwnika
        :type life: int
        :param platform: platforma na której będzie się poruszał przeciwnik
        :type platform: src.PlatformMainPackage.Platform
        """
        super().__init__()
        self.image = start_img
        self.life = life
        self.images_left = main_img.enemy_images_left
        self.images_right = main_img.enemy_images_right
        self.rect = self.image.get_rect()
        self._count = 0
        self.enemy_movement_x = 1
        self.enemy_movement_y = 0
        self.platform = platform
        self.start = self.platform.rect.top
        self.rect.x = self.platform.rect.x
        self.start_x = self.rect.x + 10
        self.start_y = self.platform.rect.y - 110
        self.angle = 0

    def draw_enemy(self, board):
        """
        metoda służąca do rysowania przeciwnika na ekranie
        :param board: miejsce na którym ma być rysowany przeciwnik
        :type board: pygame surface
        :return: None
        """
        if self.platform.rect.x >= self.rect.x:
            self.enemy_movement_x *= -1
        elif self.platform.rect.x + self.platform.width - 70 <= self.rect.x:
            self.enemy_movement_x *= -1
        board.blit(pygame.transform.rotate(self.image, self.angle),
                   (self.rect.x, self.platform.rect.y - 110 - self.enemy_movement_y))

    def move_enemy(self, speed):
        """
        metoda służąca do poruszania się przeciwnika na ekranie
        :param speed: szybkość z jaką ma się przeciwnik poruszać
        :type speed: int
        :return: None
        """
        self.rect[0] += speed

    def enemy_update(self):
        """
        metoda zarządzająca wyświetlaniem przeciwników na ekranie: updateująca obrazki etc.
        :return: None
        """
        self.rect.x += self.enemy_movement_x
        if self.life == 0:
            self.enemy_movement_x = 0
            self.enemy_movement_y = - 100
            self.angle = - 90
            self.kill()
        if self.life > 0:
            if self.enemy_movement_x > 0:
                if self._count < 4:
                    self.image = self.images_right[0]
                if 4 <= self._count < 8:
                    self.image = self.images_right[1]
                if self._count > 7:
                    self._count = 0
            elif self.enemy_movement_x < 0:
                if self._count < 4:
                    self.image = self.images_left[0]
                if 4 <= self._count < 8:
                    self.image = self.images_left[1]
                if self._count > 7:
                    self._count = 0
            else:
                self.image = main_img.enemy_stand_right
            self._count += 1
        else:
            if self.enemy_movement_x >= 0:
                self.image = main_img.enemy_dead_right
            else:
                self.image = main_img.enemy_dead_left

