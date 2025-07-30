from pixel import Pixel #import pixel class from pixel.py

#RGB = 165,89,0,255

class Potato():
    def __init__(self,potato_x,potato_y):
        self.potato_x = potato_x
        self.potato_y = potato_y
        self.border_color = (78,35,0,255)
        self.base_color = (165,89,0,255)
        self.peeled_too_far = False
        self.peeled = False
        
        #self.border_color = "black"
        #self.base_color = "red"
        
        self.peel_color = (246,207,73,255)
        self.potato_grid = []
        self.p_size = 15
        p_size = self.p_size
        tot = 0
        
        #layer0 - 80 from left 0 from top 6 spaces total
        new_x = self.potato_x + self.p_size * 8
        new_y = self.potato_y + self.p_size * 0
        for i in range(6):
            self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            self.potato_grid[tot].locked = True
            tot += 1
        
            
            
        #layer1
        new_x = self.potato_x + self.p_size * 3
        new_y = self.potato_y + self.p_size * 1
        for i in range(13):
            if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 11 or i == 12:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer2
        new_x = self.potato_x + self.p_size * 2
        new_y = self.potato_y + self.p_size * 2
        for i in range(16):
            if i == 0 or i == 14 or i == 15:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer3
        new_x = self.potato_x + self.p_size * 1
        new_y = self.potato_y + self.p_size * 3
        for i in range(18):
            if i == 0 or i == 17:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer4
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 4
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer5
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 5
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer6
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 6
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer7
        new_x = self.potato_x + self.p_size * 0
        new_y = self.potato_y + self.p_size * 7
        for i in range(20):
            if i == 0 or i == 19:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer8
        new_x = self.potato_x + self.p_size * 1
        new_y = self.potato_y + self.p_size * 8
        for i in range(19):
            if i == 0 or i == 18:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer9
        new_x = self.potato_x + self.p_size * 2
        new_y = self.potato_y + self.p_size * 9
        for i in range(18):
            if i == 0 or i == 17:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer10
        new_x = self.potato_x + self.p_size * 3
        new_y = self.potato_y + self.p_size * 10
        for i in range(17):
            if i == 0 or i == 16:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer11
        new_x = self.potato_x + self.p_size * 4
        new_y = self.potato_y + self.p_size * 11
        for i in range(15):
            if i == 0 or i == 1 or i == 2 or i == 11 or i == 12 or i == 13 or i == 14:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
                self.potato_grid[tot].locked = True
            else:
                self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.base_color))
            tot += 1
                
                
        #layer12 - 80 from left 0 from top 6 spaces total
        new_x = self.potato_x + self.p_size * 7
        new_y = self.potato_y + self.p_size * 12
        for i in range(8):
            self.potato_grid.append(Pixel(new_x + p_size * i, new_y, self.border_color))
            self.potato_grid[tot].locked = True
            tot += 1

        
    def show(self,screen):
        for i in range(len(self.potato_grid)):
            self.potato_grid[i].draw(screen)
    
    def new(self):
        #creates a new potato
        self.__init__(500,270)
    
    def peel(self,mouse_pos):
        #peels a potato with the cursor
            #Takes mouse_pos and calls check_input() on all buttons
        for i in range(len(self.potato_grid)):
            if self.potato_grid[i].check_input(mouse_pos) and self.potato_grid[i].locked == False:
                self.potato_grid[i].change_color(self.peel_color)
                self.potato_grid[i].peeled = True
                self.peeled = True
                #If over a button call change_color()
            elif self.potato_grid[i].check_input(mouse_pos) and self.potato_grid[i].locked == True:
                self.peeled_too_far = True
                self.peeled = False
        return self.peeled
                
    def ouch(self):
        #checking if we went too far
        if self.peeled_too_far:
            self.peeled_too_far = False
            return True
        else:
            return False
                
    def mouskatool(self): #Hot Dog! Mouseker Hey, Mouseker Hi, Mouseker Ho! Mouseker ready, Mouseker set, Here we go! (check if potato is peeled)
        count = 0
        for i in range(len(self.potato_grid)):
            if self.potato_grid[i].peeled:
                count += 1
        if count == (len(self.potato_grid) - 47):
            return True
        else:
            return False