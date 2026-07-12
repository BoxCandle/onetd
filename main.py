import pygame
from Renderer import Renderer
from Tower import Tower
from Enemy import Enemy
pygame.init()

WIDTH = 600
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

map_surface = pygame.image.load("assets/Maps/Map.jpg")
map_rect = map_surface.get_rect(center=(WIDTH // 2,HEIGHT // 2))

TOWER = Tower((50, HEIGHT // 2 - 50))

clock = pygame.time.Clock()
SPAWN_POINT = 550, HEIGHT // 2 - 50

enemies = []

renderer = Renderer(window)

while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 50 <= mouse_pos[0] <= 150:
                enemies.append(Enemy(SPAWN_POINT))
                print("enemy count", len(enemies))

    for enemy in enemies:
        enemy.move(dt)

    renderer.draw_background(map_surface, map_rect)
    renderer.draw_tower(TOWER.image, TOWER.rect)

    for enemy in enemies:
        renderer.draw_enemy(enemy.image, enemy.rect)
        renderer.draw_enemy_health_bar(enemy.health, enemy.rect[0], enemy.rect[1])

    renderer.spawn_enemy_button()
    renderer.draw_tower_health_bar(TOWER.health, TOWER.rect[0], TOWER.rect[1])

    pygame.display.flip()