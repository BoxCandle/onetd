from Renderer import Renderer
from Tower import *
from Enemy import Enemy
from gold_system import GoldSystem
from Player import Player

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
RENDERER = Renderer(window)
GOLD_SYS = GoldSystem(PLAYER.gold)

basic_cannon = BasicCannon((WIDTH // 2, 600))
sniper_cannon = SniperCannon((WIDTH // 2 + 100, 600))
fire_cannon = FireCannon((WIDTH // 2 + 200, 600))

enemies = []
bullets = []
active_cannons = []
shop = [basic_cannon, sniper_cannon, fire_cannon]
queue = []

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

            for cannon in shop:
                if cannon.rect.collidepoint(mouse_pos) and cannon.cost <= PLAYER.gold:
                    new_cannon = cannon.copy()
                    new_cannon.rect.center = mouse_pos
                    queue.append(new_cannon)
                    holding = True
                    PLAYER.gold -= cannon.cost

        if event.type == pygame.MOUSEBUTTONDOWN and holding:
            holding = False
            queue[0].rect.center = mouse_pos
            cannon = queue.pop(0)
            active_cannons.append(cannon)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if tools:
                tools = False
            else:
                tools = True

    if holding and queue:
        queue[0].rect.center = mouse_pos

    for enemy in enemies:
        enemy.follow_path(PATH_POINT,dt)
        enemy.update(dt)

        if enemy.kill():
            PLAYER.gold = GOLD_SYS.add_gold(enemy.gold_reward)
            enemies.remove(enemy)

    for cannon in active_cannons:
        for enemy in enemies:
            if cannon.enemy_in_range(enemy):
                bullets.append(cannon.spawn_bullet(enemy))
                break

    now = pygame.time.get_ticks()
    for bullet in bullets[:]:
        if bullet.update(dt):
            bullet.target.health -= bullet.damage
            bullets.remove(bullet)

    RENDERER.draw_background(map_surface)
    RENDERER.draw_cannon_inventory()

    for enemy in enemies:
        if enemy.isAttacking: enemy.animate_zombie_attack()
        enemy.animate_zombie_walk()
        RENDERER.draw_enemy(enemy)
        RENDERER.draw_enemy_health_bar(enemy.health, enemy.rect[0], enemy.rect[1])

    for cannon in active_cannons:
        target = None

        for enemy in enemies:
            if cannon.enemy_in_range(enemy):
                target = enemy
                break

        if target:
            cannon.turn_cannon(target.rect.center)
        RENDERER.draw_cannon(cannon.image, cannon.rect)

    for cannon in shop:
        RENDERER.draw_cannon(cannon.image, cannon.rect)

    for cannon in queue:
        RENDERER.draw_cannon(cannon.image, cannon.rect)

    for bullet in bullets:
        RENDERER.draw_bullet(bullet.image, bullet.rect)

    if tools:
        RENDERER.draw_path_point(PATH_POINT)
        for enemy in enemies:
            RENDERER.draw_enemy_hitbox(enemy)
        for cannon in active_cannons:
            RENDERER.draw_cannon_range(cannon.rect.center, cannon.show_range())
        for bullet in bullets:
            RENDERER.draw_bullet_hitbox(bullet)
    RENDERER.draw_spawn_enemy_button()
    RENDERER.draw_user_gold(PLAYER.gold)

    particle_group.draw(window)

    pygame.display.flip()