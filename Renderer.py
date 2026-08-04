import pygame

class Renderer:
    DARK_BROWN = (91, 49, 21)
    DARK_BROWN_2 = (64, 36, 11)
    BROWN = (138, 91, 65)


    def __init__(self, screen):
        self.screen = screen

    def draw_background(self, map_surface : pygame.Surface) -> None:
        self.screen.blit(map_surface, (0,0))

    def draw_cannon(self, tower_surface : pygame.Surface, tower_rect : pygame.Rect) -> None:
        self.screen.blit(tower_surface, tower_rect)
        if pygame.event == pygame.MOUSEBUTTONDOWN:
            self.draw_cannon_range(tower_rect, range)

    def draw_enemy(self, enemy) -> None:
        self.screen.blit(enemy.image, enemy.rect)

        if enemy.color_overlay:
            self.screen.blit(enemy.color_overlay, enemy.rect)

    def draw_enemy_health_bar(self, health : int, enemy_x, enemy_y) -> None:
        pygame.draw.rect(self.screen, Renderer.DARK_BROWN, pygame.Rect(enemy_x + 27, enemy_y - 25, 15, 15))
        pygame.draw.rect(self.screen, "Green", pygame.Rect(enemy_x + 30, enemy_y - 20, health, 5))

    def draw_spawn_enemy_button(self):
        pygame.draw.rect(self.screen, Renderer.DARK_BROWN, pygame.Rect(50, 50, 150, 50))
        text = pygame.font.Font.render(pygame.font.SysFont(pygame.font.get_fonts()[0], 25), "Spawn enemy", 1, (255, 255, 255))
        self.screen.blit(text, (57, 57))

    def draw_bullet(self, bullet_surface : pygame.Surface, bullet_rect : pygame.Rect) -> None:
        self.screen.blit(bullet_surface, bullet_rect)

    def draw_user_gold(self, user_gold):
        gold_count = pygame.font.Font.render(pygame.font.SysFont(pygame.font.get_fonts()[0], 25), f'Gold:{str(user_gold)}', 1, (245, 197, 39))
        self.screen.blit(gold_count, (100, 580))

    def draw_cannon_inventory(self):
        pygame.draw.rect(self.screen, Renderer.DARK_BROWN_2, pygame.Rect(0, 520, 1280, 200))
        pygame.draw.rect(self.screen, Renderer.BROWN, pygame.Rect(5, 525, 1270, 190))

    def draw_cannon_range(self, tower_pos, tower_range):
        pygame.draw.circle(self.screen, "Red", tower_pos, tower_range, 2)

    def draw_path_point(self, cords):
        pygame.draw.circle(self.screen, "Cyan", cords, 30)

    def draw_enemy_hitbox(self, enemy):
        pygame.draw.rect(self.screen, "Red", enemy.hitbox, 1)

    def draw_bullet_hitbox(self, bullet):
        pygame.draw.rect(self.screen, "Red", bullet.hitbox, 1)
