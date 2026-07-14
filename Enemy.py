import pygame

class Enemy:
    IMAGE = pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/Zombie/Zombie_idle/Zombie_idle1.png"), (100, 100)), flip_x=1, flip_y=0)

    def __init__(self, pos):
        self.image = Enemy.IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.health = 10
        self.speed = 100
        self.goLeft = True
        self.gold_reward = 5
        self.isDead = True

    def move(self, dt):
        self.rect.x += -self.speed * dt
        if self.rect.x <= 100 or self.rect.x >= 600:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, 1, 0)

    def kill(self):
        if self.health <= 0:
            return self.isDead
        return False