import random


class GenerateTree(object):
    def __init__(self, array):
        self.char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.array = array
        self.steps = []
        self.height = self.calculate_height_of_tree()
        self.trees = [[Node(1000, 800, 1400), Node(1400, 1200, 1500), Node(1200, 1111, 1358), Node(1111, 1050, 1199)],
                      [Node(980, 300, 1072), Node(300, 220, 400), Node(400, 371, 700), Node(371, 350, 390)],
                      [Node(1500, 700, 5000), Node(5000, 3500, 5040), Node(3500, 3000, 4071), Node(3000, 2000, 3300),
                       Node(3300, 3100, 3400), Node(3400, 3350, 3450), Node(3350, 3320, 3390), Node(3390, 3372, 3395)],
                      [Node(5000, 4400, 7000), Node(4400, 2000, 4800), Node(2000, 1000, 4000), Node(4000, 3000, 4100),
                       Node(3000, 2500, 2990), Node(2500, 2100, 2400), Node(2400, 2300, 2450), Node(2300, 2240, 2360)],
                      [Node(999, 100, 3000), Node(3000, 1700, 4500), Node(1700, 1000, 1900),
                       Node(1900, 1800, 2000), Node(2000, 1990, 2490), Node(2490, 2200, 2773)],
                      [Node(2000, 1000, 3001), Node(1000, 500, 1150), Node(500, 200, 900),
                       Node(900, 650, 990), Node(650, 630, 800), Node(800, 700, 990)]]
        self.tree = self.generate_tree()

    def calculate_height_of_tree(self):
        return len(self.array)

    def pick_direction(self, nr):
        if nr == 0:
            return "right"
        else:
            if random.randint(0, 1) == 0:
                return "left"
            else:
                return "right"

    def pick_letter(self, letter):
        pick = random.choice(self.char_list)
        while pick == letter:
            pick = random.choice(self.char_list)
        return pick

    def get_avaliable_path(self, len_of_path):
        avaliable_path = []
        for tree in self.trees:
            if len(tree) == len_of_path:
                avaliable_path.append(tree)
        return avaliable_path

    def generate_tree(self):
        len_of_path = len(self.array)
        avaliable_path = self.get_avaliable_path(len_of_path)
        path = random.choice(avaliable_path)
        for num_of_letter, letter in enumerate(self.array):
            path[num_of_letter].root_letter = letter
            self.set_letter(path, num_of_letter, self.array[num_of_letter + 1] if num_of_letter < self.height - 1 else 'X')
        return path

    def set_letter(self, path, pos, letter):
        if pos < self.height - 1:
            if path[pos].left_child == path[pos + 1].root:
                path[pos].left_child_letter = letter
                path[pos].right_child_letter = self.pick_letter(letter)
            elif path[pos].right_child == path[pos + 1].root:
                path[pos].right_child_letter = letter
                path[pos].left_child_letter = self.pick_letter(letter)
        else:
            path[pos].right_child_letter = 'X'
            path[pos].left_child_letter = 'X'

    def print_tree(self):
        for element in self.tree:
            print(
                f"Left: {element.left_child}({element.left_child_letter})\t Center: {element.root}({element.root_letter})\t Right: {element.right_child}({element.right_child_letter})")

    def print_tree_tmp(self, tree):
        for element in tree:
            print(
                f"Left: {element.left_child}({element.left_child_letter})\t Center: {element.root}({element.root_letter})\t Right: {element.right_child}({element.right_child_letter})")


class Node(object):
    def __init__(self, root_val, left_val, right_val):
        self.left_child = left_val
        self.left_child_letter = None
        self.right_child = right_val
        self.right_child_letter = None
        self.root = root_val
        self.root_letter = None
