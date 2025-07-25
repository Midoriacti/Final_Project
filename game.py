import pygame #import pygame
import random #import random for chance variables
from button import Button #import button class from button.py (can be used for all buttons)
from cursor import Cursor #imports cursor class from cursor.py
from potato import Potato #imports potato class from potato.py (uses buttons to make potatoes)

pygame.init() #initialize pygame

# initalize variables
volume = 1.0 # default volume is max volume (1.0)
volume_display = 100 # default display volume is max (100)

#boolean variables to control the game loop
running = True #runs the game
playing = False #dictates when the player is actively playing (for later use)
Clicked = False #boolean to check if mouse button clicked (for later use)
fade_done = False #makes it so the menu's fade in does not loop
fullscreen = False # boolean for fullscreen/windowed button
Horror = False

#screen sizing
SCREEN_WIDTH = 1250 
SCREEN_HEIGHT = 800

#sizing adjustments for screen, title, and buttons
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #makes a screen
game_state = "Play" #initializes game state to Splash for the game start

title_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 100) #loading the font for the title
title_text = title_font.render("Untitled Potato Game", True, "white") #rendering the title
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
screen.blit(title_text, title_rect) #update title

raw_button = pygame.image.load("Assets/Peel_button.png").convert_alpha() #load the button image
scaled_button = pygame.transform.scale(raw_button, (400, 150))  #make set width, height in pixels
small_scaled_button = pygame.transform.scale(raw_button, (250, 130)) #make smaller set

Main_theme = pygame.mixer.Sound("Assets/Main_theme.mp3") #main music
Custum_Cursor = Cursor()


#Gameplay loop variables
#clock = pygame.time.Clock() #for changing internal clock
#FPS = 30
MAX_TIMER = 100000
time_limit = MAX_TIMER #this is in milliseconds
timer_reset = True
peeling = False
peeled = False
spud_count = 0
spud = Potato(500,270)

#Horror
horror_shade = (255, 0, 0, 90) #red

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

fullscreen_button = Button(
    image = scaled_button, #potato peel button
    x_pos = 640, # x-coordinants on screen
    y_pos = 360, # y-coordinants on screen
    text_in = "Fullscreen", #text to display
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60), #giving it the custom font
    baseColor = "black", #sets the color (can only choose basic colors)
    hoverColor = "white" #sets the color when hovered over
)

volume_button = Button(
    image = scaled_button, #potato peel button
    x_pos = 640, # x-coordinants on screen
    y_pos = 500, # y-coordinants on screen
    text_in = "Volume: 100", #text to display
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60), #giving it the custom font
    baseColor = "black", #sets the color (can only choose basic colors)
    hoverColor = "white" #sets the color when hovered over
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
        
#------------------HORROR FADES------------------

