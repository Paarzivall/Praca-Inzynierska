import src.MainImages as main_img
from src.PlatformsMainPackage.Platforms import Platforms


class TransportPlatforms(Platforms):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.direction = "top"

    def update_transport_platform(self):
        super().update()
        if self.direction == 'top':
            self.rect.y -= 2
        else:
            self.rect.y += 2

    def set_direction(self):
        if self.rect.top == main_img.HEIGHT - 170:
            self.direction = 'top'
        elif self.rect.top == 200:
            self.direction = 'bottom'

    def draw(self, surface):
        blocks_counter = int(self.width / main_img.BLOCKS_WIDTH)
        if blocks_counter == 1:
            surface.blit(main_img.single_transport_platform, self.rect)
        else:
            for i in range(blocks_counter):
                if i == 0:
                    surface.blit(main_img.transport_platform_left,
                                 (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                elif i == blocks_counter - 1:
                    surface.blit(main_img.transport_platform_right,
                                 (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
                else:
                    surface.blit(main_img.transport_platform_center,
                                 (self.rect[0] + i * main_img.BLOCKS_WIDTH, self.rect[1]))
