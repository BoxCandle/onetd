import pygame as pg

class Tower:
    def __init__(self, position : tuple,):
        self.x, self.y = position
        self.image = pg.image.load("Tower.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.level = 1
        self.xp = 0
        self.ammo = 3
        self.shoot_delay = 500
        self.last_shot = pg.time.get_ticks()
        self.last_mag = pg.time.get_ticks()
        self.reload = 1000

    def on_enemy_killed(self, enemy, xp_sys):
        xp = enemy.kill()
        self.xp = xp_sys.add_xp(xp)
        self.level = xp_sys.try_level_up()


    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)
        pg.draw.rect(surface, "Cyan", (self.x - 30, self.y - 50, self.xp, 5))
        pg.draw.rect(surface, "Blue", (self.x - 30, self.y - 50, self.level * 5, 10), 3)

        #ADD HEALTHBAR
        #ADD XP BAR
        #ADD LEVEL
        #ADD UPGRADES