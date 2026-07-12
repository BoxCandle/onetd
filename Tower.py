import pygame

class Tower:
    IMAGE = pygame.transform.scale(pygame.image.load("assets/Tower/Tower.png"), (150, 150))

    def __init__(self, pos):
        self.image = Tower.IMAGE
        self.health = 100
        self.range = 50
        self.rect = self.image.get_rect(center=pos)

    def take_damage(self, damage : int):
        self.health -= damage