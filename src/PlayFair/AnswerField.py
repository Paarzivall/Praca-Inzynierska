import pygame


class AnswerField(object):
    def __init__(self):
        self.image = pygame.Surface([600, 105], pygame.SRCALPHA, 32)
        # self.image.fill((255, 255, 255))
        # self.image.set_alpha(128)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 80

    def draw(self, surface):
        surface.blit(self.image, self.rect)