def Horror_Splash_fade_in(screen, Splash_scale, SCREEN_WIDTH, SCREEN_HEIGHT): #each fade in needs its own separate fade as the image is needed to fade in properly
    Horror_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #set fade equal to screen size
    Horror_fade.fill(horror_shade)  # Red
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered (start at black and lighten to the image)
        screen.blit(Splash_scale, (0,0)) #draws the splash in the top left
        Horror_fade.set_alpha(alpha) #set the 
        screen.blit(Horror_fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Horror_Menu_fade_in(screen, Menu_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    Horror_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    Horror_fade.fill(horror_shade)  # Red
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Menu_scale, (0,0))
        Horror_fade.set_alpha(alpha)
        screen.blit(Horror_fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Horror_Game_fade_in(screen, Game_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    Horror_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    Horror_fade.fill(horror_shade)  # Red
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Game_scale, (0,0))
        Horror_fade.set_alpha(alpha)
        screen.blit(Horror_fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Horror_Option_fade_in(screen, Option_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    Horror_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    Horror_fade.fill(horror_shade)  # Red
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Option_scale, (0,0))
        Horror_fade.set_alpha(alpha)
        screen.blit(Horror_fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Horror_fade_out(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    Horror_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #set the fade to cover the entire screen
    Horror_fade.fill(horror_shade)  # Red
    for alpha in range (0, 255, 3): #transition into back (starts at 0 and moves to 255(black) +3 every frame)
        Horror_fade.set_alpha(alpha)
        screen.blit(Horror_fade, (0,0)) #
        pygame.display.update()
        pygame.time.delay(15)
        
        
def splash_state():
    global game_state
    
    Splash_img = pygame.image.load("Assets/Spuds_N_Buds.png").convert() #loads the image
    Splash_scale = pygame.transform.scale(Splash_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scales the image to fit screen size
    Splash_fade_in(screen, Splash_scale, 1250, 800) #calls fade in function and controls speed (each new background needs their own due to the image being needed for the fade in)
    screen.blit(Splash_scale, (0,0)) #displays image
    
    if Horror:
        Horror_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        Horror_overlay.fill(horror_shade)  # Red
        screen.blit(Horror_overlay, (0, 0))
    
    pygame.display.flip() #refreshes the screen
    pygame.time.delay(1500) #delay before fade out
    fade_out(screen, 1250, 800) #calls fade out (can be used for all transitions)
    game_state = "Menu" #set the game state to menu to continue on


def menu_state():
    global fade_done
    global mouse_pos
    
    Menu_img = pygame.image.load("Assets/Potato_Menu.png").convert() #load background image
    Menu_scale = pygame.transform.scale(Menu_img, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale the image to screen size
    if not fade_done: #if statement to control fade out if not used fade out loops
        Main_theme.play(-1).set_volume(volume) #plays audio and the -1 loops it, lowers volume
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
    #pygame.display.flip() #updates display (must be careful each time you do this stuff can get hidden behind it)
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    
    if Horror:
        Horror_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        Horror_overlay.fill(horror_shade)  # Red with 50% opacity
        screen.blit(Horror_overlay, (0, 0))
    pygame.display.flip() #update display


def play_state(spud):
    global game_state
    global time_limit
    global timer_reset
    global mouse_pos
    global fade_done
    global spud_count
    global peeling

    if not peeling:
        spud.new()
        peeling = True
            
    if spud.mouskatool():
        spud_count += 1
        peeling = False
    
    if not timer_reset:
        time_limit = MAX_TIMER #this is in milliseconds
        timer_reset = True
    Game_img = pygame.image.load("Assets/Game_Background.png").convert()
    Game_scale = pygame.transform.scale(Game_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Game_fade_in(screen, Game_scale, 1250, 800)
        fade_done = True
    screen.blit(Game_scale, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    back_button.change_color(mouse_pos)
    back_button.update(screen)
    #pygame.display.flip() #NOT NEEDED

    #timer section starts here (currently doesn't work if anyone wants to fix it)
    #start_time = pygame.time.get_ticks() #starts recording time
    time_limit -= 25 # counts down 25 is basically a second...for some reason
    seconds = time_limit // 1000 #makes it in seconds
    timer_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 50) #loading the font for the timer
    timer_text = title_font.render(f'Time left: ', True, "white") #rendering the timer
    screen.blit(timer_text, (SCREEN_WIDTH - 1000, 15))
    timer_num = title_font.render(f'{seconds}', True, "white") #rendering the numbers
    screen.blit(timer_num, (SCREEN_WIDTH - 650, 18))
    
    spud_text = title_font.render(f'Naked Spuds: {spud_count}', True, "white") #rendering the timer
    screen.blit(spud_text, (SCREEN_WIDTH - 525, 18))
    #pygame.display.flip() #update display NOT NEEDED

    #visible potato!
    spud.show(screen)

    #cursor stuff leave this last or else cursor will not appear
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display


    if time_limit <= 0:
        timer_reset = False
        peeling= False
        game_state = "Menu"


def options_state():
    global mouse_pos
    global fade_done
    
    Option_img = pygame.image.load("Assets/Options_Background.png").convert()
    Option_scale = pygame.transform.scale(Option_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Main_theme.play(-1).set_volume(volume) #plays audio and the -1 loops it, lowers volume
        Option_fade_in(screen, Option_scale, 1250, 800)
        fade_done = True
    screen.blit(Option_scale, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    back_button.change_color(mouse_pos)
    back_button.update(screen)
    fullscreen_button.change_color(mouse_pos)
    fullscreen_button.update(screen)
    volume_button.change_color(mouse_pos)
    volume_button.update(screen)
    #pygame.display.flip()
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display


def game_over_state():
    pass


#game code
while running: #while the game is running
    pygame.mouse.set_visible(False) #make normal cursor invisible


    match game_state:
        case "Splash":
            splash_state()
        case "Menu":
            menu_state()
        case "Options":
            options_state()
        case "Play":
            play_state(spud)
        case "Game Over":
            game_over_state()
        case "Horror":
            pass


    for event in pygame.event.get(): #get an event
        #This block checkes for if the mouse is clicked thus we can click and drag
        if event.type == pygame.MOUSEBUTTONDOWN: #in the event of a button press
            Clicked = True
            if game_state == "Menu":
                if play_button.check_input(mouse_pos): #if play button is pressed
                    fade_done = False
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    timer_reset = False
                    peeling = False
                    spud_count = 0
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
                spud.peel(mouse_pos)
            elif game_state == "Options":
                if back_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Menu"
                    Main_theme.stop()
                if fullscreen_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    pygame.display.toggle_fullscreen()
                    if fullscreen == False:
                        fullscreen_button.text_change("Windowed") # text change upon clicking
                        fullscreen = True
                    elif fullscreen == True:
                        fullscreen_button.text_change("Fullscreen") # text change upon clicking
                        fullscreen = False
                    pygame.display.update()
                if volume_button.check_input(mouse_pos): # if volume button is pressed
                    pygame.time.delay(1000)
                    if volume < 1.0 and volume_display < 100:
                        volume += .10
                        volume_display += 10
                    else:
                        volume = 0.0
                        volume_display = 0
                    volume_button.text_change(f"Volume: {volume_display}") # text change upon clicking
                    Main_theme.set_volume(volume)
                    # print(f"PRINTING THE VOLUME IN OPTIONS: {Main_theme.get_volume()}")
                    pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP: #in the event of a button release 
            Clicked = False 
        
        if event.type == pygame.MOUSEMOTION:  # <-- NEW BLOCK: handle dragging
            if Clicked and game_state == "Play":
                spud.peel(mouse_pos)
        
        if event.type == pygame.QUIT: #in the event of quit
            running = False #stop the while loop
    
    #clock.tick(FPS) #if we start changing the speed

pygame.quit() #close the game