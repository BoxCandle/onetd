import pygame as pg

class Tower:
    def __init__(self, position : tuple,):
        self.x, self.y = position
        self.image = pg.image.load("scarecrow.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.level = 1
        self.xp = 0

    def on_enemy_killed(self, enemy, xp_sys):
        xp = enemy.kill()
        self.xp = xp_sys.add_xp(xp)
        self.level = xp_sys.try_level_up()


    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)