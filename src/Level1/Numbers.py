import pygame
import random
from src.ResizeClass import resize


class Numbers(object):
    def __init__(self):
        self.board = pygame.display.get_surface()
        self.numbers = {0: '../../img/Level1/Cyfry/0a.png', 1: '../../img/Level1/Cyfry/1a.png',
                        2: '../../img/Level1/Cyfry/2.png', 3: '../../img/Level1/Cyfry/3.png',
                        4: '../../img/Level1/Cyfry/4.png', 5: '../../img/Level1/Cyfry/5.png',
                        6: '../../img/Level1/Cyfry/6.png', 7: '../../img/Level1/Cyfry/7.png',
                        8: '../../img/Level1/Cyfry/8.png', 9: '../../img/Level1/Cyfry/9.png'}
        self.positions = {0: (150, 180), 1: (180, 180)}
        self.picked_tuple = ()
        self.load_numbers_images()
        self.list_of_numbers = self.create_list_of_numbers()
        self.picked = self.pick_numbers()
        print(self.picked_tuple)
        self.binary = self.calculate_binary()
        self.draw_numbers()

    def load_numbers_images(self):
        for number in self.numbers:
            image = resize(pygame.image.load(self.numbers[number]))
            self.numbers.update({number: image})

    def create_list_of_numbers(self):
        return list(self.numbers.keys())

    def pick_numbers(self):
        first_number = random.choice(self.list_of_numbers[1:])
        second_number = random.choice(self.list_of_numbers)
        self.picked_tuple = (first_number, second_number)
        return first_number * 10 + second_number

    def draw_numbers(self):
        position = 0
        for number in self.picked_tuple:
            for element in self.numbers:
                if number == element:
                    self.board.blit(self.numbers[element], self.positions[position])
            position += 1

    def calculate_binary(self):
        tmp = self.picked
        tmp_list = []
        while tmp > 0:
            if tmp % 2 == 0:
                tmp_list.append(0)
            else:
                tmp_list.append(1)
            tmp = int(tmp / 2)
        return self.add_optional_element(tmp_list)

    @staticmethod
    def add_optional_element(tmp_list):
        tmp_list = tmp_list[::-1]
        if len(tmp_list) < 7:
            tmp_list.insert(0, 0)
        return tmp_list


