#!/usr/bin/python3

import random

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in a ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(list(inventory)))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = set()

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'north': 'Study',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'item': 'key'
    },
    'Study': {
        'south': 'Hall',
        'east': 'Dining Room',
        'item': 'sabre'
    },
    'Bedroom': {
        'north': 'Bedroom',
        'south': 'Kitchen',
        'east': 'Hall',
        'west': 'Bedroom',
        'item': 'elixir'
    },
    'Kitchen': {
        'north': 'Hall',
        'south': 'Garden',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Kitchen',
        'north': 'Study',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Kitchen'
    }
}

# start the player in the Hall
currentRoom = random.choice(list(filter(lambda x: x not in ["Kitchen", "Garden"], rooms.keys())))

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # Define how a player can win
            if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
                print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
                break
            # If a player enters a room with a monster
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
                if 'sabre' in inventory:
                    print('A monster attacks, but you use your sabre to slay it!')
                    del rooms[currentRoom]['item']
                elif 'elixir' in inventory:
                    inventory.remove('elixir')
                    print('A monster attacks and almost kills you! You used your elixir to heal yourself. You better '
                          'get out of here before it attacks again!')
                else:
                    print('A monster has got you... GAME OVER!')
                    break
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.add(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
