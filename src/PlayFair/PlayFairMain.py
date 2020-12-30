import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground
from src.PlayFair.LettersPlayFair import LettersPlayFair
from src.PlayFair.CopyLetters import CopyLetters
from src.PlayFair.AnswerField import AnswerField
from src.PlayFair.CheckButton import CheckButton
from src.PlayFair.CryptoOperationMain import CryptoOperationMain


class PlayFairMain(DrawBackground):
    def __init__(self):
        super().__init__(main_img.playfair_background, 0, 0)
        self.board = self.get_frame()
        self.letters = LettersPlayFair()
        self.answer_field = AnswerField()
        self.button = CheckButton()
        self.crypto = CryptoOperationMain()
        self.active_letter = None
        self.copied_letters = []
        self.answer_letters = []
        self.show_helper = False

    def draw(self):
        self.draw_window()
        self.crypto.draw(self.board)
        self.button.draw(self.board)
        self.answer_field.draw(self.board)
        self.letters.draw(self.board)
        for letter in self.copied_letters:
            letter.draw_copy_letter(self.board)
        if self.show_helper is True:
            self.board.blit(main_img.helper_playfair, (300, 100))

    def generate_answer(self):
        self.answer_letters = []
        for letter in self.copied_letters:
            if self.answer_field.rect.top <= letter.rect.top and self.answer_field.rect.bottom >= letter.rect.bottom \
                    and self.answer_field.rect.left <= letter.rect.left \
                    and self.answer_field.rect.right >= letter.rect.right:
                self.answer_letters.append(letter)

    def check_answer(self):
        tmp = ''
        for x in self.quick_sort(self.answer_letters):
            tmp += x.letter
        if self.crypto.output_text == tmp:
            return True

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        p = arr.pop()
        left = [a for a in arr if a.rect.center[0] < p.rect.center[0]]
        right = [a for a in arr if a.rect.center[0] >= p.rect.center[0]]
        return self.quick_sort(left) + [p] + self.quick_sort(right)

    def run(self):
        while not self.handle_events():
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        return True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.show_helper = True
            elif event.type == pygame.KEYUP:
                self.show_helper = False
            for ltr in self.copied_letters:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.board.blit(ltr.img, (ltr.rect.x, ltr.rect.y)).collidepoint(pygame.mouse.get_pos()):
                            self.active_letter = ltr
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.active_letter = None
            for ltr in self.copied_letters:
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:
                        if self.active_letter == ltr:
                            ltr.rect.center = pygame.mouse.get_pos()
                            ltr.draw_copy_letter(self.board)
            else:
                for letters in self.letters.letters:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_click_pos = pygame.mouse.get_pos()
                            if self.board.blit(self.letters.letters[letters], self.letters.letters_start_pos[letters]).collidepoint(mouse_click_pos):
                                tmp_letter = CopyLetters(letters, self.letters.letters[letters], mouse_click_pos[0], mouse_click_pos[1])
                                self.copied_letters.append(tmp_letter)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.blit(self.button.image, self.button.position).collidepoint(pygame.mouse.get_pos()):
                        self.generate_answer()
                        if self.check_answer() is True:
                            return True
