import pygame
from src.DrawBackground import DrawBackground
from src.BinaryConvert.ActionClass import Action
import src.MainImages as main_img
from sys import exit


class Level_1_Main(DrawBackground):

    def __init__(self):
        self.background = main_img.first_background
        super().__init__(self.background, 0, 0)
        self.board = pygame.display.get_surface()
        self.action = Action()
        self.is_done = False
        self.show_helper = False

    def draw(self):
        self.draw_window()
        self.action.draw_action()
        if self.show_helper is True:
            self.board.blit(main_img.helper_binary_convert, (300, 100))

    def run(self):
        while not self.handle_events() and not self.action.end_level():
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)
            return False
        else:
            self.is_done = True

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.show_helper = True
            elif event.type == pygame.KEYUP:
                self.show_helper = False

