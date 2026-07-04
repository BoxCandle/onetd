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

                if self._distance(bullet, enemy) < bullet.radius + enemy.radius:
                    enemy.kill()
                    bullet.hit_enemy()
                    self.bullets.remove(bullet)
                    break


    def _distance(self,a, b):
        return math.hypot(a.x - b.x, a.y - b.y)
