import pygame #import pygame
import random #import random for chance variables
from button import Button #import button class from button.py (can be used for all buttons)
from cursor import Cursor #imports cursor class from cursor.py

pygame.init() #initialize pygame

#boolean variables to control the game loop
running = True #runs the game
playing = False #dictates when the player is actively playing (for later use)
Clicked = False #boolean to check if mouse button clicked (for later use)
fade_done = False #makes it so the menu's fade in does not loop

#screen sizing
SCREEN_WIDTH = 1250 
SCREEN_HEIGHT = 800

#sizing adjustments for screen, title, and buttons
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #makes a screen
game_state = "Splash" #initializes game state to Splash for the game start

title_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 100) #loading the font for the title
title_text = title_font.render("Untitled Potato Game", True, "white") #rendering the title
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
screen.blit(title_text, title_rect) #update title

raw_button = pygame.image.load("Assets/Peel_button.png").convert_alpha() #load the button image
scaled_button = pygame.transform.scale(raw_button, (400, 150))  #make set width, height in pixels
small_scaled_button = pygame.transform.scale(raw_button, (250, 130)) #make smaller set

Main_theme = pygame.mixer.Sound("Assets/Main_theme.mp3") #main music
Custum_Cursor = Cursor()

#buttons start
play_button = Button(
    image = scaled_button, #potato peel button
    x_pos = 640, # x-coordinants on screen
    y_pos = 360, # y-coordinants on screen
    text_in = "Play", #text to display
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60), #giving it the custom font
    baseColor = "black", #sets the color (can only choose basic colors)
    hoverColor = "white" #sets the color when hovered over
)

Options_button = Button(
    image = scaled_button,
    x_pos = 640,
    y_pos = 500,
    text_in = "Options",
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60),
    baseColor = "black",
    hoverColor = "white"
)

Quit_button = Button(
    image = scaled_button,
    x_pos = 640,
    y_pos = 640,
    text_in = "Quit",
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60),
    baseColor = "black",
    hoverColor = "white"
)

back_button = Button(
    image = small_scaled_button,
    x_pos = 140,
    y_pos = 40,
    text_in = "Back",
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60),
    baseColor = "black",
    hoverColor = "white"
)
#buttons end 

#fades start
def Splash_fade_in(screen, Splash_scale, SCREEN_WIDTH, SCREEN_HEIGHT): #each fade in needs its own separate fade as the image is needed to fade in properly
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #set fade equal to screen size
    fade.fill((0,0,0)) #fill with black
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered (start at black and lighten to the image)
        screen.blit(Splash_scale, (0,0)) #draws the splash in the top left
        fade.set_alpha(alpha) #set the 
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Menu_fade_in(screen, Menu_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0,0,0))
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Menu_scale, (0,0))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Game_fade_in(screen, Game_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0,0,0))
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Game_scale, (0,0))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Option_fade_in(screen, Option_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0,0,0))
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Option_scale, (0,0))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def fade_out(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #set the fade to cover the entire screen
    fade.fill((0,0,0)) #fill fade with black 
    for alpha in range (0, 255, 3): #transition into back (starts at 0 and moves to 255(black) +3 every frame)
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0)) #
        pygame.display.update()
        pygame.time.delay(15)

