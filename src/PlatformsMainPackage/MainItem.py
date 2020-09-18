import pygame

"""
Klasa odpowiadająca różnym item'om w grze takim jak na przykłąd broń
"""


class MainItem(pygame.sprite.Sprite):
    def __init__(self, item_image, name_of_item):
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

    def draw_item(self, board):
        """
        metoda służąca do rysowania przedmiotu na ekranie
        :param board: miejsce na którym można rysować przedmioty
        :type board: pygame surface
        :return: None
        """
        board.blit(self.item_image, (self.rect[0] + 20, self.rect[1] + 20))

    def update_item(self, rect_center):
        """
        metoda pozycjonująca broń w centrum postaci gracza
        :param rect_center: współrzędne postaci gracza
        :type rect_center: tuple
        :return: None
        """
        self.rect.center = rect_center
