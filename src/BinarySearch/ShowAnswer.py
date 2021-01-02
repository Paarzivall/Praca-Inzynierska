import pygame


class ShowAnswer(object):
    def __init__(self):
        self.answer = []
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.position = (500, 20)

    def add_letter_to_answer(self, letter):
        self.answer.append(letter)

    def draw(self, surface):
        for nr, letter in enumerate(self.answer):
            surface.blit(self.font.render(str(letter), False, (0, 0, 0)), (self.position[0] + nr * 20, self.position[1] + 20))
