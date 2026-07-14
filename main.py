import pygame
from Renderer import Renderer
from Tower import Tower
from Enemy import Enemy
from Bullet import Bullet
from gold_system import GoldSystem
pygame.init()

WIDTH = 600
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

map_surface = pygame.image.load("assets/Maps/Map.jpg")
map_rect = map_surface.get_rect(center=(WIDTH // 2,HEIGHT // 2))

TOWER = Tower((50, HEIGHT // 2 - 50))

clock = pygame.time.Clock()
SPAWN_POINT = 550, HEIGHT // 2 - 50

user_gold = 0
enemies = []
bullets = []
towers = [TOWER]
renderer = Renderer(window)
gold_system = GoldSystem(user_gold)


while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 50 <= mouse_pos[0] <= 200 and 50 <= mouse_pos[1] <= 100:
                enemies.append(Enemy(SPAWN_POINT))
                print("enemy count", len(enemies))
                print("bullet count", len(bullets))

    for enemy in enemies:
        enemy.move(dt)
        if enemy.kill():
            user_gold = gold_system.add_gold(enemy.gold_reward)
            enemies.remove(enemy)

    for tower in towers:
        for enemy in enemies:
            if tower.enemy_in_range(enemy):
                bullets.append(Bullet(tower.rect.center, enemy, speed = 200, damage = 5))
                break

    now = pygame.time.get_ticks()

    for bullet in bullets[:]:
        if bullet.update(dt):  # returns True when bullet hits
            bullet.target.health -= bullet.damage
            bullets.remove(bullet)

    renderer.draw_background(map_surface, map_rect)
    renderer.draw_tower(TOWER.image, TOWER.rect)

    for enemy in enemies:
        renderer.draw_enemy(enemy.image, enemy.rect)
        renderer.draw_enemy_health_bar(enemy.health, enemy.rect[0], enemy.rect[1])

    for bullet in bullets:
        renderer.draw_bullet(bullet.image, bullet.rect)

    renderer.draw_spawn_enemy_button()
    renderer.draw_tower_health_bar(TOWER.health, TOWER.rect[0], TOWER.rect[1])
    renderer.draw_user_gold(user_gold)
    pygame.display.flip()