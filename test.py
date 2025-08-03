import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Falling Potato Sprite"

#custom sprite class for falling potato peel
class FallingPotato(arcade.Sprite):
    def __init__(self, scale):
        super().__init__("Assets/Potato_anim_1.png", scale) #loads the sprite image and scales it 
        #randomize various fall speeds
        self.angle_speed = random.uniform(-2, 2)
        self.fall_speed = random.uniform(2, 5)
        self.sway_speed = random.uniform(0.5, 1.5)
        #randomizes direction it sways
        self.sway_direction = random.choice([-1, 1])

    #update every frame
    def update(self, delta_time: float = 1/60):
        self.center_y -= self.fall_speed
        self.center_x += self.sway_speed * self.sway_direction
        self.angle += self.angle_speed

        if self.center_y < -self.height:
            self.remove_from_sprite_lists()

class PotatoFallGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.potato_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        self.potato_list.draw()

    def on_update(self, delta_time):
        self.potato_list.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            potato = FallingPotato(scale=0.2)
            potato.center_x = x
            potato.center_y = y
            self.potato_list.append(potato)

# Run the game
game = PotatoFallGame()
arcade.run()

