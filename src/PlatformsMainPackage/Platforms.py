import pygame
import src.MainImages as main_img


class Platforms(pygame.sprite.Sprite):

    def __init__(self, image_platform, width, height, rect_x, rect_y):
        # self.surface = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image = self.image.convert()
        self.image.fill((250, 250, 250))
        # self.image.blit(main_img.platform_center, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        # print(self.rect.x, self.rect.y)

    def set_platforms_positions(self):
        # 650 - dolne platformy - przy założeniu że lvl jest easy
        # co 70 ustawianie platform do chodzenia
        pass

    def draw(self, surface):
        blocks_counter = int(self.width / 70)
        for i in range(blocks_counter):
            if i == 0:
                surface.blit(main_img.platform_left, (self.rect[0] + i * 70, self.rect[1]))
            elif i == blocks_counter - 1:
                surface.blit(main_img.platform_right, (self.rect[0] + i * 70, self.rect[1]))
            else:
                surface.blit(main_img.platform_center, (self.rect[0] + i * 70, self.rect[1]))
