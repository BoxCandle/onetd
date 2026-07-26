import pygame, copy
from Renderer import Renderer
from Tower import Tower
from Enemy import Enemy
from Bullet import Bullet
from gold_system import GoldSystem
from Player import Player
from Cannons import cannons

particle_group = pygame.sprite.Group()

pygame.init()

WIDTH = 1280
HEIGHT = 720
PATH_POINT = 950, 305


window = pygame.display.set_mode((WIDTH, HEIGHT))


map_surface = pygame.transform.scale(pygame.image.load("assets/Maps/Map.png").convert(), (1280, 720))

clock = pygame.time.Clock()
SPAWN_POINT = 0 + 400, HEIGHT // 2 - 50
PLAYER = Player()
enemies = []
bullets = []
towers = []
shop = [Tower(cannons["Cannon"], (WIDTH // 2, 620)), Tower(cannons["SniperCannon"], (WIDTH // 2 + 100, 620))]
queue = []
renderer = Renderer(window)
gold_system = GoldSystem(PLAYER.gold)
holding = False
show_details = False
tools = False

while True:
    mouse_pos = pygame.mouse.get_pos()
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if 50 <= mouse_pos[0] <= 200 and 50 <= mouse_pos[1] <= 100:
                enemies.append(Enemy(SPAWN_POINT))

            for tower in shop:
                if tower.rect.collidepoint(mouse_pos) and tower.cost <= PLAYER.gold:
                    new_tower = tower.copy()
                    new_tower.rect.center = mouse_pos
                    queue.append(new_tower)
                    holding = True
                    PLAYER.gold -= 5

        if event.type == pygame.MOUSEBUTTONDOWN and holding:
            holding = False
            queue[0].rect.center = mouse_pos
            tower = queue.pop(0)
            towers.append(tower)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if tools:
                tools = False
            else:
                tools = True

    if holding and queue:
        queue[0].rect.center = mouse_pos

    for enemy in enemies:
        enemy.follow_path(PATH_POINT,dt)

        if enemy.kill():
            PLAYER.gold = gold_system.add_gold(enemy.gold_reward)
            enemies.remove(enemy)

    for tower in towers:
        tower.isActive = True
        if tower.isActive:
            for enemy in enemies:
                if tower.enemy_in_range(enemy):
                    bullets.append(Bullet((tower.rect.centerx, tower.rect.centery - 20), enemy, speed = 200, damage = tower.damage)) ; break

    now = pygame.time.get_ticks()

    for bullet in bullets[:]:
        if bullet.update(dt):
            bullet.target.health -= bullet.damage
            bullets.remove(bullet)

    renderer.draw_background(map_surface)
    renderer.draw_tower_inventory()

    for enemy in enemies:
        if enemy.isAttacking: enemy.animate_zombie_attack()
        enemy.animate_zombie_walk()
        renderer.draw_enemy(enemy.image, enemy.rect)
        renderer.draw_enemy_health_bar(enemy.health, enemy.rect[0], enemy.rect[1])

    for tower in towers:
        for enemy in enemies:
            tower.turn_cannon(enemy.rect.center)
        renderer.draw_tower(tower.image, tower.rect)

    for tower in shop:
        renderer.draw_tower(tower.image, tower.rect)

    for tower in queue:
        renderer.draw_tower(tower.image, tower.rect)

    for bullet in bullets: renderer.draw_bullet(bullet.image, bullet.rect)

    if tools:
        renderer.draw_path_point(PATH_POINT)
        for tower in towers:
            renderer.draw_tower_range(tower.rect.center, tower.show_range())
    renderer.draw_spawn_enemy_button()
    renderer.draw_user_gold(PLAYER.gold)

    particle_group.draw(window)

    pygame.display.flip()