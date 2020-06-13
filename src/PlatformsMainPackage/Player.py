import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.LifeController import LifeController


class Player(pygame.sprite.Sprite):
    def __init__(self, life, start_image):
        super().__init__()
        self.life = LifeController(life)
        self.actual_image = start_image
        self.rect = self.actual_image.get_rect()
        self.direction_of_movement = 'right'
        self.count = 0
        self.level = None
        self.rect = self.actual_image.get_rect()
        self.player_movement_x = 0
        self.player_movement_y = 0
        self.draw_back = DrawBackground.get_instance()


    def draw(self, board):
        board.blit(self.actual_image, self.rect)
        # self.life.draw_player_life(board)

    def turn_left(self):
        self.direction_of_movement = 'left'
        self.player_movement_x = -5

    def turn_right(self):
        self.direction_of_movement = 'right'
        self.player_movement_x = 5

    def stop(self):
        self.player_movement_x = 0

    def jump(self):
        if self.player_movement_y == 0:
            self.player_movement_y = -20

    def _gravity(self):
        if self.player_movement_y == 0:
            self.player_movement_y = 1
        else:
            self.player_movement_y += 0.5
            # self.draw_back.add_y_position(10)
        if self.player_movement_y > 15:
            self.player_movement_y = 14

    def _move(self, images):
        if self.count < 4:
            self.actual_image = images[0]
        if self.count >= 4 and self.count < 8:
            self.actual_image = images[1]

        if self.count > 8:
            self.count = 0
        else:
            self.count += 1

    def get_event(self, event):
        left_pressed = False
        right_pressed = False
        jump_pressed = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.turn_left()
                left_pressed = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.turn_right()
                right_pressed = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.jump()
                jump_pressed = True
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player_movement_x < 0:
                self.stop()
                self.actual_image = main_img.stand_left
                left_pressed = False
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player_movement_x > 0:
                self.stop()
                self.actual_image = main_img.stand_right
                right_pressed = False

        if left_pressed is True:
            print("jeden")
            self.draw_back.add_x_position(-10)
        if right_pressed is True:
            print("jeden1")
            self.draw_back.add_x_position(10)
        if jump_pressed is True:
            print("jeden2")
            self.draw_back.add_y_position(-10)

    def update_images(self):
        self.rect[0] += self.player_movement_x
        collisions = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for col in collisions:
            if self.player_movement_x > 0:
                self.rect.left = col.rect.right
            if self.player_movement_x < 0:
                self.rect.right = col.rect.left

        if self.player_movement_x < 0:
            self._move(main_img.images_left)
        if self.player_movement_x > 0:
            self._move(main_img.images_right)
        self._gravity()
        self.rect[1] += self.player_movement_y

        collisions = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for col in collisions:
            if self.player_movement_y < 0:
                self.rect.top = col.rect.bottom
            if self.player_movement_y > 0:
                self.rect.bottom = col.rect.top
            self.player_movement_y = 0

        if self.direction_of_movement == "right":
            if self.player_movement_y > 0:
                self.actual_image = main_img.fail_right
            if self.player_movement_y < 0:
                self.actual_image = main_img.jump_right

        if self.direction_of_movement == "left":
            if self.player_movement_y > 0:
                self.actual_image = main_img.fail_left
            if self.player_movement_y < 0:
                self.actual_image = main_img.jump_left
        if self.player_movement_y == 0 and self.player_movement_x == 0:
            if self.direction_of_movement == "left":
                self.actual_image = main_img.stand_left
            else:
                self.actual_image = main_img.stand_right
        if self.rect[1] > 640:
            if self.direction_of_movement == 'left':
                self.actual_image = main_img.fail_left
            else:
                self.actual_image = main_img.fail_right
            self.rect[0] = 50
            self.rect[1] = 520
            self.life.del_life(1)
