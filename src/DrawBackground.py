import pygame
import pygame.locals
import src.MainImages as main_img


class DrawBackground(object):
    _instance = None

    @staticmethod
    def get_instance():
        if DrawBackground._instance is None:
            DrawBackground(main_img.platform_background)
        return DrawBackground._instance

    def __init__(self, background, start_x, start_y):
        self.background = background
        self.rect = self.background.get_rect()
        self.frame = pygame.display.set_mode((1280, 720))
        self.x = start_x
        self.y = start_y
        self.clock = pygame.time.Clock()
        DrawBackground._instance = self

    def set_to_start_position(self, x, y):
        self.x = x
        self.y = y

    def draw_window(self, *args):
        self.frame.blit(self.background, (self.x, self.y))
        for drawable in args:
            drawable.draw_on(self.frame)

    def set_background(self, background):
        self.background = background

    def get_frame(self):
        return self.frame
