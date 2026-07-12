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

    def spawn_enemy_button(self):
        pygame.draw.rect(self.screen, Renderer.DARK_BROWN, pygame.Rect(50, 50, 100, 50))