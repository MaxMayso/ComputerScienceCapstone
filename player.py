# Protect and Serve Game
# 
# Author : Max Maysonet-Ramirez
# Date : 05/25/2025
#
# Player State Class - "player.py"
#
# Stores information about the current game state including player location, inventory, and map.
#
# ---- Also includes methods to save and load game state using JSON.

import json
import os
from config import rooms, room_items

class GameState:
    def __init__(self, username, location="Bedroom", inventory=None):
        # Initialize player attributes
        self.username = username
        self.location = location
        self.inventory = set(inventory) if inventory else set()
        self.rooms = rooms  # Room layout from config
        self.room_items = room_items.copy()  # Items in rooms
        self.required_items = set(room_items.values()) - {"Burglar"}  # Win condition items

# Convert game state into a serializable dictionary
    def to_dict(self):
        return {
            "username": self.username,
            "location": self.location,
            "inventory": list(self.inventory)
        }

# Save the current game state to a JSON file
    def save_to_file(self):
        filename = f"{self.username}_save.json"
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f)
        print("Game saved successfully.")


# Load game state from a JSON file
    @staticmethod
    def load_from_file(username):
        filename = f"{username}_save.json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                return GameState(
                    username=data["username"],
                    location=data["location"],
                    inventory=data["inventory"]
                )
        else:
            print("No saved game found. Starting a new game.")
            return GameState(username)