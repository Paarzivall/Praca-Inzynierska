import pygame


class BinaryPlatforms(object):
    def __init__(self, img, position, value, type, mode):
        self.image = img
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.value = value
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.type = type
        self.mode = mode

    def draw(self, surface):
        surface.blit(self.image, self.position)
        surface.blit(self.font.render(self.value, False, (0, 0, 0)), (self.position[0] + 90, self.position[1] + 20))
