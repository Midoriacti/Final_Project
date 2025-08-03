import pygame #import pygame
import random #import random for chance variables
import math
from button import Button #import button class from button.py (can be used for all buttons)
from cursor import Cursor #imports cursor class from cursor.py
from potato import Potato #imports potato class from potato.py (uses buttons to make potatoes)

pygame.init() #initialize pygame

# initalize variables
menu_volume = 1.0 # default volume is max volume (1.0)
play_volume = 0.5 # default volume is half volume (0.5)
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
game_state = "Splash" #initializes game state to Splash for the game start

title_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 100) #loading the font for the title
title_text = title_font.render("Untitled Potato Game", True, "white") #rendering the title
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
title_rect_back = title_text.get_rect(center=(SCREEN_WIDTH // 2 + 5, 172))
title_back = title_font.render("Untitled Potato Game", True, "black") #rendering the title
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
MAX_LIVES = 6
SCORE_VAL = 1

player_score = 0

Play_theme = pygame.mixer.Sound("Assets/Play_Theme.wav")
Alarm = pygame.mixer.Sound("Assets/Timer_Alarm.wav")
Peeling_effect = pygame.mixer.Sound("Assets/peeling_effect.mp3")
time_limit = MAX_TIMER #this is in milliseconds
lives = MAX_LIVES
timer_reset = True
timer_done = False
Themeing = False
peeling_music = False
bad_peeling = False
peeling = False
peeled = False
peeling_again = True
spud_count = 0
spud = Potato(500,270)

Game_over_theme = pygame.mixer.Sound("Assets/Game_over_music2.mp3") #game over music

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
    x_pos = 130,
    y_pos = 70,
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

help_button = Button(
    image = scaled_button,
    x_pos = 640,
    y_pos = 640,
    text_in = "Help",
    font = pygame.font.Font('Assets/Ithaca-LVB75.ttf', 60),
    baseColor = "black",
    hoverColor = "white"
)

menu_button = Button(
    image = scaled_button, #potato peel button
    x_pos = SCREEN_WIDTH // 2, # x-coordinants on screen
    y_pos = 500, # y-coordinants on screen
    text_in = "Main Menu", #text to display
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

def Help_fade_in(screen, Help_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0,0,0))
    for alpha in range (255, -1, -3): #aplha = opacity thus when alpha is used the opacity is altered
        screen.blit(Help_scale, (0,0))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def Game_over_fade_in(screen, Option_scale, SCREEN_WIDTH, SCREEN_HEIGHT):
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
        Main_theme.play(-1).set_volume(menu_volume) #plays audio and the -1 loops it, lowers volume
        Menu_fade_in(screen, Menu_scale, 1250, 800) #call the menu fade in function
        fade_done = True #set fade done to true to stop the looping
    screen.blit(Menu_scale, (0,0)) #places the background
    
    screen.blit(title_back, title_rect_back) #update title
    
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
    global lives
    global player_score
    global time_limit
    global timer_reset
    global timer_done
    global mouse_pos
    global fade_done
    global spud_count
    global peeling
    global bad_peeling
    global peeling_again
    
    if not peeling:
        spud.new()
        peeling = True
            
    if spud.mouskatool():
        spud_count += 1
        player_score += SCORE_VAL
        peeling = False
    
    if not timer_reset:
        time_limit = MAX_TIMER #this is in milliseconds
        timer_reset = True
    Game_img = pygame.image.load("Assets/Game_Background.png").convert()
    Game_scale = pygame.transform.scale(Game_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Game_fade_in(screen, Game_scale, 1250, 800)
        # Play_theme.play(-1).set_volume(0.85)
        Play_theme.play(-1).set_volume(play_volume) #plays audio and the -1 loops it, lowers volume
        Alarm.set_volume(play_volume) #plays audio and the -1 loops it, lowers volume
        Peeling_effect.set_volume(play_volume) #plays audio and the -1 loops it, lowers volume
        lives = MAX_LIVES
        player_score = 0
        fade_done = True
    screen.blit(Game_scale, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    back_button.change_color(mouse_pos)
    back_button.update(screen)

    #timer section starts here 
    #start_time = pygame.time.get_ticks() #starts recording time
    time_limit -= 25 # counts down 25 is basically a second...for some reason
    seconds = time_limit // 1000 #makes it in seconds
    timer_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 50) #loading the font for the timer
    
    #black outline for timer
    timer_text_out = title_font.render(f'Time left: ', True, "black") #rendering the timer
    screen.blit(timer_text_out, (SCREEN_WIDTH - 995, 12))
    timer_num_out = title_font.render(f'{seconds}', True, "black") #rendering the numbers
    screen.blit(timer_num_out, (SCREEN_WIDTH - 645, 15))
    
    
    timer_text = title_font.render(f'Time left: ', True, "white") #rendering the timer
    screen.blit(timer_text, (SCREEN_WIDTH - 1000, 15))
    timer_num = title_font.render(f'{seconds}', True, "white") #rendering the numbers
    screen.blit(timer_num, (SCREEN_WIDTH - 650, 18))
    
    #Black outline for spuds
    spud_text = title_font.render(f'Naked Spuds: {spud_count}', True, "black") #rendering the timer
    screen.blit(spud_text, (SCREEN_WIDTH - 520, 15))
    
    spud_text = title_font.render(f'Naked Spuds: {spud_count}', True, "white") #rendering the timer
    screen.blit(spud_text, (SCREEN_WIDTH - 525, 18))
    #pygame.display.flip() #update display NOT NEEDED

    #put the hand behind the potato
    Hand_img = pygame.image.load("Assets/Hand_3_Fixed.png").convert_alpha()
    #print(f"Image width: {Hand_img.get_width()}")
    #print(f"Image height: {Hand_img.get_height()}")
    scaled_hand = pygame.transform.scale(Hand_img, (600, 600))
    screen.blit(scaled_hand, (SCREEN_WIDTH / 4, 100))

    #check if we peeled over the edge
    if peeling_again:
        bad_peeling = False
    if spud.ouch() and lives > 0 and not bad_peeling:
        lives -= 1
        bad_peeling = True
    
    if lives < 6:
        #put mark on 1st finger
        Mark_1 = pygame.Rect(SCREEN_WIDTH/3 + 80, 230, 10, 50)
        pygame.draw.rect(screen, "red", Mark_1)
        
        if lives < 5:
            #put mark on 2nd finger
            Mark_2 = pygame.Rect(SCREEN_WIDTH/2 + 70, 165, 7, 35)
            pygame.draw.rect(screen, "red", Mark_2)
            
            if lives < 4:
                #put mark on 3rd finger
                Mark_3_1 = pygame.Rect(SCREEN_WIDTH/2 + 130, 195, 7, 15)
                Mark_3_2 = pygame.Rect(SCREEN_WIDTH/2 + 123, 210, 7, 15)
                pygame.draw.rect(screen, "red", Mark_3_1)
                pygame.draw.rect(screen, "red", Mark_3_2)
                
                if lives < 3:
                    #put mark on 4th finger
                    Mark_4_1 = pygame.Rect(SCREEN_WIDTH/2 + 190, 195, 7, 15)
                    Mark_4_2 = pygame.Rect(SCREEN_WIDTH/2 + 183, 208, 7, 15)
                    Mark_4_3 = pygame.Rect(SCREEN_WIDTH/2 + 176, 221, 7, 15)
                    pygame.draw.rect(screen, "red", Mark_4_1)
                    pygame.draw.rect(screen, "red", Mark_4_2)
                    pygame.draw.rect(screen, "red", Mark_4_3)
                    
                    if lives < 2:
                        #put mark on 5th finger
                        Mark_5_1 = pygame.Rect(SCREEN_WIDTH/2 + 200, 320, 7, 25)
                        Mark_5_2 = pygame.Rect(SCREEN_WIDTH/2 + 193, 340, 7, 25)
                        pygame.draw.rect(screen, "red", Mark_5_1)
                        pygame.draw.rect(screen, "red", Mark_5_2)
                
    
    #visible potato!
    spud.show(screen)
    

    #cursor stuff leave this last or else cursor will not appear
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display

    if lives <= 0:
        #Game over (Failure)
        Play_theme.stop()
        Peeling_effect.stop()
        game_state = "Game Over"
        fade_done = False
        print(player_score)
        
        
    if time_limit <= 0:
        #Time ran out
        Play_theme.stop()
        Peeling_effect.stop()
        Alarm.play().set_volume(0.5)
        timer_reset = False
        peeling= False
        pygame.time.delay(2500)
        game_state = "Game Over"
        fade_done = False
        print(player_score)


def options_state():
    global mouse_pos
    global fade_done

    Option_img = pygame.image.load("Assets/Options_Background.png").convert()
    Option_scale = pygame.transform.scale(Option_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Main_theme.play(-1).set_volume(menu_volume) #plays audio and the -1 loops it, lowers volume
        Option_fade_in(screen, Option_scale, 1250, 800)
        fade_done = True
    screen.blit(Option_scale, (0,0))

    options_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 200) #loading the font for the title
    options_text = options_font.render("Options", True, "white") #rendering the title
    options_rect = options_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
    options_rect_back = options_text.get_rect(center=(SCREEN_WIDTH // 2 + 5, 172))
    options_back = options_font.render("Options", True, "black") #rendering the title
    screen.blit(options_back, options_rect_back) #update title
    screen.blit(options_text, options_rect) #update title

    mouse_pos = pygame.mouse.get_pos()
    back_button.change_color(mouse_pos)
    back_button.update(screen)
    fullscreen_button.change_color(mouse_pos)
    fullscreen_button.update(screen)
    volume_button.change_color(mouse_pos)
    volume_button.update(screen)
    help_button.change_color(mouse_pos)
    help_button.update(screen)
    #pygame.display.flip()
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display


def help_state():
    global mouse_pos
    global fade_done

    help_img = pygame.image.load("Assets/help_screen.png").convert()
    Help_scale = pygame.transform.scale(help_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Main_theme.play(-1).set_volume(menu_volume) #plays audio and the -1 loops it, lowers volume
        Help_fade_in(screen, Help_scale, 1250, 800)
        fade_done = True
    screen.blit(Help_scale, (0,0))

    help_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 200) #loading the font for the title
    help_text = help_font.render("Help", True, "white") #rendering the title
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH // 2, 90)) 
    help_rect_back = help_text.get_rect(center=(SCREEN_WIDTH // 2 + 5, 87))
    help_back = help_font.render("Help", True, "black") #rendering the title
    screen.blit(help_back, help_rect_back) #update title
    screen.blit(help_text, help_rect) #update title

    mouse_pos = pygame.mouse.get_pos()
    back_button.change_color(mouse_pos)
    back_button.update(screen)    
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display


def game_over_state():
    global lives
    global player_score
    global mouse_pos
    global fade_done
    
    # calculate score
    scoring = math.ceil((int(SCORE_VAL * spud_count) ** 2)*(int(lives) * .25))
    
    Game_over_img = pygame.image.load("Assets/Game_Over_Screen.png").convert()
    Game_over_scale = pygame.transform.scale(Game_over_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    if not fade_done:
        Game_over_theme.play(-1).set_volume(menu_volume) #plays audio and the -1 loops it, lowers volume
        Game_over_fade_in(screen, Game_over_scale, 1250, 800)
        fade_done = True
    screen.blit(Game_over_scale, (0,0))

    game_over_font = pygame.font.Font("Assets/Ithaca-LVB75.ttf", 150) #loading the font for the title

    if scoring >= 10:
        # winning text
        you_win_text_back = game_over_font.render("You Win!", True, "black") #rendering the title
        you_win_rect_back = you_win_text_back.get_rect(center=(SCREEN_WIDTH // 2 + 5, 172))
        screen.blit(you_win_text_back, you_win_rect_back) #update title
        you_win_text = game_over_font.render("You Win!", True, "white") #rendering the title
        you_win_rect = you_win_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
        screen.blit(you_win_text, you_win_rect) #update title
    else:
        # losing text
        you_lose_text_back = game_over_font.render("You Lose  :(", True, "black") #rendering the title
        you_lose_rect_back = you_lose_text_back.get_rect(center=(SCREEN_WIDTH // 2 + 5, 172))
        screen.blit(you_lose_text_back, you_lose_rect_back) #update title
        you_lose_text = game_over_font.render("You Lose  :(", True, "white") #rendering the title
        you_lose_rect = you_lose_text.get_rect(center=(SCREEN_WIDTH // 2, 175)) 
        screen.blit(you_lose_text, you_lose_rect) #update title
    
    # score text
    score_text_back = title_font.render(f"Score: {scoring}", True, "black") #rendering the title
    score_rect_back = score_text_back.get_rect(center=(SCREEN_WIDTH // 2, 330))  
    screen.blit(score_text_back, score_rect_back) #update title
    score_text = title_font.render(f"Score: {scoring}", True, "white") #rendering the title
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 333))
    screen.blit(score_text, score_rect) #update title
    
    mouse_pos = pygame.mouse.get_pos()
    menu_button.change_color(mouse_pos)
    menu_button.update(screen) 
    
    Custum_Cursor.update() #update the cursor location
    Custum_Cursor.draw() #draw the cursor
    pygame.display.flip() #update display


#game code
while running: #while the game is running
    pygame.mouse.set_visible(False) #make normal cursor invisible
    mouse_pos = pygame.mouse.get_pos()


    match game_state:
        case "Splash":
            splash_state()
        case "Menu":
            menu_state()
        case "Options":
            options_state()
        case "Help":
            help_state()
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
                    Play_theme.stop()
                    Peeling_effect.stop()
                    fade_done = False
                    game_state = "Menu"
                peeling_again = spud.peel(mouse_pos)
            elif game_state == "Options":
                if back_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Menu"
                    Main_theme.stop()
                if fullscreen_button.check_input(mouse_pos): #if fullscreen button is pressed
                    pygame.display.toggle_fullscreen()
                    # if in windowed
                    if fullscreen == False:
                        fullscreen_button.text_change("Fullscreen") # text change upon clicking
                        fullscreen = True
                    # if in fullscreen
                    elif fullscreen == True:
                        fullscreen_button.text_change("Windowed") # text change upon clicking
                        fullscreen = False
                    pygame.display.update()
                if volume_button.check_input(mouse_pos): # if volume button is pressed
                    if volume_display < 100:
                        if menu_volume < 1.0:
                            menu_volume += .10
                            volume_display += 10
                        if play_volume < 0.5:
                            play_volume += .10
                    else:
                        menu_volume = 0.0
                        play_volume = 0.0
                        volume_display = 0
                    volume_button.text_change(f"Volume: {volume_display}") # text change upon clicking
                    Main_theme.set_volume(menu_volume)
                    pygame.display.update()
                if help_button.check_input(mouse_pos): # if help button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Help"
                    Main_theme.stop()
            elif game_state == "Help":
                if back_button.check_input(mouse_pos): #if back button is pressed
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Options"
                    Main_theme.stop()
            elif game_state == "Game Over":
                if menu_button.check_input(mouse_pos):
                    pygame.time.delay(1000)
                    fade_out(screen, 1250, 800)
                    fade_done = False
                    game_state = "Menu"
                    Game_over_theme.stop()   
        if event.type == pygame.MOUSEBUTTONUP: #in the event of a button release 
            Clicked = False
            bad_peeling = False
            peeling_again = True
            if game_state == "Play" and peeling_music:
                Peeling_effect.stop()
                peeling_music = False
        
        if event.type == pygame.MOUSEMOTION:  # <-- NEW BLOCK: handle dragging
            if Clicked and game_state == "Play":
                peeling_again = spud.peel(mouse_pos)
                if not peeling_music:
                    Peeling_effect.play(-1).set_volume(0.4)
                    peeling_music = True
        
        if event.type == pygame.QUIT: #in the event of quit
            running = False #stop the while loop
    
    #clock.tick(FPS) #if we start changing the speed

pygame.quit() #close the game