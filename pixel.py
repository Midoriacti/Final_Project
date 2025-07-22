import pygame

class Pixel:
    def __init__(self, x_pos, y_pos, baseColor, width=30, height=30):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.baseColor = baseColor
        self.width = width
        self.height = height

        # Rectangle for the pixel
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x_pos, self.y_pos)

    def check_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, new_color):
        self.baseColor = new_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.baseColor, self.rect)
