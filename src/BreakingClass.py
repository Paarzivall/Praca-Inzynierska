import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground


class BreakingClass(DrawBackground):
    def __init__(self, img):
        super().__init__(img, -300, -300)
        self.is_done = False

    def draw(self):
        self.draw_window()

    def run(self):
        while not self.handle_events() and self.is_done is False:
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)
            if self.is_done:
                break

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    self.is_done = True

