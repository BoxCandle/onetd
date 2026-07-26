import pygame
import math

class Tower:

    def __init__(self, data, pos):
        self.damage = data["damage"]
        self.range = data["range"]
        self.reload = data["reload"]
        self.sprites = data["sprites"]
        self.pos = pos
        self.rect = self.sprites["up"].get_rect()
        self.rect.center = pos
        self.last_shot = 0
        self.image = self.sprites["up"]
        self.cost = data["cost"]
        self.isActive = False

    def copy(self):

        new_tower = Tower(
            {
                "damage": self.damage,
                "range": self.range,
                "reload": self.reload,
                "sprites": self.sprites,
                "cost": self.cost

            },
            self.rect.center
        )
        return new_tower

    def enemy_in_range(self, enemy):
        now = pygame.time.get_ticks()

        dx = self.rect.centerx - enemy.rect.centerx
        dy = self.rect.centery - enemy.rect.centery
        distance = math.hypot(dx, dy)

        if distance < self.range and now - self.last_shot > self.reload:
            self.last_shot = now
            return True

        return False

    def show_range(self):
        return self.range

    def turn_cannon(self, enemy_pos):
        enemy_x, enemy_y = enemy_pos

        if enemy_x < self.rect.centerx:
            self.image = self.sprites["left"]
        if enemy_x > self.rect.centerx:
            self.image = self.sprites["right"]
        if enemy_y < self.rect.centery and self.rect.centerx - 30 <= enemy_x <= self.rect.centerx + 30:
            self.image = self.sprites["up"]
        if enemy_y > self.rect.centery and self.rect.centerx - 30 <= enemy_x <= self.rect.centerx + 30:
            self.image = self.sprites["down"]