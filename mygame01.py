#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import time 
def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    
    To win:
    i) Get to the Garden with a key and potion.
        or 
    ii) Get to the Garage with a key and drive().
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print(f"Numer of moves: {move_count}")
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print ('Hints for Navigation : \n' + rooms[currentRoom]['desc'] )
    print("---------------------------")
    


# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'desc'  : 'Dining room on East, Kitchen on South'

                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster.',
                  'desc'  : 'Your invisible cloak saved you. \nGet another from Living Room if you need to come back to kitchen. \nCan only go North from here'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : '[potion, water]',
                  'north': 'Living Room',
                  'east':  'Drawing Room',
                  'desc' : 'Hall on West, Living Room on North, Garden on South, Drawing Room on East'

               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'east'  : 'Bedrooom',
                  'desc'  : 'Dining Room on North, Bedroom on East'
                },
            #Adding 4 more rooms to the game 
            'Living Room' : {
                  'south' : 'Dining Room',
                  'east'  : 'Garage',
                  'item'  : 'invisible_cloak',
                  'desc'  : 'Dining room on South, Garage on East'
                },

            'Garage' : {
                  'west'  : 'Living Room',
                  'south' : 'Drawing Room',
                  'item'  : 'car',
                  'desc'  : 'Drawing room on South, Living Room on West'
                },
            'Drawing Room' : {
                  'west' : 'Dining Room',
                  'south': 'Bedroom',
                  'north': 'Garage',
                  'item' : 'wine',
                  'desc' : 'Garage on North, Dining Room on West, Bedroom on South'
               },
            'Bedroom' : {
                  'north' : 'Drawing Room',
                  'west'  : 'Garden',
                  'item'  : 'sleep',
                  'desc'  : 'Drawing Room on North, Garden on West'
                }
         }

# start the player in the Hall
currentRoom = 'Hall'
move_count = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            move_count +=1 
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')
    
    #check if the last cell of split list is room
    #if yes, combine last two words for full name of the room
    if move[-1] == 'room':
        move[2] = move[2] + " " + move[3]
        
        

    #if they type 'teleport to ....'  
    if (move[0]+ " " + move[1]) == 'teleport to':
        move[2] = move[2].title()
        #check that they are allowed wherever they want teleport to
        if move[2] in rooms.keys():
            #set the current room to the new room
            currentRoom = move[2]
            move_count +=1
            print('Be patient. You are being teleported to ......' + currentRoom)
            #delay in coding while teleporting 
            time.sleep(2)
        # if they aren't allowed to go that way:
        else:
            print('You can\'t teleport there!')
            
        #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    ## Player does not lose if they have an 'invisible cloak' in their inventory: monster cannot see them
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'invisible_cloak' not in inventory:
        print('A monster has got you... GAME OVER!')
        break
    ## the invisible cloak is used and removed from the inventory  
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'invisible_cloak' in inventory:
        inventory.remove('invisible_cloak')
        

    ## i. win scenario I : Define how a player can win 
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## ii. Win scenario II: Define how a player can win
    if currentRoom == 'Garage' and 'key' in inventory and 'car' in inventory:
        print('You escaped the hosue in the car ... YOU WIN!')
        break






















