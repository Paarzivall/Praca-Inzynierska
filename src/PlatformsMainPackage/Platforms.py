import pygame
import src.MainImages as main_img

"""
Główna klasa odpowiadająca za platformy po których będzie się poruszał nasz gracz jak również przeciwnicy
"""


class Platforms(pygame.sprite.Sprite):

    def __init__(self, width, height, rect_x, rect_y):
        """

        :params: współrzędne opisujące położenie danej platformy
        :type: int
        """
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.start_position_x = rect_x
        self.rect.y = self.start_position_y = rect_y
        self.ok = True

    def set_to_start_position(self):
        """
        ustawienie platform do pozycji startowej po spadnięciu gracza za obrys planszy
        :return: None
        """
        self.rect[0] = self.start_position_x
        self.rect[1] = self.start_position_y

    def move_platform_x(self, speed):
        """
        metoda służąca za poruszanie się platformy na osi OX
        :param speed: szybkość z jaką ma się poruszać platforma
        :type speed: int
        :return: None
        """
        self.rect[0] += speed

    def move_platform_y(self, speed):
        """
        metoda służąca do poruszania platformą wzdłuż osi OY
        :param speed: szybkość z jaką ma się poruszać platforma
        :type speed: int
        :return: None
        """
        if not (self.rect[1] > self.start_position_y - 70 and speed > 0):
            self.rect[1] = self.start_position_y
        elif not (self.rect[1] < self.start_position_y - 70 and speed < 0):
            self.rect[1] = self.start_position_y
        else:
            self.rect[1] += speed

    def draw(self, surface):
        """
        metoda dzięki której rysowane są platformy w zależności od wielkości oraz obliczanie pozycji poszczególnych
        elementów platformy
        :param surface: miejsce na którym będzie rysowana platforma
        :type surface: pygame img
        :return: None
        """
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
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
