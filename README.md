**Project Title**: 
 - Untitled Potato Game

**Description**: 
 - In this game, the player attempts to peel potatoes with minimal mistakes and under a time limit. At the end, the score determines if the player wins or loses.
 - This program is made with Python and its libraries: pygame and pygame widgets.

**Features**:
 - **Main Menu**:
      - Navigation to play and options screens
      - Quit button to allow players to exit the game
 - **Options Menu**:
      - Fullscreen button that changes the resolution of the window to fullscreen. It can return the window back to the original scaling when pressed again.
      - Help button that takes the player to a description of the game.
      - Volume slider that changes the volume of the audio within the game.
 - **Play Screen**:
      - If a player goes off the potato or hits the border, they damage a finger.
      - If the player makes another mistake after all five fingers are injured, then the player loses the game.
      - The game ends after the timer runs out or after the player injures all five fingers.
 - **Game Over Screen**:
      - Displays if the player won or lost the game
      - Displays the player's score
      - Includes a button that can return the player to the main menu

**Installation**:
 - Python version 3.13.5
 - Pygame (python -m pip install pygame)
 - Pygame Widgets (python -m pip install pygame-widgets)
   
**How to run the game**:
 - Download the files in this repository
 - Open them using Visual Studio Code
 - In VS Code, open terminal, locate the directory you placed it in, and type "python game.py".
 - A window will open and this will allow the player to play the game.
 - To activate the peeling mechanism, click and drag on the potato using the mouse.
   
**File Structure**: 
 - **game.py**: main file to run the game
 - **button.py**: file for the Button class that is used for creating buttons
 - **cursor.py**: file for the Cursor class that manages the customized cursor
 - **pixel.py**: file for the Pixel class that manages the pixels for the Potato class
 - **potato.py**: file for the Potato class that manages the peeling of the potato using the Pixel class from pixel.py
 - **peel.py**: file for the Peel class that manages the animation of the potato peeling

**Credits**:
 - **Contributors**:
     - Kensey McDowell
     - Jake Weaver
     - Eliza Danila
 - Audio sourced from pixabay.com
