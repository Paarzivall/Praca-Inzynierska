import pygame


def resize(img):
    """
        metoda sluzaca to zmiany rozdzielczosci obrazow z 1920x1280 do 1280x720
    """
    size = img.get_size()
    size = int(size[0] / 1.5), int(size[1] / 1.5)
    img = pygame.transform.scale(img, size)
    return img
