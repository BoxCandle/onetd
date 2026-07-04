import math

class Collision:
    def __init__(self, bullets, enemies):
        self.bullets = bullets
        self.enemies = enemies

    def update(self):
        self._bullet_enemy_collisions()

    def _bullet_enemy_collisions(self):
        for bullet in self.bullets:
            if not bullet.alive:
                continue

            for enemy in self.enemies:
                if not enemy.alive:
                    continue

                if bullet.rect.colliderect(enemy.rect):
                    bullet.hit_enemy()
                    enemy.take_damage(bullet.hit_enemy())
                    self.bullets.remove(bullet)
                    break

