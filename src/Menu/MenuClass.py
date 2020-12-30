import pygame
from src.DrawBackground import DrawBackground
import src.MainImages as main_img


class MenuClass(DrawBackground):
    def __init__(self, mode):
        super().__init__(main_img.menu_background, 0, 0)
        self.board = self.get_frame()
        self.start_button = main_img.start_button
        self.end_button = main_img.end_button
        self.again = main_img.again_button
        self.is_done = False
        self.rect = pygame.Rect((400, 520), (500, 100))
        self.mode = mode

    def draw_title(self):
        shape_surf = pygame.Surface(pygame.Rect((400, 520), (500, 100)).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, (169, 169, 169, 128), shape_surf.get_rect())
        self.board.blit(shape_surf, ((400, 520), (500, 100)))
        self.board.blit(main_img.title, (400, 500))

    def draw_button_start(self):
        self.board.blit(self.start_button, (100, 100))
        self.board.blit(self.end_button, (1000, 100))

    def draw_button_end(self):
        self.board.blit(self.again, (100, 100))
        self.board.blit(self.end_button, (1000, 100))

    def draw_start(self):
        super().draw_window()
        self.draw_button_start()
        self.draw_title()

    def draw_end(self):
        super().draw_window()
        self.draw_button_end()
        self.draw_title()

    def run(self):
        while not self.handle_events():
            if self.mode == 'start':
                self.draw_start()
            else:
                self.draw_end()
            pygame.display.flip()
            self.clock.tick(30)
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
                    if self.mode == 'start':
                        tmp_ev = self.board.blit(self.start_button,
                                                 (100, 100))
                        if tmp_ev.collidepoint(event.pos):
                            self.is_done = True
                            return True

                    tmp_ev = self.board.blit(self.end_button,
                                             (1000, 100))
                    if tmp_ev.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                        return True
                    if self.mode == 'finish':
                        tmp_ev = self.board.blit(self.again,
                                                 (100, 100))
                        if tmp_ev.collidepoint(event.pos):
                            return True

