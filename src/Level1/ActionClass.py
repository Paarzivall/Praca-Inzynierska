import pygame
from sys import exit
from time import sleep
from src.Level1.Pins import Pins
from src.Level1.Numbers import Numbers


class Action(Pins):
    def __init__(self):
        super().__init__()
        self.numbers = Numbers()
        print(self.numbers.binary)
        self.actual_positions = [1, 1, 1, 1, 1, 1, 1]
        self.end_level()

    def draw_action(self):
        self.numbers.draw_numbers()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for pin in self.pins_up:
            if self.actual_positions[pin] == 1:
                self.board.blit(self.pins_up[pin], self.positions_up[pin])
            else:
                self.board.blit(self.pins_down[pin], self.positions_down[pin])
            if pygame.MOUSEBUTTONUP:
                if click == (1, 0, 0):
                    if self.actual_positions[pin] == 1:
                        event = self.board.blit(self.pins_up[pin], self.positions_up[pin]).collidepoint(mouse)
                        if event:
                            self.event_up(pin)
                    else:
                        event = self.board.blit(self.pins_down[pin], self.positions_down[pin]).collidepoint(mouse)
                        if event:
                            self.event_down(pin)
        if self.end_level():
            exit()

    def event_up(self, pin):
        self.board.blit(self.pins_down[pin], self.positions_down[pin])
        self.actual_positions[pin] = 0

    def event_down(self, pin):
        self.board.blit(self.pins_up[pin], self.positions_up[pin])
        self.actual_positions[pin] = 1

    def end_level(self):
        if self.actual_positions == self.numbers.binary:
            return True
        else:
            return False
