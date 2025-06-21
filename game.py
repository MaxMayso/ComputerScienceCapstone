
# Protect and Serve Game
# 
# Author : Max Maysonet-Ramirez
# Date : 05/25/2025
#
# Game Entry Point - "game.py"
# Initializes and launches the game loop.

from player import GameState
from mechanics import play_game

# Displays game intro and initializes the game state
def main():
    print("                       ****Welcome to Protect and Serve!****")
    print("A burglar has broken into your home, where you now have to protect yourself!")
    print("But oh no, you now find yourself having to assemble your weapon!")
    print("Run around your house and find the parts that you need to assemble your weapon!")
    print('How to play: Type commands like "go north", "move west", or "run east" to travel.')
    print('Type "yes" or "no" to pick up parts and store them in your inventory.')
    print('Type "exit" to quit the game at any time.\n')

    username = input("Enter your character name: ").strip()

    game_loader = input ('Want to load a saved game? (yes/no): ').strip().lower()
    if game_loader == 'yes':
        state = GameState.load_from_file(username)
    else:
        state = GameState(username)
        
    play_game(state)


# Run game
if __name__ == "__main__":
    main()
