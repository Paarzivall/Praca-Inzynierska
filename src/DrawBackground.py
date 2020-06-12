import pygame
import pygame.locals


class DrawBackground(object):
    def __init__(self, background):
        self.background = background
        self.frame = pygame.display.set_mode((1280, 720))

    def draw_window(self, *args):
        self.frame.blit(self.background, (0, 0))
        for drawable in args:
            drawable.draw_on(self.frame)

    def get_frame(self):
        return self.frame