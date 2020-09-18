import pygame
from sys import exit
from src.DrawBackground import DrawBackground
from src.PlatformsMainPackage.Player import Player
from src.PlatformsMainPackage.LifeController import LifeController
from src.PlatformsMainPackage.EnemyClass import EnemyClass
from src.PlatformsMainPackage.MainItem import MainItem
from src.PlatformsMainPackage.TransportPlatforms import TransportPlatforms
from  src.PlatformsMainPackage.MapStaticElements import MapStaticElements
import src.MainImages as main_img

"""
Główna klasa leveli platformowych. Działa jako łącznik do wszystkich klas wykorzystywanych w tego typu levelach.
Odpowiada za tworzenie poziomów jak również za wszystkie akcje wykonywane na niej. Tutaj znajdują się główne
metody zarządzające całą rozgrywką na "platformach"
"""


class BaseLevelPlatform(DrawBackground):
    def __init__(self, background, player=Player):
        """

        :param background: obraz tła dla danego levelu
        :type background: pygame img
        :param player: obiekt gracza
        :type player: src.PlatformsMainPackage.Player
        """
        super().__init__(background, -300, -300)
        self.b_x = self.b_y = -300
        self.board = self.get_frame()
        self.player = player
        self.set_of_platforms = set()
        self.set_of_enemies = set()
        self.set_of_transport_platforms = set()
        self.life = LifeController.get_instance()
        self.reset_map = self.life.player_life
        self.min_y = 0
        self.enemy = set()
        self.gun = None
        self.items()
        self.finish_platform = None
        self.portal = None
        self.is_done = False

    def items(self):
        """
        metoda tworząca item (broń gracza) na planszy
        :return: None
        """
        self.gun = MainItem(main_img.gun, "GUN")
        self.gun.rect.x = 600
        self.gun.rect.y = 600
        self.player.set_of_items.add(self.gun)

    def generate_portal(self):
        number_of_platform = len(self.set_of_platforms)
        print(number_of_platform)
        tmp_platform = list(self.set_of_platforms)
        last_platform = tmp_platform[number_of_platform - 1]
        print(last_platform.rect)
        self.portal = MapStaticElements(main_img.portal, last_platform.rect[0], last_platform.rect[1],
                                        last_platform.rect[2], last_platform.rect[3])

    def generate_enemies_on_platforms(self, platform, life):
        """
        metoda dzięki której generowani są przeciwnicy na danej planszy
        :param platform: platforma na której ma się znajdować przeciwnik
        :type platform: src.PlatformsMainPackage.Platforms
        :param life: ilość życia danego przeciwnika
        :type life: int
        :return:
        """
        self.enemy.add(EnemyClass(main_img.enemy_stand_right, life, platform))

    def calculate_min_y_of_platforms(self, list_of_platforms):
        """
        metoda pomocnicza dzięki której wyliczana jest wysokość poniżej której gracz traci życie, to znaczy:
        wyszukiwana jest najniżej położona platforma; jeżeli obiekt gracza znajdzie się poniżej jej, gracz traci życie
        :param list_of_platforms: lista platform dostępnych dla danego levelu
        :type list_of_platforms: list
        :return: None
        """
        self.min_y = list_of_platforms[0][3]
        for platform in list_of_platforms:
            if platform[3] > self.min_y:
                self.min_y = platform[3]
        self.player.min_y = self.min_y

    def kill_enemy(self):
        """
        metoda służąca "uśmiercaniu przeciwników": jeżeli nastąpi kolizja pocisku z hitboxem przeciwnika, to przeciwnik
        traci życie
        :return: None
        """
        for enemy in self.enemy:
            for bullet in self.player.set_of_bullets:
                if (bullet.rect.center[1] + 55 >= enemy.start_y + 30) and \
                        (bullet.rect.center[1] + 55 <= enemy.start_y + 130) and \
                        (bullet.rect.center[0] <= enemy.start_x - 10 or bullet.rect.center[0] >= enemy.start_x + 10):
                    if enemy.life > 0:
                        enemy.life -= 1
                    else:
                        enemy.life = 0

    def _destroy_bullet(self):
        """
        metoda służąca do niszczenia pocisków po wykryciu kolizji z platformą bądż przeciwnikiem
        :return: None
        """
        for bullet in self.player.set_of_bullets:
            for platform in self.set_of_platforms:
                if platform.rect.colliderect(bullet):
                    self.player.set_of_bullets.remove(bullet)
            if main_img.WIDTH < bullet.rect.x:
                self.player.set_of_bullets.remove(bullet)

    def is_finish(self):
        """
        metoda sprawdzająca kolizje gracza z ostatnią platformą, która jest punktem zakończenia danego levelu
        :return: None
        """
        if (self.player.rect.right >= self.portal.rect.left and self.player.rect.left <= self.portal.rect.right) and \
                (self.player.rect.top <= self.portal.rect.bottom and self.player.rect.bottom >= self.portal.rect.top):
            print("koniec " + str(self.is_done))
            self.is_done = True

    def update(self):
        """
        metoda update'ująca poszczególne komponenty danego levelu, takie jak:
        1. platformy;
        2. przeciwnicy
        3. pociski
        4. item'y
        :return: None
        """
        for simple_p in self.set_of_platforms:
            simple_p.update()
        for enemy in self.enemy:
            enemy.enemy_update()
        for bullet in self.player.set_of_bullets:
            bullet.update_bullet()
        for transport in self.set_of_transport_platforms:
            transport.update_transport_platform()
        self.gun.update_item(self.player.rect.center)
        self.kill_enemy()
        self._destroy_bullet()
        self.is_finish()

    def draw(self):
        """
        metoda służąca do rysowania na ekranie poszczególnych elementów składowych danego levelu
        :return: None
        """
        self.draw_window()
        for simple_p in self.set_of_platforms:
            simple_p.draw(self.board)
        for enemy in self.enemy:
            enemy.draw_enemy(self.board)
        for bullet in self.player.set_of_bullets:
            bullet.draw(self.board)
        for transport in self.set_of_transport_platforms:
            transport.set_direction()
            transport.draw(self.board)
        self.portal.draw(self.board)
        self.player.draw(self.board)
        self.player.update_images()
        self.life.draw_player_life(self.board)
        self.gun.draw_item(self.board)

    def run(self):
        """
        metoda dzięki której dany level się update'uje: służy jako kontroler levelu
        :return: None
        """
        while not self.handle_events() and self.life.is_life() is True:
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(40)

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
                if event.key == pygame.K_TAB:
                    print("HELPER")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.add_y_position(2)
                    self.move_platform('up')
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
            self.move_platform('left')
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and tmp_player_position_x != self.player.rect.x:
            self.add_x_position(-1 * main_img.SPEED_BACKGROUND_X)
            self.move_platform('right')
        if keys[pygame.K_w] or keys[pygame.K_UP] and tmp_player_position_y != self.player.rect.y:
            self.add_y_position(main_img.SPEED_BACKGROUND_Y * 2)
            self.move_platform('up')
        if self.player.falling:
            self.add_y_position(-1 * main_img.SPEED_BACKGROUND_Y)
            self.move_platform('down')
        if self.reset_map != self.life.player_life:
            self.reset_map = self.life.player_life
            for simple_p in self.set_of_platforms:
                simple_p.set_to_start_position()
            for transport in self.set_of_transport_platforms:
                transport.set_to_start_position()
            self.set_to_start_position(self.b_x, self.b_y)

    def move_platform(self, direction):
        """
        metoda dzięki której platformy poruszają się adekwatnie do ruchu gracza, oraz portali
        :param direction: kierunek poruszania się platform [góra/dół/lewo/prawo]
        :type direction: string
        :return: None
        """
        if direction == 'right':
            for simple_p in self.set_of_platforms:
                simple_p.move_platform_x(-1 * main_img.SPEED_PLATFORM_X)
            for enemy in self.enemy:
                enemy.move_enemy(-1 * main_img.SPEED_PLATFORM_X)
            for transport in self.set_of_transport_platforms:
                transport.move_platform_x(-1 * main_img.SPEED_PLATFORM_X)
            self.portal.move_element(-1 * main_img.SPEED_PLATFORM_X)
        if direction == 'left':
            for simple_p in self.set_of_platforms:
                simple_p.move_platform_x(main_img.SPEED_PLATFORM_X)
            for enemy in self.enemy:
                enemy.move_enemy(main_img.SPEED_PLATFORM_X)
            for transport in self.set_of_transport_platforms:
                transport.move_platform_x(main_img.SPEED_PLATFORM_X)
            self.portal.move_element(main_img.SPEED_PLATFORM_X)
        if direction == 'up':
            for simple_p in self.set_of_platforms:
                simple_p.move_platform_y(main_img.SPEED_PLATFORM_Y * 2)
        if direction == 'down':
            for simple_p in self.set_of_platforms:
                simple_p.move_platform_y(-0.05 * main_img.SPEED_PLATFORM_Y)



