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

    def __init__(self, background):
        self.background = background
        self.frame = pygame.display.set_mode((1280, 720))
        self.x = 0
        self.y = 0
        self.clock = pygame.time.Clock()
        DrawBackground._instance = self

    def draw_window(self, *args):
        size = self.background.get_size()
        if self.x <= 10 or self.y <= 30:
           #  print(self.x, self.y)
            self.frame.blit(self.background, (self.x, self.y))
        else:
            # print(self.x, self.y)
            self.frame.blit(self.background, (self.x - 10, self.y - 10))
        for drawable in args:
            drawable.draw_on(self.frame)

    def set_background(self, background):
        self.background = background

    def get_frame(self):
        # print("frame " + str(self.frame))
        return self.frame

    def add_x_position(self, size=1):
        self.x += size

    def add_y_position(self, size=1):
        self.y += size
