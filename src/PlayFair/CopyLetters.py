class CopyLetters(object):
    def __init__(self, letter, img, positionX, positionY):
        self.letter = letter
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = positionX
        self.rect.y = positionY

    def update_position(self, position, surface):
        print("xsayd")
        self.rect.center = position
        # self.draw_copy_letter(surface)

    def draw_copy_letter(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))