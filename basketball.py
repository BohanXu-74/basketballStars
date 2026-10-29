import pygame

class Basketball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pygame.image.load("basketball.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vx = 0
        self.vy = 0

    def update(self):
        