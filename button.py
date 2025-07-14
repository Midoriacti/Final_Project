class Button():
    def __init__(self, image, x_pos, y_pos, text_in, font, baseColor, hoverColor):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.baseColor = baseColor
        self.hoverColor = hoverColor
        self.text_in = text_in
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text = self.font.render(self.text_in, True, self.baseColor)
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen): #draws button image and text to the screen
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_input(self, position): #returns true if clicked
        return self.rect.collidepoint(position)
    
    def change_color(self, position): #changes the text color on hover
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_in, True, self.hoverColor)
        else:
            self.text = self.font.render(self.text_in, True, self.baseColor)
