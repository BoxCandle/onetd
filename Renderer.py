import pygame

class Renderer:
    DARK_BROWN = (91, 49, 21)

    def __init__(self, screen):
        self.screen = screen

    def draw_background(self, map_surface : pygame.Surface, map_rect : pygame.Rect) -> None:
        self.screen.blit(map_surface, map_rect)

    def draw_tower(self, tower_surface : pygame.Surface, tower_rect : pygame.Rect) -> None:
        self.screen.blit(tower_surface, tower_rect)

    def draw_tower_health_bar(self, health : int, tower_x, tower_y) -> None:
        pygame.draw.rect(self.screen, Renderer.DARK_BROWN, pygame.Rect(tower_x + 27, tower_y - 25, 105, 15))
        pygame.draw.rect(self.screen, "Green", pygame.Rect(tower_x + 30, tower_y - 20, health, 5))

    def draw_enemy(self, enemy_surface : pygame.Surface, enemy_rect : pygame.Rect) -> None:
        self.screen.blit(enemy_surface, enemy_rect)

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
        gold_count = pygame.font.Font.render(pygame.font.SysFont(pygame.font.get_fonts()[0], 25), f'User gold:{str(user_gold)}', 1, (255, 255, 255))
        self.screen.blit(gold_count, (450, 10))