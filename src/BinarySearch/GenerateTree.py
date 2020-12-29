import random


class GenerateTree(object):
    def __init__(self, array):
        self.char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.array = self.qsort(array)
        self.height = self.calculate_height_of_tree()
        self.tree = self.generate_tree()

    def calculate_height_of_tree(self):
        return len(self.array)

    def qsort(self, arr):
        if len(arr) <= 1: return arr
        p = arr.pop()
        left = [a for a in arr if a < p]
        right = [a for a in arr if a >= p]
        return self.qsort(left) + [p] + self.qsort(right)

    def generate_tree(self):
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
        return tree

    def generate_letter(self, root):
        if root == 'A':
            return 'A'
        else:
            return random.choice(self.char_list[:self.char_list.index(root)])

    def check_position(self, root, child):
        if root > child:
            return 'left'
        else:
            return 'right'

    def print_tree(self):
        for element in self.tree:
            print(f"Left: {element.left_child}\t Center: {element.root}\t Right: {element.right_child}")


class Node(object):
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.root = value

"""
if __name__ == '__main__':
    arr = ['A', 'D', 'O', 'E', 'G', 'K', 'K', 'G']
    tmp = GenerateTree(arr)
    print(tmp.array)
    tmp.print_tree()"""
