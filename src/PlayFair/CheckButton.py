import src.MainImages as main_img


class CheckButton(object):
    def __init__(self):
        self.image = main_img.try_open_button
        self.position = (500, 500)

    def draw(self, surface):
        surface.blit(self.image, self.position)