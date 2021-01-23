import pygame


def resize(img, scale=1.5):
    """
        metoda sluzaca to zmiany rozdzielczosci obrazow z 1920x1280 do 1280x720
    """
    size = img.get_size()
    size = int(size[0] / scale), int(size[1] / scale)
    img = pygame.transform.scale(img, size)
    return img
