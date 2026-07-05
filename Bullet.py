import math
import pygame as pg
pg.init()
pg.mixer.init()
shoot_sound = pg.mixer.Sound("Shootsound.wav")

class Bullet:

    def __init__(self, position, speed : int = 50, damage = 1):
        self.x, self.y = position
        self.speed = speed
        self.alive = True
        self.rect = pg.Rect(self.x, self.y, 5, 5)
        self.radius = 5
        self.image = pg.image.load("bullet.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.damage = damage

    def update(self, dt, target_position):
        target_x, target_y = target_position

        direction_x = target_x - self.x
        direction_y = target_y - self.y
        distance = math.hypot(direction_x, direction_y)

        direction_x /= distance
        direction_y /= distance

        self.x += direction_x * self.speed * dt
        self.y += direction_y * self.speed * dt
        self.rect.center = (self.x, self.y)

    def hit_enemy(self):
        self.alive = False
        return self.damage

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)
        #pg.draw.rect(surface, "Red", (self.x, self.y, 30, 30), 3)    #bullet hitbox

