import pygame
import src.MainImages as main_img
from src.DrawBackground import DrawBackground


class BreakingClass(DrawBackground):
    def __init__(self, img):
        super().__init__(img, -300, -300)
