import pygame

class Enemy:
    IMAGE = pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/Zombie/Zombie_idle/Zombie_idle1.png"), (100, 100)), flip_x=1, flip_y=0)

    def __init__(self, pos):
        self.image = Enemy.IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.health = 10
        self.speed = 300

    def move(self, dt):
        goLeft = True
        self.rect[0] -= 1 * self.speed * dt
        if goLeft and 100 < self.rect[0] <= 600:
            self.speed = self.speed
        else:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed

