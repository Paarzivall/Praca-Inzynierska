import pygame


class AnswerField(object):
    def __init__(self):
        self.image = pygame.Surface([600, 75])
        self.image.fill((237, 199, 25))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def draw(self, surface):
        surface.blit(self.image, self.rect)