import pygame
import src.MainImages as main_img


class CeilingClass(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        """
        :params: współrzędne opisujące położenie danego sufitu
        :type: int
        """
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.start_position_x = rect_x
        self.rect.y = self.start_position_y = rect_y

    """def __init__(self, start_position_x, start_position_y, len_of_ceiling):
        self.image = pygame.Surface([980, 150])
        self.image = self.image.convert()
        self.image.fill((250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.start_position = start_position_x
        self.rect.y = self.finish_position = start_position_y
        self.width = len_of_ceiling"""

    def draw(self, surface):
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
        if blocks_counter == 1:
            surface.blit(main_img.single_platform, self.rect)
        else:
            for i in range(blocks_counter):
                if i == 0:
                    surface.blit(main_img.ceiling_left, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                elif i == blocks_counter - 1:
                    surface.blit(main_img.ceiling_right, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                else:
                    surface.blit(main_img.ceiling_center, (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))

    def move_ceiling_x(self, speed):
        self.rect[0] += speed
