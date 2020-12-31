import pygame
import src.MainImages as main_img
from src.PlatformsMainPackage.LifeController import LifeController
from src.PlatformsMainPackage.BulletClass import BulletClass

"""
    Główna klasa gracza, odpowiada za:
    1. poruszanie się gracza
    2. aktualizację obrazków gracza
"""


class Player(pygame.sprite.Sprite):
    def __init__(self, life, start_image, binary_lvl):
        """

        :param life: ilość życia jaką dysponuje gracz na począku rozgrywki
        :type life: int
        :param start_image: obraz gracza, od którego zaczyna się rozgrywka
        :type start_image: pygame img
        """
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
        self.agree_to_jump = False
        self.start_player_position_x = self.rect[0]
        self.start_player_position_y = self.rect[1]
        self.items = set()
        self.set_of_items = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()
        self.binary_lvl = binary_lvl
        self.diference = 0

    def draw(self, board):
        """
        :param board: 'tablica' na której rysuje gracza
        :type board: surface
        :return: None
        """
        board.blit(self.actual_image, self.rect)

    def turn_left(self, speed=main_img.SPEED_X):
        """
        metoda służąca do zmiany kierunku poruszania się gracza - konkretnie zmiana na lewo
        :return: None
        """
        self.direction_of_movement = 'left'
        self.player_movement_x = -1 * speed

    def turn_right(self, speed=main_img.SPEED_X):
        """
        metoda służąca do zmiany kierunku poruszania się gracza - konkretnie zmiana na prawo
        :return: None
        """
        self.direction_of_movement = 'right'
        self.player_movement_x = speed

    def stop(self):
        """
        metoda służąca do zatrzymania gracza, aby się on nie poruszał
        :return: None
        """
        self.player_movement_x = 0
        self.player_movement_y = 0

    def jump(self, movement=-12):
        """
        metoda dzięki której nasz gracz może skakać
        :return: None
        """
        if self.player_movement_y == 0 or self.player_movement_y == (-1 * movement) or self.agree_to_jump is True:
            self.player_movement_y = movement
            self.falling = False

    def _gravity(self):
        """
        metoda, która obsługuje grawitację: dzięki niej po skoku gracz 'opada'
        na platformę pod siebie, bądź też spada poza mapę przez co traci życie
        :return:
        """
        if self.player_movement_y == 0:
            self.player_movement_y = 1
        else:
            self.player_movement_y += 0.35
        if self.player_movement_y > 15:
            self.player_movement_y = 16

    def _move(self, images):
        """
        metoda służąca do podmiany obrazu gracza jaki widzi użytkownik
        :param images: lista z dostępnymi obrazami dla danego kierunku
        :type images: list
        :return: None
        """
        if self.count < 4:
            self.actual_image = images[0]
        if 4 <= self.count < 8:
            self.actual_image = images[1]
        if self.count > 8:
            self.count = 0
        else:
            self.count += 1

    def pick_up(self):
        """
        metoda służąca za akcje podnoszenia "item'ów", takich jak broń.
        :return: None
        """
        for item in self.level.dict_of_items:
            if self.level.dict_of_items[item].rect.center[0] - 20 >= self.rect.left and \
                    self.level.dict_of_items[item].rect.center[0] + 20 <= self.rect.right and \
                    (self.level.dict_of_items[item].rect.top == self.rect.bottom or
                     self.level.dict_of_items[item].rect.top - 35 == self.rect.bottom):
                if item == "potion_max_life":
                    if self.life.player_life < 3:
                        self.level.potion.picked = True
                        self.life.set_life_to_default()
                        self.level.reset_map = self.life.player_life
                elif item == 'tip':
                    self.level.tip.picked = True
                elif item == 'heart':
                    if self.level.heart.picked is False:
                        self.level.heart.picked = True
                        self.life.add_life(1)
                        self.level.reset_map = self.life.player_life

    def shot(self, event):
        """
        metoda odpowiadająca za strzelanie pociskami przez gracza w danym kierunku:
        tworzy obiekt 'BulletClass', który jest naszym pociskiem
        :param event: zbiór eventów wykrytych przez pygame
        :return: None
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.direction_of_movement == 'right':
                    self.set_of_bullets.add(BulletClass(main_img.bullet_right,
                                                        self.direction_of_movement, self.rect.center))
                if self.direction_of_movement == 'left':
                    self.set_of_bullets.add(BulletClass(main_img.bullet_left,
                                                        self.direction_of_movement, self.rect.center))

    def get_event(self, event):
        """
        metoda sterująca zachowaniem gracza: sprawdzanie wciśniętych klawiszy oraz
        wykonanie odpowiednich zadań przypisanych do danego klawisza
        :param event: zbiór wszystkich eventów jakie są dostępne
        :type event: pygame.event
        :return: None
        """

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

    def enemy_collide(self):
        """
        metoda sterująca życiem oraz zachowaniem gracza podczas zderzenia z przeciwnikiem
        :return: None
        """
        for enemy in self.level.enemy:
            if self.rect.center[1] + 55 == enemy.start_y + 110 and (self.rect.right == enemy.rect.right - 50 or
                                                                    self.rect.left == enemy.rect.left - 50):
                self.life.del_life(1)

    def enemy_bullet_collide(self):
        for enemy in self.level.enemy:
            for nr, bullet in enumerate(enemy.set_of_bullet_enemy):
                if self.rect.left <= bullet.rect.center[0] <= self.rect.right and \
                        self.rect.center[1] + 55 == enemy.start_y + 110:
                    self.life.del_life(1)
                    self.rect.y -= 150

    def update_images(self):
        """
        metoda do aktualizowania obrazów, sprawdzania kolizji z platformami etc
        :return: None
        """
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

        if self.binary_lvl is False:
            collisions = pygame.sprite.spritecollide(self, self.level.set_of_transport_platforms, False)
            if collisions:
                self.agree_to_jump = True
            else:
                self.agree_to_jump = False
            for col in collisions:
                if self.player_movement_y < 0:
                    self.rect.top = col.rect.bottom
                if self.player_movement_y > 0:
                    self.rect.bottom = col.rect.top
                if self.rect.right == col.rect.left or self.rect.left == col.rect.right:
                    break

        collisions = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for col in collisions:
            if col.type != 'trap':
                if self.player_movement_y < 0:
                    self.rect.top = col.rect.bottom
                if self.player_movement_y > 0:
                    self.rect.bottom = col.rect.top
                self.player_movement_y = 0
                if self.binary_lvl is True:
                    if col not in self.level.player_answer:
                        self.level.player_answer.append(col)
                        self.level.actual_platform = col
                    if self.level.actual_platform.mode == 'up' and self.level.actual_height_of_lvl < 8:
                        self.level.actual_platform.mode = 'down'
                        self.rect.x = 600
                        self.rect.y = 500
                        self.level.actual_height_of_lvl += 1
                        self.level.generate_platform()

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
        if (self.player_movement_y == 0 and self.player_movement_x == 0) or self.player_movement_y == 16:
            self.falling = False
            if self.direction_of_movement == "left":
                self.actual_image = main_img.stand_left
            else:
                self.actual_image = main_img.stand_right
        if self.rect.center[1] > 2000:
            #tutaj reset mapy do stanu początkowego po spadnięciu gracza poniżej poziomu najniższej platformy
            if self.direction_of_movement == 'left':
                self.actual_image = main_img.fail_left
                self.falling = True
            else:
                self.actual_image = main_img.fail_right
                self.falling = True
            self.rect[0] = self.start_player_position_x
            self.rect[1] = self.start_player_position_y
            self.life.del_life(1)
            self.reset_level()
        if self.binary_lvl is False:
            self.enemy_collide()
            self.enemy_bullet_collide()
            self.pick_up()

    def reset_level(self):
        self.diference = self.start_player_position_x - self.rect[0]
        for enemy in self.level.enemy:
            enemy.rect.x = enemy.start_x - self.diference
