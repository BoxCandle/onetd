import pygame as pg

class Enemy:
    def __init__(self, xp_reward : int, position : tuple, speed : int = 100):
        self.x, self.y = position
        self.speed = speed
        self.alive = True
        self.image = pg.image.load("crow.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.xp_reward = xp_reward
        self.radius = 10

    def kill(self) -> int:
        self.alive = False
        return self.xp_reward

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.image, self.rect)

