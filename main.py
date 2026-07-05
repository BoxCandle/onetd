import pygame as pg
import random
from enemy import Enemy
from Bullet import Bullet
from tower_system import Tower
from collision_system import Collision
from level_system import LevelSystem

pg.init()
pg.mixer.init()

window_height = 500
window_width = 500
screen = pg.display.set_mode((window_width, window_height))

# Colors
PALE_BLUE = (73, 144, 209)
CEMENT = (54, 54, 54)
RED = (168, 0, 0)
BLACK = (20, 20, 20)

def spawn_enemy():
    x = random.randint(400, window_width)
    y = random.randint(400, window_height)
    return x, y

# Sounds
shoot_sound = pg.mixer.Sound("Shootsound.wav")

# Constants
TOWER_COLOR = CEMENT
ENEMY_COLOR = RED
BULLET_COLOR = BLACK

# Game state
tower_pos = (window_width // 2, window_height // 2)
bullet_pos = tower_pos
tower_radius = 20
enemy_radius = 10
bullet_radius = 5
bullet_speed = 200

tower = Tower(tower_pos)
enemies = []
bullets = []
clock = pg.time.Clock()
running = True
interval = 500
last_time = pg.time.get_ticks()

while running:
    dt = clock.tick(60) / 1000
    collision_system = Collision(bullets, enemies)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(PALE_BLUE)

    # RESPAWN ENEMY AND BULLET IF NEEDED
    if not enemies:
        enemies.append(Enemy(5, spawn_enemy()))
        for enemy in enemies:
            enemies[-1].update()
            enemy.target(tower_pos, dt)

    now = pg.time.get_ticks()

    if tower.ammo > 0 and now - tower.last_shot >= tower.shoot_delay:
        bullets.append(Bullet(tower_pos, speed = 50, damage = 5))
        tower.ammo -= 1
        tower.last_shot = now

    for bullet in bullets:
        bullet.update(dt, enemies[-1].rect.center)

    # CHECK COLLISION BETWEEN BULLET AND ENEMY
    collision_system.update()
    xp_system = LevelSystem(tower, enemies[-1])
    # GIVE XP TO PLAYER IF ENEMY IS KILLED
    for enemy in enemies:
        if not enemy.alive:
            tower.on_enemy_killed(enemies[-1], xp_system)
    # REMOVE DEAD ENEMIES AND BULLETS
    bullets = [b for b in bullets if b.alive]
    enemies = [e for e in enemies if e.alive]

    # DRAW TOWER
    tower.draw(screen)

    # DRAW ENEMIES
    for enemy in enemies:
        enemy.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    pg.display.flip()