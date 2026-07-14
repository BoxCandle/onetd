import pygame
import math

class Tower:
    IMAGE = pygame.transform.scale(pygame.image.load("assets/Tower/Tower.png"), (150, 150))

    def __init__(self, pos):
        self.image = Tower.IMAGE
        self.health = 100
        self.range = 200
        self.rect = self.image.get_rect(center=pos)
        self.reload = 200
        self.last_shot = 0
        self.level = 1

    def enemy_in_range(self, enemy):
        now = pygame.time.get_ticks()

        dx = self.rect.centerx - enemy.rect.centerx
        dy = self.rect.centery - enemy.rect.centery
        distance = math.hypot(dx, dy)

        if distance < self.range and now - self.last_shot > self.reload:
            self.last_shot = now
            return True

        return False
