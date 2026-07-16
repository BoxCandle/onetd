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

clock = pygame.time.Clock()
SPAWN_POINT = 550, HEIGHT // 2 - 50


enemies = []
bullets = []
towers = []
renderer = Renderer(window)
gold_system = GoldSystem(user_gold)
holding = False

effects = {
    "poison" : {"dps" : 1, "duration" : 5},
    "burn" : {"dps" : 2, "duration" : 3}
}
user_gold = 0

while True:

    if not towers:
        towers.append(Tower((200, 500)))

    mouse_pos = pygame.mouse.get_pos()
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and 50 <= mouse_pos[0] <= 200 and 50 <= mouse_pos[1] <= 100:
            enemies.append(Enemy(SPAWN_POINT))
            print("enemy count", len(enemies))
            print("bullet count", len(bullets))

        if event.type == pygame.MOUSEBUTTONDOWN and (towers[-1].rect.centerx - 50 <= mouse_pos[0] <= towers[-1].rect.centerx + 50 and
                    towers[-1].rect.centery - 50 <= mouse_pos[1] <= towers[-1].rect.centery + 50):
            towers[-1].rect.center = mouse_pos
            holding = True

        if event.type == pygame.MOUSEBUTTONUP:
            holding = False

    if holding:
        towers[-1].rect.center = mouse_pos

    for enemy in enemies:
        enemy.move(dt)
        if enemy.kill():
            user_gold = gold_system.add_gold(enemy.gold_reward)
            enemies.remove(enemy)

    for tower in towers:
        if tower.rect[1] <= 200 and not holding:
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
    renderer.draw_tower_inventory()

    for tower in towers:
        renderer.draw_tower(tower.image, tower.rect)
        if tower.rect[1] <= 200:
            renderer.draw_tower_health_bar(tower.health, tower.rect[0], tower.rect[1])
            renderer.draw_tower_range(tower.rect.center, tower.range)

    for enemy in enemies:
        renderer.draw_enemy(enemy.image, enemy.rect)
        renderer.draw_enemy_health_bar(enemy.health, enemy.rect[0], enemy.rect[1])

    for bullet in bullets:
        renderer.draw_bullet(bullet.image, bullet.rect)

    renderer.draw_spawn_enemy_button()
    renderer.draw_user_gold(user_gold)



    pygame.display.flip()
