import pygame
import os
import src.MainImages as main_img
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.Platforms import Platforms

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()


class BaseLevelPlatform(DrawBackground):

    def __init__(self, player_lives, platform_number=5, platform_enemy_number=0, difficulty='easy'):
        self.background = main_img.platform_background
        super().__init__(self.background)
        self.list_of_platforms = [(0, 650), (70, 650), (140, 650),
                                  (210, 650), (280, 650), (350, 650),
                                  (420, 650), (490, 650), (560, 650),
                                  (630, 650)]
        self.player = Player(player_lives, main_img.stand_right)
        self.player.rect = self.frame.get_rect()
        self.player.level = self.list_of_platforms
        self.platforms = Platforms(platform_number, platform_enemy_number, difficulty, self.list_of_platforms)
        self.platform_number = platform_number
        self.platform_enemy_number = platform_enemy_number
        self.difficulty = difficulty
        self.clock = pygame.time.Clock()
        self.board = pygame.display.get_surface()
        self.is_done = True

    def get_platforms(self):
        return self.list_of_platforms

    def draw(self):
        self.draw_window()
        self.platforms.draw()
        self.player.draw()
        self.player.update_images()

    def run(self):
        while not self.handle_events():
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def handle_events(self):
        """Metoda pozwalająca zamknąć okienko"""
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    print("HELPER")
            self.player.get_event(event)

lvl = BaseLevelPlatform(3)
lvl.run()