
# Protect and Serve Game
# 
# Author : Max Maysonet-Ramirez
# Date : 05/25/2025
#
# Config File - "config.py"
# Contains static data defining the rooms in the game and the items found within them.

# Dictionary mapping room names to item names found in each room
room_items = {
    'Family room': 'Ammo',
    'Library': 'Iron Sight',
    'Kitchen': 'Grip',
    'Office': 'Clip',
    'Living room': 'Gun frame',
    'Foyer': 'Burglar',
    'Garage': 'Muzzle',
}

# Dictionary defining allowed room-to-room directional navigation
rooms = {
    'Bedroom': {"east": "Family room"},
    'Family room': {'north': 'Living room', 'west': 'Bedroom', "east": 'Kitchen', 'south': 'Library'},
    'Library': {'north': 'Family room', 'east': 'Office'},
    'Office': {'west': 'Library'},
    'Living room': {'south': 'Family room', 'east': 'Garage'},
    'Garage': {'west': 'Living room'},
    'Kitchen': {'west': 'Family room', 'north': 'Foyer'},
    'Foyer': {'south': 'Kitchen'},
}
