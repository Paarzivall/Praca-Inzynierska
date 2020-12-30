import pygame
import src.MainImages as main_img

"""
Klasa odpowiadająca różnym item'om w grze takim jak na przykłąd broń
"""


class MainItem(pygame.sprite.Sprite):
    def __init__(self, item_image, name_of_item, platform, picked=True):
        """

        :param item_image: obraz przedmiotu
        :type item_image: pygame img
        :param name_of_item: nazwa danego przedmiotu
        :type name_of_item: string
        """
        super().__init__()
        self.item_image = item_image
        self.rect = self.item_image.get_rect()
        self.name_of_item = name_of_item
        self.platform = platform
        self.picked = picked

    def draw_thumbnail(self, board):
        if self.picked is True:
            board.blit(self.item_image, (1200, 30))

    def draw_item(self, board):
        """
        metoda służąca do rysowania przedmiotu na ekranie
        :param board: miejsce na którym można rysować przedmioty
        :type board: pygame surface
        :return: None
        """
        if self.picked is False:
            board.blit(self.item_image, (self.platform.rect.center[0], self.platform.rect.top - 70))

    def update_item(self, rect_center):
        """
        metoda pozycjonująca broń w centrum postaci gracza
        :param rect_center: współrzędne postaci gracza
        :type rect_center: tuple
        :return: None
        """
        self.rect.center = rect_center

    def draw_tip_full_screen(self, action_button, board, image):
        if self.name_of_item == 'Tip' and action_button is True:
            if self.picked is False:
                board.blit(main_img.helper_platform_none, (300, 100))
            else:
                board.blit(image, (300, 100))