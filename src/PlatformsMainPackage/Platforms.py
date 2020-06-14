import pygame
import src.MainImages as main_img


class Platforms(pygame.sprite.Sprite):

    def __init__(self, width, height, rect_x, rect_y):
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.start_position_x = rect_x
        self.rect.y = self.start_position_y = rect_y

    def set_to_start_position(self):
        self.rect[0] = self.start_position_x
        self.rect[1] = self.start_position_y

    def move_platform_x(self, speed):
        self.rect[0] += speed

    def move_platform_y(self, speed):
        self.rect[1] += speed

    def draw(self, surface):
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
        for i in range(blocks_counter):
            if i == 0:
                surface.blit(main_img.platform_left, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
            elif i == blocks_counter - 1:
                surface.blit(main_img.platform_right, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
            else:
                surface.blit(main_img.platform_center, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
