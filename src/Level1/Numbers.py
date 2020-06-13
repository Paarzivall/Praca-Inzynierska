import pygame
import random
import src.MainImages as main_img


class Numbers(object):
    def __init__(self):
        self.board = pygame.display.get_surface()
        self.numbers = main_img.numbers
        self.positions = {0: (150, 180), 1: (180, 180)}
        self.picked_tuple = ()
        self.list_of_numbers = self.create_list_of_numbers()
        self.picked = self.pick_numbers()
        print(self.picked_tuple)
        self.binary = self.calculate_binary()
        self.draw_numbers()

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
        print(tmp_list)
        tmp_list = tmp_list[::-1]
        if len(tmp_list) < 7:
            if len(tmp_list) < 6:
                if len(tmp_list) < 5:
                    tmp_list.insert(0, 0)
                tmp_list.insert(0, 0)
            tmp_list.insert(0, 0)
        print("tmop")
        print(tmp_list)
        return tmp_list


