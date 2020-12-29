import pygame

"""
    Klasa odpowiadająca za pociski generowane przez gracza.
"""


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, bullet_image, direction, rect_center):
        """

        :param bullet_image: obraz pocisku
        :type bullet_image: pygame img
        :param direction: kierunek w którym porusza się pocisk
        :type direction: string
        :param rect_center: podstawa pozycji startowej pocisku - środek postaci gracza
        :type rect_center: tuple
        """
        super().__init__()
        self.bullet_image = bullet_image
        self.bullet_direction = direction
        self.rect = self.bullet_image.get_rect()
        self.rect.center = rect_center
        self.counter = 0

    def draw(self, board):
        """
        metoda służąca do rysowania pocisków na ekranie
        :param board: pole na którym rysujemy
        :type board: pygame surface
        :return: None
        """
        board.blit(self.bullet_image, (self.rect[0] + 10, self.rect[1] + 16))

    def update_bullet(self):
        """
        metoda dzięki której pociski mogą się poruszać z zadaną szybkością
        :return: None
        """
        self.counter += 1
        if self.bullet_direction == 'right':
            self.rect.x += 15
        if self.bullet_direction == 'left':
            self.rect.x -= 15
