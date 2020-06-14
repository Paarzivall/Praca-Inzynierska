import pygame
import src.MainImages as main_img
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
        self.falling = False
        self.min_y = None
        self.start_player_position_x = self.rect[0]
        self.start_player_position_y = self.rect[1]

    def draw(self, board):
        board.blit(self.actual_image, self.rect)

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
            self.falling = False

    def _gravity(self):
        if self.player_movement_y == 0:
            self.player_movement_y = 1
        else:
            self.player_movement_y += 0.35
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.turn_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.jump()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player_movement_x < 0:
                self.stop()
                self.actual_image = main_img.stand_left
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player_movement_x > 0:
                self.stop()
                self.actual_image = main_img.stand_right

    def update_images(self):
        self.falling = False
        self._gravity()
        self.rect[0] += self.player_movement_x
        collisions = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for col in collisions:
            if self.player_movement_x < 0 and (self.player_movement_y < 0 or self.player_movement_y != 1):
                self.rect.left = col.rect.right
            if self.player_movement_x > 0 and (self.player_movement_y < 0 or self.player_movement_y != 1):
                self.rect.right = col.rect.left

        if self.player_movement_x < 0:
            self._move(main_img.images_left)
        if self.player_movement_x > 0:
            self._move(main_img.images_right)
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
                self.falling = True
            if self.player_movement_y < 0:
                self.actual_image = main_img.jump_right
                self.falling = False

        if self.direction_of_movement == "left":
            if self.player_movement_y > 0:
                self.actual_image = main_img.fail_left
                self.falling = True
            if self.player_movement_y < 0:
                self.actual_image = main_img.jump_left
                self.falling = False
        if self.player_movement_y == 0 and self.player_movement_x == 0:
            self.falling = False
            if self.direction_of_movement == "left":
                self.actual_image = main_img.stand_left
            else:
                self.actual_image = main_img.stand_right
        if self.rect[1] > self.min_y:
            if self.direction_of_movement == 'left':
                self.actual_image = main_img.fail_left
                self.falling = True
            else:
                self.actual_image = main_img.fail_right
                self.falling = True
            self.rect[0] = self.start_player_position_x
            self.rect[1] = self.start_player_position_y
            self.life.del_life(1)