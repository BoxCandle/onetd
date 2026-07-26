import pygame
import math

class Bullet:
    IMAGE = pygame.transform.scale(pygame.image.load("assets/Tower/bullet.png"), (40,40))

    def __init__(self, pos, target, speed = 200, damage = 10, effect = None):
        self.x, self.y = pos
        self.target = target
        self.speed = speed
        self.damage = damage
        self.effect = effect
        self.image = self.IMAGE
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        dx = self.target.rect.centerx - self.x
        dy = self.target.rect.centery - self.y
        distance = math.hypot(dx, dy)

        if distance < 5: return self.deal_damage()

        if distance != 0:
            self.x += (dx / distance) * self.speed * dt
            self.y += (dy / distance) * self.speed * dt
            self.rect.center=(self.x, self.y)
        return None

    def deal_damage(self):
        return self.damage
