import pygame


class MapStaticElements(pygame.sprite.Sprite):
    def __init__(self, image, width, height, rect_x, rect_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = self.width
        self.rect.y = self.height - 300

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_element(self, speed):
        # print(self.width, self.height)
        self.rect.x += speed
