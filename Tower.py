from Cannons import cannons
from Bullet import *

class Cannon:

    def __init__(self, tower_type, pos):
        if isinstance(tower_type, dict):
            data = tower_type
            self.name = data.get("name", "Cannon")
        else:
            data = cannons[tower_type]
            self.name = tower_type

        self.type = data
        self.damage = data["damage"]
        self.range = data["range"]
        self.reload = data["reload"]
        self.sprites = data["sprites"]
        self.cost = data["cost"]
        self.projectile_speed = data["projectile_speed"]
        self.bullet_size = data["bullet_size"]

        #positioning
        self.pos = pos
        self.rect = self.sprites["up"].get_rect()
        self.rect.center = pos
        self.last_shot = 0
        self.image = self.sprites["up"]
        self.isActive = False

    def copy(self):
        if isinstance(self, FireCannon):
            return FireCannon(self.rect.center)

        return Cannon(
            {
                "name": self.name,
                "damage": self.damage,
                "range": self.range,
                "reload": self.reload,
                "sprites": self.sprites,
                "projectile_speed": self.projectile_speed,
                "bullet_size": self.bullet_size,
                "cost": self.cost
            },
            self.rect.center
        )

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

    def spawn_bullet(self, enemy):
        return Bullet(self.rect.center, enemy, self)

class BasicCannon(Cannon):
    def __init__(self, pos):
        super().__init__("Cannon", pos)

class SniperCannon(Cannon):
    def __init__(self, pos):
        super().__init__("SniperCannon", pos)

class FireCannon(Cannon):
    def __init__(self, pos):
        super().__init__("FireCannon", pos)
        self.fire_dps = 3
        self.fire_duration = 3

    def turn_cannon(self, enemy_pos):
        pass

    def enemy_in_range(self, enemy):
        now = pygame.time.get_ticks()

        dx = self.rect.centerx - enemy.rect.centerx
        dy = self.rect.centery - enemy.rect.centery
        distance = math.hypot(dx, dy)

        if distance < self.range and now - self.last_shot > self.reload:
            self.last_shot = now
            return True

        return False


    def spawn_bullet(self, enemy):
        return FireBullet(self.rect.center, enemy, self)

    def apply_effect(self, enemy):
        effect = FireEffect(self.fire_duration, self.fire_dps)
        enemy.add_effect(effect)
        enemy.set_color_overlay(effect.color_overlay)


