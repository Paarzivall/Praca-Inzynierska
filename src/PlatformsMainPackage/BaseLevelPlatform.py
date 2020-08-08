import pygame
from sys import exit
import os
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.LifeController import LifeController
from src.PlatformsMainPackage.EnemyClass import EnemyClass
from src.PlatformsMainPackage.MainItem import MainItem
import src.MainImages as main_img


os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()


class BaseLevelPlatform(DrawBackground):
    def __init__(self, background, player=Player):
        super().__init__(background, -300, -300)
        self.b_x = self.b_y = -300
        self.board = self.get_frame()
        self.player = player
        self.set_of_platforms = set()
        self.set_of_enemies = set()
        self.life = LifeController.get_instance()
        self.reset_map = self.life.player_life
        self.min_y = 0
        self.enemy = set()
        self.items()

    def items(self):
        gun = MainItem(main_img.gun, "GUN")
        gun.rect.x = 600
        gun.rect.y = 600
        self.player.set_of_items.add(gun)

    def generate_enemies_on_platforms(self, platform):
        self.enemy.add(EnemyClass(main_img.enemy_stand_right, 1, platform))

    def calculate_min_y_of_platforms(self, list_of_platforms):
        self.min_y = list_of_platforms[0][3]
        for platform in list_of_platforms:
            if platform[3] > self.min_y:
                self.min_y = platform[3]
        self.player.min_y = self.min_y

    def kill_enemy(self):
        for enemy in self.enemy:
            for bullet in self.player.set_of_bullets:
                if bullet.rect.center[1] + 55 == enemy.start_y + 110:
                    enemy.life -= 1
                    # self.player.set_of_bullets.remove(bullet)

    def _destroy_bullet(self):
        for bullet in self.player.set_of_bullets:
            for platform in self.set_of_platforms:
                if platform.rect.colliderect(bullet):
                    self.player.set_of_bullets.remove(bullet)
            if main_img.WIDTH < bullet.rect.x:
                self.player.set_of_bullets.remove(bullet)

    def update(self):
        for simple_p in self.set_of_platforms:
            simple_p.update()
        for enemy in self.enemy:
            enemy.enemy_update()
        for bullet in self.player.set_of_bullets:
            bullet.update_bullet()
        for item in self.player.set_of_items:
            item.update_item(self.player.rect.center)
        self.kill_enemy()

    def draw(self):
        self.draw_window()
        for simple_p in self.set_of_platforms:
            simple_p.draw(self.board)
        for enemy in self.enemy:
            enemy.draw_enemy(self.board)
        for bullet in self.player.set_of_bullets:
            bullet.draw(self.board)
        self.player.draw(self.board)
        self.player.update_images()
        self.life.draw_player_life(self.board)
        for item in self.player.set_of_items:
            item.draw_item(self.board)

    def run(self):
        while not self.handle_events() and self.life.is_life() is True:
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(40)

    def handle_events(self):
        # Metoda pozwalająca zamknąć okienko
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    print("HELPER")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.add_y_position(2)
                    self.move_platform('y', 'up')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.add_y_position(-1)
            self.player.get_event(event)
            self.player.shot(event)

        tmp_player_position_x = self.player.rect.x
        tmp_player_position_y = self.player.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and tmp_player_position_x != self.player.rect.x:
            self.add_x_position(main_img.SPEED_BACKGROUND_X)
            self.move_platform('x', 'left')
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and tmp_player_position_x != self.player.rect.x:
            self.add_x_position(-1 * main_img.SPEED_BACKGROUND_X)
            self.move_platform('x', 'right')
        if keys[pygame.K_w] or keys[pygame.K_UP] and tmp_player_position_y != self.player.rect.y:
            self.add_y_position(main_img.SPEED_BACKGROUND_Y * 2)
            self.move_platform('y', 'up')
        if self.player.falling:
            self.add_y_position(-1 * main_img.SPEED_BACKGROUND_Y)
            self.move_platform('y', 'down')
        if self.reset_map != self.life.player_life:
            self.reset_map = self.life.player_life
            for simple_p in self.set_of_platforms:
                simple_p.set_to_start_position()
            self.set_to_start_position(self.b_x, self.b_y)

    def move_platform(self, typ, direction):
        if typ == 'x':
            if direction == 'right':
                for simple_p in self.set_of_platforms:
                    simple_p.move_platform_x(-1 * main_img.SPEED_PLATFORM_X)
                for enemy in self.enemy:
                    enemy.move_enemy(-1 * main_img.SPEED_PLATFORM_X)
            if direction == 'left':
                for simple_p in self.set_of_platforms:
                    simple_p.move_platform_x(main_img.SPEED_PLATFORM_X)
                for enemy in self.enemy:
                    enemy.move_enemy(main_img.SPEED_PLATFORM_X)
        elif typ == 'y':
            if direction == 'up':
                for simple_p in self.set_of_platforms:
                    simple_p.move_platform_y(main_img.SPEED_PLATFORM_Y * 2)
            if direction == 'down':
                for simple_p in self.set_of_platforms:
                    simple_p.move_platform_y(-0.05 * main_img.SPEED_PLATFORM_Y)



