import pygame
import src.MainImages as main_img


class Pins(object):
    def __init__(self):
        self.board = pygame.display.get_surface()
        self.pins_up = main_img.pins_up
        self.pins_down = main_img.pins_down
        self.positions_up = {0: (718, 153), 1: (798, 158), 2: (866, 163), 3: (928, 168), 4: (984, 173),
                             5: (1036, 176), 6: (1081, 180)}
        self.positions_down = {0: (718, 338), 1: (798, 333), 2: (866, 328), 3: (928, 324), 4: (985, 322),
                               5: (1036, 318), 6: (1081, 316)}

    def draw_pins(self):
        for position, element in enumerate(self.pins_up):
            self.board.blit(self.pins_up[element], self.positions_up[position])

        self.board.blit(self.pins_down[0], self.positions_down[0])
        self.board.blit(self.pins_down[1], self.positions_down[1])
        self.board.blit(self.pins_down[2], self.positions_down[2])
        self.board.blit(self.pins_down[3], self.positions_down[3])
        self.board.blit(self.pins_down[4], self.positions_down[4])
        self.board.blit(self.pins_down[5], self.positions_down[5])
        self.board.blit(self.pins_down[6], self.positions_down[6])