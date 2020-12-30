import src.MainImages as main_img
import random


class SwitchingNumbers(object):
    def __init__(self):
        self.position = {0: (195, 220), 1: (385, 220), 2: (575, 220), 3: (770, 220), 4: (960, 220)}
        self.pairs = {0: (0, 1), 1: (1, 2), 2: (2, 3), 3: (3, 4)}
        self.numbers = main_img.numbers_image
        self.list_of_numbers = self.create_list_of_numbers()
        self.picked_numbers = self.pick_numbers()
        self.sorted_picked_numbers = self.picked_numbers.copy()
        self.sorted()

    def create_list_of_numbers(self):
        return list(self.numbers.keys())

    def pick_numbers(self):
        tmp = []
        while len(tmp) < 5:
            tmp_number = random.choice(self.list_of_numbers)
            if tmp_number not in tmp:
                tmp.append(tmp_number)
        return tmp

    def sorted(self):
        """
            Metoda w której zaimplementowane jest sortowanie bąbelkowe
        """
        for x in range(len(self.sorted_picked_numbers) - 1, 0, -1):
            for i in range(x):
                if self.sorted_picked_numbers[i] > self.sorted_picked_numbers[i + 1]:
                    temp = self.sorted_picked_numbers[i]
                    self.sorted_picked_numbers[i] = self.sorted_picked_numbers[i + 1]
                    self.sorted_picked_numbers[i + 1] = temp

    def draw(self, surface):
        for count, number in enumerate(self.picked_numbers):
            surface.blit(self.numbers[number], self.position[count])

    def switch_positions(self, number_of_position):
        for element in self.picked_numbers:
            tmp = self.picked_numbers[self.pairs[number_of_position][0]]
            self.picked_numbers[self.pairs[number_of_position][0]] = self.picked_numbers[self.pairs[number_of_position][1]]
            self.picked_numbers[self.pairs[number_of_position][1]] = tmp

    def is_finish(self):
        if self.picked_numbers == self.sorted_picked_numbers:
            return True
        else:
            return False
