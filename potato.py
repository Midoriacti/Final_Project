from pixel import Pixel #import pixel class from pixel.py

#RGB = 165,89,0,255

class Potato():
    def __init__(self,potato_x,potato_y):
        self.potato_x = potato_x
        self.potato_y = potato_y
        self.border_color = (78,35,0,255)
        self.base_color = (165,89,0,255)
        
        #self.border_color = "black"
        #self.base_color = "red"
        
        self.peel_color = (246,207,73,255)
        self.potato_grid = []
        self.p_size = 30
        p_size = self.p_size
        
        #layer0 - 80 from left 0 from top 6 spaces total
        new_x = self.potato_x + self.p_size * 8
        new_y = self.potato_y + self.p_size * 0
        for i in range(6):
            self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            
            
        #layer1
        new_x = self.potato_x + self.p_size * 3
        new_y = self.potato_y + self.p_size * 1
        for i in range(13):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 11 or i == 12:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer2
        new_x = self.potato_x + self.p_size * 2
        new_y = self.potato_y + self.p_size * 2
        for i in range(16):
            if i == 0 or i == 14 or i == 15:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer3
        new_x = self.potato_x + self.p_size * 1
        new_y = self.potato_y + self.p_size * 3
        for i in range(18):
            if i == 0 or i == 17:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer4
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 4
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer5
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 5
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer6
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 6
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer7
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 7
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer8
        new_x = self.potato_x + self.p_size * 1
        new_y = self.potato_y + self.p_size * 8
        for i in range(19):
            if i == 0 or i == 18:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer9
        new_x = self.potato_x + self.p_size * 2
        new_y = self.potato_y + self.p_size * 9
        for i in range(18):
            if i == 0 or i == 17:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer10
        new_x = self.potato_x + self.p_size * 3
        new_y = self.potato_y + self.p_size * 10
        for i in range(17):
            if i == 0 or i == 16:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer11
        new_x = self.potato_x + self.p_size * 4
        new_y = self.potato_y + self.p_size * 11
        for i in range(15):
            if i == 0 or i == 1 or i == 2 or i == 11 or i == 12 or i == 13 or i == 14:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
                
                
        #layer12 - 80 from left 0 from top 6 spaces total
        new_x = self.potato_x + self.p_size * 7
        new_y = self.potato_y + self.p_size * 12
        for i in range(8):
            self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))

        
    def show(self,screen):
        for i in range(len(self.potato_grid)):
            self.potato_grid[i].draw(screen)
    
    def new():
        #creates a new potato
        pass
    
    def delete():
        #Deletes a potato
        pass
    
    def peel(mouse_pos):
        #peels a potato with the cursor
            #Takes mouse_pos and calls check_input() on all buttons
                #If over a button call change_color()
        pass