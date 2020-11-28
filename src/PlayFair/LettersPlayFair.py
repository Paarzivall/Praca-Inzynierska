import src.MainImages as main_img


class LettersPlayFair(object):
    def __init__(self):
        self.letters = main_img.letters
        self.letters_start_pos = {'A': (908, 8), 'B': (980, 8), 'C': (1053, 8), 'D': (1127, 8), 'E': (1200, 8),
                                  'F': (908, 80), 'G': (980, 80), 'H': (1053, 80), 'I': (1127, 80), 'K': (1200, 80),
                                  'L': (908, 153), 'M': (980, 153), 'N': (1053, 153), 'O': (1127, 153), 'P': (1200, 153),
                                  'Q': (908, 227), 'R': (980, 227), 'S': (1053, 227), 'T': (1127, 227), 'U': (1200, 227),
                                  'V': (908, 300), 'W': (980, 300), 'X': (1053, 300), 'Y': (1127, 300), 'Z': (1200, 300)}

    def draw(self, surface):
        for letter in self.letters:
            surface.blit(self.letters[letter], self.letters_start_pos[letter])
