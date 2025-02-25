# Michael Zaccaria

def instructions():  # Create function that introduces the game, tells player the object, and lists valid inputs
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Welcome to Viral Outbreak! A text Adventure/Survival game.\n')
    print('The objective of the game is find and collect six items to defeat the Zombie Horde.')
    print('However, you must be careful. If you run into the hoard before collecting all 6 items you will fall to them.\n')
    print('Movement Commands: go North, go South, go East, go West.\n')
    print('To add items to your inventory enter: get "item name".')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def story():  # Create function that tells player the backstory of the game
    print('Backstory:\nIt started as any ordinary day in your high-clearance lab. You got into work and were responding to some emails in your office like you normally do.\nHowever, you started to hear a commotion coming from the Laboratory. Glass shattering and people screaming, everyone began frantically running around the Main Office.\nYou knew what happened without even needing to look, immediately you slammed your office door shut and locked it behind you.\nSomeone had dropped one of the test tubes containing a highly contagious virus in the Laboratory.\nAs you waited and listened in horror you could hear your once co-workers turning into uncontrollable monsters.\nYou knew your best chance at survival was to wait until night, and once it had set in you decided it was time to move.')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def main():  # Create function that holds most of the gameplay code and rooms dictionary
    rooms = {
        'Main Office': {'go north': 'Security Checkpoint', 'go south': 'Decontamination Chamber', 'go east': 'Stairwell', 'go west': 'Laboratory', 'item': ''},
        'Security Checkpoint': {'go south': 'Main Office', 'go east': 'Armory', 'item': 'Kevlar Vest'},
        'Armory': {'go west': 'Security Checkpoint', 'item': 'Gun'},
        'Laboratory': {'go east': 'Main Office', 'item': 'Anti-Virus'},
        'Stairwell': {'go north': 'Kitchen', 'go west': 'Main Office', 'item': 'Emergency Axe'},
        'Kitchen': {'go south': 'Stairwell', 'item': 'Food Stash'},
        'Decontamination Chamber': {'go north': 'Main Office', 'go east': 'Lobby', 'item': 'Hazmat Suit'},
        'Lobby': {'go west': 'Decontamination Chamber', 'boss': 'Zombie Horde', 'item': ''}
    }

    start_room = 'Main Office'  # Set start room to main office

    current_room = start_room  # Set current room to start room

    inventory = []  # Create a blank list for the inventory

    while True:  # Start loop
        print(f'You are in the {current_room}')  # Print message telling the player the room they are in
        print(f'Inventory: {inventory}')  # Print message telling the player what items they have in their inventory

        direction = input('\nEnter your move: ')  # Prompt player to enter their move

        if direction.lower() in rooms[current_room]:  # Check to see if the move is valid
            current_room = rooms[current_room][direction.lower()]  # If valid then move player to a new room based on direction

        elif direction.lower() == 'get ' + str(rooms[current_room]['item']).lower():  # Check if the player entered 'get ' to pick up an item
            if rooms[current_room]['item'] in inventory:  # Check to see if the item they are trying to pick up is already in their inventory and if it is then...
                print('You already have this item in your inventory.')  # ...Print message saying the item has already been picked up

            else:
                inventory.append(rooms[current_room]['item'])  # Else add item to their inventory

        else:
            print('\nInvalid Input. Please enter a valid input.')  # All other inputs return as invalid

        if 'item' in rooms[current_room].keys() and rooms[current_room]['item'] != '':  # Check if item is in the current room the player is in and has not been picked up yet
            near_item = rooms[current_room]['item']  # Set near item to the item in the current room
            if near_item not in inventory:  # If near item is not in the players inventory then print a spacer
                print('------------------------------------------')

                if near_item[-1] == 's':  # If the last letter of the item is an 'S' then print a message for proper grammar
                    print(f'\nYou see an {near_item}!\n')

                else:  # For all other items and proper grammar
                    print(f'\nYou see a {near_item}!\n')

        if 'boss' in rooms[current_room].keys():  # If the boss is in the room the player is currently in...

            if len(inventory) < 6:  # ...And if the length of their inventory is less than 6 items
                print(f'\nYou died to the {rooms[current_room]["boss"]}. Better luck next time, make sure you collect all six items before trying to defeat the Zombie Horde!')  # Then print death message
                break

            else:  # Else their inventory has 6 items
                print(f'\nYou killed the {rooms[current_room]["boss"]}! Congratulations! Thanks for playing, I hope you enjoyed Viral Outbreak!')  # Print victory message
                break
        print('------------------------------------------')


# Run all functions below in order listed
instructions()
story()
main()
