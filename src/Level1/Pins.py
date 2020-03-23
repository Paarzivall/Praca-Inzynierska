import pygame
from src.ResizeClass import resize


class Pins(object):
    def __init__(self):
        self.board = pygame.display.get_surface()
        self.pins_up = {"1G": "../../img/Level1/Bolce/bolec_1_gora.png",
                     "2G": "../../img/Level1/Bolce/bolec_2_gora.png",
                     "3G": "../../img/Level1/Bolce/bolec_3_gora.png",
                     "4G": "../../img/Level1/Bolce/bolec_4_gora.png",
                     "5G": "../../img/Level1/Bolce/bolec_5_gora.png",
                     "6G": "../../img/Level1/Bolce/bolec_6_gora.png",
                     "7G": "../../img/Level1/Bolce/bolec_7_gora.png"}
        self.pins_down = {}
        self.positions_up = {0: (718, 153), 1: (798, 158), 2: (866, 163), 3: (928, 168), 4: (984, 173),
                          5: (1036, 176), 6: (1081, 180)}
        self.positions_down = {"1D": "../../img/Level1/Bolce/bolec_1_dol.png",
                               "2D": "../../img/Level1/Bolce/bolec_2_dol.png",
                               "3D": "../../img/Level1/Bolce/bolec_3_dol.png",
                               "4D": "../../img/Level1/Bolce/bolec_4_dol.png",
                               "5D": "../../img/Level1/Bolce/bolec_5_dol.png",
                               "6D": "../../img/Level1/Bolce/bolec_6_dol.png",
                               "7D": "../../img/Level1/Bolce/bolec_7_dol.png"
                               }
        self.load_pins()

    def load_pins(self):
        for pin in self.pins_up:
            image = resize(pygame.image.load(self.pins_up[pin]))
            self.pins_up.update({pin: image})

    def draw_pins(self):
        for position, element in enumerate(self.pins_up):
            self.board.blit(self.pins_up[element], self.positions_up[position])