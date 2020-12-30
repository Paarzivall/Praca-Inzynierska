import src.MainImages as main_img


class SwitchingButtons(object):
    def __init__(self, number_of_buttons):
        self.number_of_buttons = number_of_buttons
        self.button_positions = {0: (315, 255), 1: (510, 255), 2: (705, 255), 3: (900, 255)}
        self.next_button = main_img.next_button
        self.next_button_pos = {0: (315, 355), 1: (510, 355), 2: (705, 355), 3: (900, 355)}
        self.active_button = 0
        self.lock = main_img.lock
        self.lock_pos = (540, 500)
        self.buttons = {}
        self.buttons_light = main_img.switch_button_light
        self.add_buttons()

    def add_buttons(self):
        for count in range(self.number_of_buttons):
            self.buttons.update({count: main_img.switch_button})

    def draw(self, surface):
        surface.blit(self.lock, self.lock_pos)
        for count, button in enumerate(self.buttons):
            if count == self.active_button:
                surface.blit(self.buttons_light, self.button_positions[count])
                surface.blit(self.next_button, self.next_button_pos[count])
            else:
                surface.blit(self.buttons[button], self.button_positions[count])