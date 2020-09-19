import pygame


class MapStaticElements(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = self.start_position_x = self.width
        self.rect.y = self.start_position_y = self.height - 300

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move_element(self, speed):
        self.rect.x += speed

    def set_to_start_position(self):
        self.rect.x = self.start_position_x
        self.rect.y = self.start_position_y

