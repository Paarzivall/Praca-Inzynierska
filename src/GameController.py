import os


class GameController(object):
    def __init__(self):
        self.backgrounds = "img/Level1/otwieranie_zamka.png"
        # self.level1_pins = {}
        # self.level1_numbers = {}

    def tmp(self):
        if os.path.isfile(self.level1_background):
            print("ok")
        else: print("nok")

    def get_name(self):
        return self.level1_background


