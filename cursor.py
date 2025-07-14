import pygame

class Cursor():
    def __init__(self):
        self.Raw_sprite = pygame.image.load("Assets/Peeler_Cursor.png")
        self.Cursor_sprite = pygame.transform.scale(self.Raw_sprite, (64,64)).convert_alpha()
        self.root = pygame.display.get_surface()
        self.x_pos = 0
        self.y_pos = 0

    def update(self):
        self.x_pos = pygame.mouse.get_pos()[0] - 16
        self.y_pos = pygame.mouse.get_pos()[1] - 16

    def draw(self):
        self.root.blit(self.Cursor_sprite, (self.x_pos, self.y_pos))


