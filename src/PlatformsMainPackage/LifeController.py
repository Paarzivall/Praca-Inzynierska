import src.MainImages as main_img

"""
Główna klasa kontrolująca ilość życia gracza
"""


class LifeController(object):
    _instance = None

    @staticmethod
    def get_instance():
        """
        metoda pomocnicza do zaimplementowania wzorca projektowego "Singleton"
        :return: instancja tej klasy
        """
        if LifeController._instance is None:
            return LifeController()
        else:
            return LifeController._instance

    def __init__(self, player_life):
        """

        :param player_life: ilość życia, którą gracz będzie posiadał "na start"
        :type player_life: int
        """
        if LifeController._instance is None:
            self.player_life = player_life
            self.player_life_position = [30, 30]
        LifeController._instance = self

    def add_life(self):
        """
        metoda dzięki której wywołaniu gracz dostanie dodatkowe życie
        :return: None
        """
        self.player_life += 1

    def del_life(self, minus=1):
        """
        metoda służąca do usuwania życia gracza
        :param minus: ilość życia do odjęcia
        :type minus: int
        :return: None
        """
        self.player_life -= minus

    def draw_player_life(self, board):
        """
        metoda służąca do "rysowania" życia gracza na ekranie
        :param board: miejsce na którym mają być rysowane "życia" gracza
        :type board: pygame surface
        :return: None
        """
        for life in range(self.player_life):
            board.blit(main_img.heart, (self.player_life_position[0], self.player_life_position[1]))
            self.player_life_position[0] += 30
            if life + 1 == self.player_life:
                self.player_life_position[0] = 30

    def is_life(self):
        """
        pomocnicza metoda służąca do sprawdzania czy gracz ma jeszcze życie
        :return: bool'owska wartość w zależności od tego czy gracz posiada jeszcze życie
        """
        if self.player_life > 0:
            return True
        else:
            return False
