import random
import pygame
import src.MainImages as main_img


class CryptoOperationMain(object):
    def __init__(self):
        pygame.font.init()
        self.char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.word_list = ['RAGNAR', 'WALHALLA', 'ODYN', 'THOR']
        self.char_position = [(70, 400), (120, 400), (170, 400), (220, 400), (270, 400),
                              (70, 460), (120, 460), (170, 460), (220, 460), (270, 460),
                              (70, 510), (120, 510), (170, 510), (220, 510), (270, 510),
                              (70, 560), (120, 560), (170, 560), (220, 560), (270, 560),
                              (70, 620), (120, 620), (170, 620), (220, 620), (270, 620)]
        self.picked_word = self.pick_word()
        self.key = self.pick_word()
        self.table = self.generate_table()
        self.output_text = self.coding()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        print(self.output_text)

    def pick_word(self):
        return random.choice(self.word_list)

    def generate_table(self):
        table = [[0] * 5 for i in range(5)]
        tmp = ""
        x = 0
        y = 0
        for letter in self.key:
            if tmp.find(letter) == -1:
                tmp += letter
                table[x][y] = letter
                y += 1
                if y == 5:
                    x += 1
                    y = 0
        for letter in self.char_list:
            if tmp.find(letter) == -1:
                tmp += letter
                table[x][y] = letter
                y += 1
                if y == 5:
                    x += 1
                    y = 0
        return table

    def find_letter(self, letter):
        for i in range(5):
            for j in range(5):
                if self.table[i][j] == letter:
                    return Position(i, j)
        return None

    def coding(self):
        text = ""
        for x in range(0, len(self.picked_word), 2):
            first_letter = self.find_letter(self.picked_word[x])
            second_letter = self.find_letter(self.picked_word[x + 1])
            if first_letter is None or second_letter is None:
                return
            elif first_letter.x == second_letter.x:
                text += self.table[first_letter.x][(first_letter.y + 1) % 5]
                text += self.table[second_letter.x][(second_letter.y + 1) % 5]
            elif first_letter.y == second_letter.y:
                text += self.table[(first_letter.x + 1) % 5][first_letter.y]
                text += self.table[(second_letter.x + 1) % 5][second_letter.y]
            else:
                text += self.table[first_letter.x][second_letter.y]
                text += self.table[second_letter.x][first_letter.y]
        return text

    def draw(self, surface):
        surface.blit(self.font.render(self.picked_word, False, (0, 0, 0)), (930, 550))
        surface.blit(main_img.table, (50, 400))
        counter = 0
        for x in self.table:
            for y in x:
                surface.blit(self.font.render(y, False, (0, 0, 0)), self.char_position[counter])
                if counter < 24:
                    counter += 1
                else:
                    counter = 0


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
