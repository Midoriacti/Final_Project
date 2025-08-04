import pygame
import random

class Peel:
    def __init__(self, x, y, scale):
        original_image = pygame.image.load("Assets/Potato_anim_1.png").convert_alpha()
        width = int(original_image.get_width() * scale)
        height = int(original_image.get_height() * scale)
        self.original_image = pygame.transform.scale(original_image, (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        # Animation properties
        self.angle = 0
        self.angle_speed = random.uniform(-2, 2)
        self.fall_speed = random.uniform(2, 5)
        self.sway_speed = random.uniform(0.5, 1.5)
        self.sway_direction = random.choice([-1, 1])

    def update(self):
        # Move down and sway left/right
        self.rect.y += self.fall_speed
        self.rect.x += self.sway_speed * self.sway_direction
        self.angle += self.angle_speed

        # Rotate image around its center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        # Draw the peel to the given surface
        surface.blit(self.image, self.rect)

    def is_off_screen(self, screen_height):
        return self.rect.top > screen_height
