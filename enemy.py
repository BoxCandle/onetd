import pygame as pg
import math

class Enemy:
    def __init__(self, xp_reward : int, position : tuple, speed : int = 100, health : int = 20):
        self.x, self.y = position
        self.speed = speed
        self.alive = True
        self.xp_reward = xp_reward
        self.radius = 10
        self.sprites = [pg.transform.scale(pg.image.load(f"Zombie/Zombie_walk/Zombie_Walk{i}.png").convert_alpha(), (70, 70))
                        for i in range(1, 11)]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.inflate_ip(-25 , 0)
        self.health = health

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

        self.rect.inflate_ip(-25, 0)

    def target(self, window_center, dt):
        center_x, center_y = window_center

        direction_x = center_x - self.x
        direction_y = center_y - self.y

        distance = math.hypot(direction_x, direction_y)

        direction_x /= distance
        direction_y /= distance

        self.x += direction_x * self.speed * dt
        self.y += direction_y * self.speed * dt

        self.rect.center = (self.x, self.y)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def kill(self) -> int:
        self.alive = False
        return self.xp_reward

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.image, self.rect)
        #pg.draw.rect(surface,"Red", self.rect, 3) #enemy hitbox
    #ADD HEALTHBARS
