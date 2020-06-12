import pygame
import src.MainImages as main_img


class Player(pygame.sprite.Sprite):
    def __init__(self, lives, start_image):
        self.lives = lives
        self.actual_image = start_image
        self.rect = self.actual_image.get_rect()
        self.player_right = main_img.images_right
        self.player_left = main_img.images_left
        self.direction_of_movement = 'right'
        self.count = 0
        self.level = None
        self.player_position_x = 50
        self.player_movement_x = 0
        self.player_position_y = 540
        self.player_movement_y = 0
        self.surface = pygame.display.get_surface()

    def draw(self):
        # self.surface.blit(self.actual_image, self.rect.center)
        self.surface.blit(self.actual_image, (self.player_position_x, self.player_position_y))

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
            self.player_movement_y = -7

    def _gravity(self):
        if self.player_movement_y == 0:
            self.player_movement_y = 1
        else:
            self.player_movement_y += 0.5
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
            if event.key == pygame.K_LEFT:
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
        self.player_position_x += self.player_movement_x
        # collisions = pygame.sprite.spritecollide(self, self.level, False)
       # collisions = pygame.sprite.collide_rect(self.rect, self.level)
        #for o in collisions:
         #   if self.movement_x > 0:
          #      self.rect.left = o.rect.right
           # if self.movement_x < 0:
            #    self.rect.right = o.rect.left
        if self.player_movement_x < 0:
            self._move(self.player_left)
        if self.player_movement_x > 0:
            self._move(self.player_right)
        # self._gravity()
        self.player_position_y += self.player_movement_y

        #collisions = pygame.sprite.collide_rect(self.rect, self.level)
        #for o in collisions:
        #    if self.movement_y < 0:
         #       self.rect.top = o.rect.bottom
          #  if self.movement_y > 0:
           #     self.rect.bottom = o.rect.top
        # self.player_movement_y = 0



