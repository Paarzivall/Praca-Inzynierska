import pygame


class MainItem(pygame.sprite.Sprite):
    def __init__(self, item_image, name_of_item):
        super().__init__()
        self.item_image = item_image
        self.rect = self.item_image.get_rect()
        self.name_of_item = name_of_item

    def draw_item(self, board):
        board.blit(self.item_image, self.rect)

    def update_item(self, rect_center):
        self.rect.center = rect_center
