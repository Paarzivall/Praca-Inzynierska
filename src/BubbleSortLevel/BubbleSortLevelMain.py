import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground
from src.BubbleSortLevel.SwitchingNumbers import SwitchingNumbers
from src.BubbleSortLevel.SwitchingButtons import SwitchingButtons


class BubbleSortLevelMain(DrawBackground):
    def __init__(self):
        super().__init__(main_img.bubble_background, 0, 0)
        self.numbers = SwitchingNumbers()
        self.board = self.get_frame()
        self.buttons = SwitchingButtons(4)
        self.is_done = False

    def draw(self):
        self.draw_window()
        self.numbers.draw(self.board)
        self.buttons.draw(self.board)

    def run(self):
        while not self.handle_events():
            self.draw()
            pygame.display.flip()
            self.clock.tick(10)
        return True

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # tutaj zapewnione przejście do następnej pary cyfr
                    tmp_ev = self.board.blit(self.buttons.next_button, self.buttons.next_button_pos)
                    if tmp_ev.collidepoint(event.pos):
                        if self.buttons.active_button < 3:
                            self.buttons.active_button += 1
                        else:
                            self.buttons.active_button = 0
                    # tutaj przesunięcie aktywnego przycisku
                    tmp_ev = self.board.blit(self.buttons.buttons[self.buttons.active_button],
                                             self.buttons.button_positions[self.buttons.active_button])
                    if tmp_ev.collidepoint(event.pos):
                        # zamiana miejscami danych cyfr
                        self.numbers.switch_positions(self.buttons.active_button)
                    tmp_ev = self.board.blit(self.buttons.lock, self.buttons.lock_pos)
                    if tmp_ev.collidepoint(event.pos):
                        if self.numbers.is_finish() is True:
                            self.is_done = True
                            return True
