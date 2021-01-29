import pygame


class BinaryPlatforms(object):
    def __init__(self, img, position, value, letter_value, type, mode):
        self.image = img
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.value = value
        self.letter_value = letter_value
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.type = type
        self.mode = mode
        self.show_for_user = self.value + '(' + self.letter_value + ')'

    def draw(self, surface):
        surface.blit(self.image, self.position)
        surface.blit(self.font.render(self.show_for_user, False, (255, 255, 255 )), (self.position[0] + 90, self.position[1] + 20))
