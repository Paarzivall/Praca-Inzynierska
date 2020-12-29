import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.Player import Player
from src.BinarySearch.GenerateTree import GenerateTree
from src.BinarySearch.BinaryPlatforms import BinaryPlatforms
from src.BinarySearch.ShowAnswer import ShowAnswer


class BinarySearchMain(DrawBackground):
    def __init__(self, answer_text):
        super().__init__(main_img.platform_background2, -300, -300)
        self.answer_text = answer_text
        self.show_answer = ShowAnswer()
        self.tree = GenerateTree(list(answer_text))
        self.player_actual_position = 'down'
        self.player = Player(3, main_img.stand_right, True)
        self.player.level = self
        self.player.min_y = 600
        self.player.rect.x = self.player.start_player_position_x = 600
        self.player.rect.y = self.player.start_player_position_y = 500
        self.player_answer = []
        self.is_done = False
        self.board = self.get_frame()
        self.platform_position = {'root': (530, 600), 'left': (130, 300), 'right': (930, 300)}
        self.set_of_platforms = []
        self.actual_height_of_lvl = 0
        self.tree.print_tree()
        self.actual_platform = None
        self.generate_platform()

    def generate_answer(self):
        self.show_answer.answer.append(self.actual_platform.value)

    def generate_platform(self):
        self.set_of_platforms.clear()
        root = self.tree.tree[self.actual_height_of_lvl].root
        left_child = self.tree.tree[self.actual_height_of_lvl].left_child
        right_child = self.tree.tree[self.actual_height_of_lvl].right_child
        self.set_of_platforms.append(BinaryPlatforms(main_img.platform_binary, self.platform_position['root'],
                                                     root, 'normal', 'down')) # root zawsze jest dobrą platformą
        self.set_of_platforms.append(BinaryPlatforms(main_img.platform_binary, self.platform_position['left'],
                                                     left_child, self.check_type_of_platform(left_child), 'up'))
        self.set_of_platforms.append(BinaryPlatforms(main_img.platform_binary, self.platform_position['right'],
                                                     right_child, self.check_type_of_platform(right_child), 'up'))
        self.actual_platform = self.set_of_platforms[0]
        self.generate_answer()

    def check_type_of_platform(self, child):
        if self.tree.tree[self.actual_height_of_lvl + 1].root == child:
            return 'normal'
        else:
            return 'trap'

    def draw(self):
        super().draw_window()
        for platform in self.set_of_platforms:
            platform.draw(self.board)
        self.player.draw(self.board)
        self.show_answer.draw(self.board)

    def update(self):
        self.player.update_images()

    def is_finish(self):
        if self.actual_height_of_lvl == self.tree.height - 1:
            self.is_done = True

    def run(self):
        """
        metoda dzięki której dany level się update'uje: służy jako kontroler levelu
        :return: None
        """
        while not self.handle_events():
            self.is_finish()
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(40)
            if self.is_done:
                break
        return True

    def handle_events(self):
        """
        metoda do przechwytywania eventów "łapanych" przez pygame, oraz zarządzania położeniem platform,
        przeciwników etc.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.turn_left(5)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.turn_right(5)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.jump(-17)
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.player_movement_x < 0:
                    self.player.stop()
                    self.player.actual_image = main_img.stand_left
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.player_movement_x > 0:
                    self.player.stop()
                    self.player.actual_image = main_img.stand_right

