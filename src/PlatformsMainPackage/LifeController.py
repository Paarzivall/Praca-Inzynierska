import src.MainImages as main_img


class LifeController(object):
    _instance = None

    @staticmethod
    def get_instance():
        if LifeController._instance is None:
            return LifeController()
        else:
            return LifeController._instance

    def __init__(self, player_life):
        if LifeController._instance is None:
            self.player_life = player_life
            self.player_life_position = [30, 30]
        LifeController._instance = self

    def add_life(self):
        self.player_life += 1

    def del_life(self, minus=1):
        self.player_life -= minus

    def draw_player_life(self, board):
        for life in range(self.player_life):
            board.blit(main_img.heart, (self.player_life_position[0], self.player_life_position[1]))
            self.player_life_position[0] += 30
            if life + 1 == self.player_life:
                self.player_life_position[0] = 30

    def is_life(self):
        if self.player_life > 0:
            return True
        else:
            return False
