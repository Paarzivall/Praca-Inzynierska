import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground


class PlayFairMain(DrawBackground):
    def __init__(self):
        super().__init__(main_img.playfair_background, 0, 0)

    def draw(self):
        self.draw_window()

    def run(self):
        while not self.handle_events():
            self.draw()
            pygame.display.flip()
            self.clock.tick(10)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True

if __name__ == '__main__':
    ob = PlayFairMain()
    ob.run()
