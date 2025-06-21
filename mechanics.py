# Protect and Serve Game
# 
# Author : Max Maysonet-Ramirez
# Date : 05/25/2025
#
# Game Logic - "mechanics.py"
#
# Contains core game mechanics including movement, item collection, game saving, and win/loss logic

from player import GameState

# Handles logic for picking up an item in the current room
def pickup_item(state):
    item = state.room_items.get(state.location)
    if item:
        print(f"You see a {item} on the floor. Would you like to pick it up? (yes/no)")
        if input().strip().lower() == 'yes':
            state.inventory.add(item)
            del state.room_items[state.location]
            print(f"{item} has been added to your inventory.")
        else:
            print("You left the item on the floor.")
        print("Current inventory:", ", ".join(state.inventory))

# Parses the player's input to extract a direction word
def parse_direction(command):
    command = command.lower()
    directions = {'north', 'south', 'east', 'west'}
    for direction in directions:
        if direction in command:
            return direction
    return None

# Main game loop
def play_game(state):
    while True:
        print(f"\n{state.username}, you are in the {state.location}.")
        # Check if player loses
        if state.location == "Foyer":
            print("\nYou see the burglar. You lose!!")
            restart = input("Would you like to restart the game? (yes/no): ").strip().lower()
            if restart == "yes":
                # Reset the game state with the same username
                from player import GameState
                state = GameState(state.username)
                continue
            else:
                print('Thank you for playing!!')
                break

        # Check for item in current room and handle pickup
        if state.location in state.room_items:
            pickup_item(state)
            # Check if player has collected all required items
            if state.required_items.issubset(state.inventory):
                print("\nYou've assembled your gun! You win!")
                print("Oh wait, it's only your daughter getting home early from that sleepover.")
                break

        # Show valid directions from current location
        directions = state.rooms.get(state.location, {})
        print("You can go:", ", ".join(directions.keys()))

        # Handle user input
        user_input = input("What would you like to do?: ").strip().lower()
        if user_input == 'exit':
            state.save_to_file()
            print("Thank you for playing and goodbye!")
            break

        # Move player to new location if valid direction
        direction = parse_direction(user_input)
        if direction and direction in directions:
            state.location = directions[direction]
        else:
            print("Invalid direction. Try again.")