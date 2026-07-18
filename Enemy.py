import pygame, math

class Enemy:
    IMAGE = pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/Zombie/Zombie_idle/Zombie_idle1.png"), (100, 100)), flip_x=1, flip_y=0)
    zombie_animation = [pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk1.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk2.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk3.png"),
                        pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk4.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk5.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk6.png"),
                        pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk7.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk8.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk9.png"),
                        pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk10.png")]
    def __init__(self, pos):
        self.image = Enemy.IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.health = 10
        self.speed = 100
        self.goLeft = True
        self.gold_reward = 5
        self.isDead = True
        self.effects = []
        self.animation_speed = 0.15
        self.frame = 0

    def kill(self):
        if self.health <= 0:
            return self.isDead
        return False

    def follow_path(self, path, dt):
        px, py = path
        dx = px - self.rect.x
        dy = py - self.rect.y

        distance = math.hypot(dx, dy)
        dx /= distance
        dy /= distance

        if distance >= 30:
            self.rect.x += dx * self.speed * dt
            self.rect.y += dy * self.speed * dt
            return None

        return None

    def animate_zombie(self):
        self.frame += 0.3  # animation speed

        if self.frame >= len(Enemy.zombie_animation):
            self.frame = 0

        self.image = pygame.transform.flip(pygame.transform.scale(Enemy.zombie_animation[int(self.frame)], (100, 100)), True, False)

