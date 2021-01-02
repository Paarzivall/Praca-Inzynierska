import random


class GenerateTree(object):
    def __init__(self, array):
        self.char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.array = array
        self.height = self.calculate_height_of_tree()
        self.tree = self.generate_tree()

    def calculate_height_of_tree(self):
        return len(self.array)

    def pick_direction(self):
        if random.randint(0, 1) == 0:
            return "left"
        else:
            return "right"

    def pick_letter(self, letter):
        pick = random.choice(self.char_list)
        while pick == letter:
            pick = random.choice(self.char_list)
        return pick

    def generate_tree(self):
        output_array = []
        root = Node(random.randint(100, 1000))
        for num_of_letter, letter in enumerate(self.array):
            if num_of_letter < self.height - 1:
                if self.pick_direction() == 'right':
                    root.right_child = random.randint(root.root, 2000)
                    root.left_child = self.cos(output_array, num_of_letter)
                    root.root_letter = letter
                    root.right_child_letter = self.array[num_of_letter + 1]
                    root.left_child_letter = self.pick_letter(self.array[num_of_letter])
                    output_array.append(root)
                    root = Node(root.right_child)
                else:
                    root.right_child = random.randint(root.root, 2000)
                    root.left_child = self.cos(output_array, num_of_letter)
                    root.root_letter = letter
                    root.left_child_letter = self.array[num_of_letter + 1]
                    root.right_child_letter = self.pick_letter(self.array[num_of_letter])
                    output_array.append(root)
                    root = Node(root.right_child)
            else:
                root = Node(random.randint(root.root, 2000))
                root.root_letter = letter
                root.right_child_letter = letter
                root.left_child_letter = letter
                output_array.append(root)
        return output_array

    def cos(self, array, nr):
        if len(array) == 0:
            return 0
        else:
            return random.randint(array[nr - 2].root, array[nr - 1].root)

    """def generate_tree(self):
        print(self.array)
        tree = []
        for num_of_letter, letter in enumerate(self.array):
            if num_of_letter < self.height - 1:
                root = Node(letter)
                next_letter = self.array[num_of_letter + 1]
                check = self.check_position(letter, next_letter)
                if check == 'left':
                    root.left_child = next_letter
                    root.right_child = self.generate_letter(letter)
                else:
                    root.right_child = next_letter
                    root.left_child = self.generate_letter(letter)
            else:
                root = Node(letter)
            tree.append(root)
        return tree"""


    def print_tree(self):
        for element in self.tree:
            print(
                f"Left: {element.left_child}({element.left_child_letter})\t Center: {element.root}({element.root_letter})\t Right: {element.right_child}({element.right_child_letter})")


class Node(object):
    def __init__(self, value):
        self.left_child = None
        self.left_child_letter = None
        self.right_child = None
        self.right_child_letter = None
        self.root = value
        self.root_letter = None


