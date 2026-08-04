import pygame, math

class Enemy:
    IMAGE = pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/Zombie/Zombie_idle/Zombie_idle1.png"), (100, 100)), flip_x=1, flip_y=0)
    zombie_walk_animation = [pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk1.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk2.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk3.png"),
                             pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk4.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk5.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk6.png"),
                             pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk7.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk8.png"), pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk9.png"),
                             pygame.image.load("assets/Zombie/Zombie_Walk/Zombie_Walk10.png")
                             ]
    zombie_attack_animation = [pygame.image.load("assets/Zombie/Zombie_Hurt/Zombie_Hurt1.png"), pygame.image.load("assets/Zombie/Zombie_Hurt/Zombie_Hurt2.png"),
                               pygame.image.load("assets/Zombie/Zombie_Hurt/Zombie_Hurt3.png"), pygame.image.load("assets/Zombie/Zombie_Hurt/Zombie_Hurt4.png")]


    def __init__(self, pos):
        self.x, self.y = pos
        self.image = Enemy.IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-85, -85)
        self.health = 100
        self.speed = 70
        self.goLeft = True
        self.gold_reward = 5
        self.isDead = True
        self.effects = []
        self.animation_speed = 0.15
        self.frame = 0
        self.current_point = 0
        self.isAttacking = False
        self.color_overlay = None

    def kill(self):
        if self.health <= 0:
            return self.isDead
        return False

    def add_effect(self, effect):
        self.effects.append(effect)

    def update(self, dt):
        for effect in self.effects[:]:
            effect.update(dt, self)
            if effect.expired():
                self.effects.remove(effect)

    def follow_path(self, path_point, dt):
        px, py = path_point
        dx = px - self.x
        dy = py - self.y

        distance = math.hypot(dx, dy)
        dx /= distance
        dy /= distance

        if distance >= 5:
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt
            self.rect.center = (self.x, self.y)
            self.hitbox.centerx = self.rect.centerx - 20
            self.hitbox.centery = self.rect.centery - 10
            return True
        self.isAttacking = True
        return False

    def animate_zombie_walk(self):
        self.frame += 0.21  # animation speed

        if self.frame >= len(Enemy.zombie_walk_animation):
            self.frame = 0

        self.image = pygame.transform.scale(Enemy.zombie_walk_animation[int(self.frame)], (100, 100))

    def animate_zombie_attack(self):
        self.frame += 0.21

        if self.frame >= len(Enemy.zombie_attack_animation): self.frame = 0

        self.image = pygame.transform.scale(Enemy.zombie_attack_animation[int(self.frame)], (100, 100))

    def set_color_overlay(self, color, alpha=128):
        w, h = self.image.get_size()  # use sprite size
        overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        overlay.fill((*color, alpha))
        self.color_overlay = overlay
