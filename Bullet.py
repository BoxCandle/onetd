import math
from Effect import *

class Bullet:
    def __init__(self, pos, target, tower):
        self.x, self.y = pos
        self.target = target
        self.speed = tower.projectile_speed
        self.damage = tower.damage
        self.size = tower.bullet_size
        self.image = tower.sprites["bullet_image"]
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-35, -35)
        self.hit_radius = (self.rect.width // 2) + 10
        self.tower = tower


    def update(self, dt):
        dx = self.target.hitbox.centerx - self.x
        dy = self.target.hitbox.centery - self.y
        distance = math.hypot(dx, dy)

        if distance != 0:
            self.x += (dx / distance) * self.speed * dt
            self.y += (dy / distance) * self.speed * dt
            self.rect.center=(self.x, self.y)
            self.hitbox.center = self.rect.center

        if self.hitbox.colliderect(self.target.hitbox):
            self.deal_damage()
            return True
        return False

    def deal_damage(self):
        return self.damage

class FireBullet(Bullet):
    def __init__(self, pos, target, tower):
        super().__init__(pos, target, tower)
        self.image = tower.sprites["bullet_image"]
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-65, -65)
        self.hit_radius = max(self.rect.width, self.rect.height)
        self.target = target

    def update(self, dt):
        hit = super().update(dt)

        if hit:
            self.tower.apply_effect(self.target)
            return True
        return False