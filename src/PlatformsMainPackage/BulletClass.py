import pygame


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, bullet_image, direction, rect_center):
        super().__init__()
        self.bullet_image = bullet_image
        self.bullet_direction = direction
        self.rect = self.bullet_image.get_rect()
        self.rect.center = rect_center

    def draw(self, board):
        board.blit(self.bullet_image, self.rect)

    def update_bullet(self):
        if self.bullet_direction == 'right':
            self.rect.x += 15
        if self.bullet_direction == 'left':
            self.rect.x -= 15