#game code
while running: #while the game is running
    pygame.mouse.set_visible(False) #make normal cursor invisible

    #starting game state
    if game_state == "Splash": #Game state starts in splash then moves through states depending on buttons pressed
        Splash_img = pygame.image.load("Assets/Spuds_N_Buds.png").convert() #loads the image
        Splash_scale = pygame.transform.scale(Splash_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scales the image to fit screen size
        Splash_fade_in(screen, Splash_scale, 1250, 800) #calls fade in function and controls speed (each new background needs their own due to the image being needed for the fade in)
        screen.blit(Splash_scale, (0,0)) #displays image
        pygame.display.flip() #refreshes the screen
        pygame.time.delay(1500) #delay before fade out
        fade_out(screen, 1250, 800) #calls fade out (can be used for all transitions)
        game_state = "Menu" #set the game state to menu to continue on

    #now in menu game state
    if game_state == "Menu": 
        Menu_img = pygame.image.load("Assets/Potato_Menu.png").convert() #load background image
        Menu_scale = pygame.transform.scale(Menu_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale the image to screen size
        if not fade_done: #if statement to control fade out if not used fade out loops
            Main_theme.play(-1).set_volume(0.5) #plays audio and the -1 loops it, lowers volume
            Menu_fade_in(screen, Menu_scale, 1250, 800) #call the menu fade in function
            fade_done = True #set fade done to true to stop the looping
        screen.blit(Menu_scale, (0,0)) #places the background
        screen.blit(title_text, title_rect) #places the title text
        mouse_pos = pygame.mouse.get_pos() #constantly checks for the position of the mouse
        #these look for the mouse position if it goes on or off a button the color will update from base to hover or vise versa
        play_button.change_color(mouse_pos) 
        play_button.update(screen)
        Options_button.change_color(mouse_pos)
        Options_button.update(screen)
        Quit_button.change_color(mouse_pos)
        Quit_button.update(screen) 
        pygame.display.flip() #updates display (must be careful each time you do this stuff can get hidden behind it)
        Custum_Cursor.update() #update the cursor location
        Custum_Cursor.draw() #draw the cursor
        pygame.display.flip() #update display

    #now in play game state
    if game_state == "Play":
        #start_time = pygame.time.get_ticks() #starts recording time 
        Game_img = pygame.image.load("Assets/Game_Background.png").convert()
        Game_scale = pygame.transform.scale(Game_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        if not fade_done:
            Game_fade_in(screen, Game_scale, 1250, 800)
            fade_done = True
        screen.blit(Game_scale, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        back_button.change_color(mouse_pos)
        back_button.update(screen)
        pygame.display.flip()

        #timer section starts here (currently doesn't work if anyone wants to fix it)
        #time_limit = 100000 #this is in milliseconds 
        #current_time = pygame.time.get_ticks() #records for current time
        #count_down = max(0, time_limit - (current_time - start_time)) #prevents going past 0 when counting down
        #seconds = count_down // 1000 #makes it in seconds
        #timer_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 50) #loading the font for the timer
        #timer_text = title_font.render(f'Time left: {seconds}', True, "white") #rendering the timer
        #screen.blit(timer_text, (SCREEN_WIDTH - 700, 15))

        #cursor stuff leave this last or else cursor will not appear
        Custum_Cursor.update() #update the cursor location
        Custum_Cursor.draw() #draw the cursor
        pygame.display.flip() #update display

        if seconds == 0:
            game_state == "Game Over"
            fade_done = False

    if game_state == "Options":
        Option_img = pygame.image.load("Assets/Options_Background.png").convert()
        Option_scale = pygame.transform.scale(Option_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        if not fade_done:
            Option_fade_in(screen, Option_scale, 1250, 800)
            fade_done = True
        screen.blit(Option_scale, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        back_button.change_color(mouse_pos)
        back_button.update(screen)
        pygame.display.flip()
        Custum_Cursor.update() #update the cursor location
        Custum_Cursor.draw() #draw the cursor
        pygame.display.flip() #update display

    #if game_state == "Horror":


    for event in pygame.event.get(): #get an event
        #This block checkes for if the mouse is clicked thus we can click and drag
        if event.type == pygame.MOUSEBUTTONDOWN: #in the event of a button press
            if game_state == "Menu":
                if play_button.check_input(mouse_pos): #if play button is pressed
                    fade_done = False
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    game_state = "Play"
                    Main_theme.stop()
                if Options_button.check_input(mouse_pos): #if options button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Options"
                    Main_theme.stop()
                if Quit_button.check_input(mouse_pos): #if quit button is pressed
                    running = False
            elif game_state == "Play":
                if back_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Menu"
            elif game_state == "Options":
                if back_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Menu"
        if event.type == pygame.MOUSEBUTTONUP: #in the event of a button release 
            Clicked = False 
        if event.type == pygame.QUIT: #in the event of quit
            running = False #stop the while loop

pygame.quit() #close the game