import pygame
from src.ResizeClass import resize


class Pins(object):
    def __init__(self):
        self.board = pygame.display.get_surface()
        self.pins_up = {0: "../../img/Level1/Bolce/bolec_1_gora.png",
                        1: "../../img/Level1/Bolce/bolec_2_gora.png",
                        2: "../../img/Level1/Bolce/bolec_3_gora.png",
                        3: "../../img/Level1/Bolce/bolec_4_gora.png",
                        4: "../../img/Level1/Bolce/bolec_5_gora.png",
                        5: "../../img/Level1/Bolce/bolec_6_gora.png",
                        6: "../../img/Level1/Bolce/bolec_7_gora.png"}
        self.pins_down = {0: "../../img/Level1/Bolce/bolec_1_dol.png",
                          1: "../../img/Level1/Bolce/bolec_2_dol.png",
                          2: "../../img/Level1/Bolce/bolec_3_dol.png",
                          3: "../../img/Level1/Bolce/bolec_4_dol.png",
                          4: "../../img/Level1/Bolce/bolec_5_dol.png",
                          5: "../../img/Level1/Bolce/bolec_6_dol.png",
                          6: "../../img/Level1/Bolce/bolec_7_dol.png"}
        self.positions_up = {0: (718, 153), 1: (798, 158), 2: (866, 163), 3: (928, 168), 4: (984, 173),
                             5: (1036, 176), 6: (1081, 180)}
        self.positions_down = {0: (718, 338), 1: (798, 333), 2: (866, 328), 3: (928, 324), 4: (985, 322),
                               5: (1036, 318), 6: (1081, 316)}
        self.load_pins()
        self.load_pins_down()

    def load_pins(self):
        for pin in self.pins_up:
            image = resize(pygame.image.load(self.pins_up[pin]))
            self.pins_up.update({pin: image})

    def load_pins_down(self):
        for pin in self.pins_down:
            image = resize(pygame.image.load(self.pins_down[pin]))
            self.pins_down.update({pin: image})

    # def draw_pins(self, pin, which, position):

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