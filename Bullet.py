import math
import pygame as pg
pg.init()
pg.mixer.init()
shoot_sound = pg.mixer.Sound("Shootsound.wav")

class Bullet:

    def __init__(self, position, speed : int = 50):
        self.x, self.y = position
        self.speed = speed
        self.alive = True
        self.rect = pg.Rect(self.x, self.y, 5, 5)
        self.radius = 5

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
        shoot_sound.play()
        self.alive = False

    def draw(self, surface: pg.Surface, color: tuple, radius: int):
        pg.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)

