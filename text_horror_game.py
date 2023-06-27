import time

# This starts the first room of the game
def play_game():
    player_inventory = ['start']
    i = 0
    while i == 0:
        user_move = input('What would you like to do? ')
        if user_move == 'check desk':
            print('you found an old brass key!')
            time.sleep(1)
            print('Maybe you can use it to open the door')
            player_inventory = ['Old Brass Key']
        elif user_move == 'check armchair':
            time.sleep(1)
            print('An old dingy armchair. It looks like something you would find at a garage sale.')
        elif user_move == 'check bed':
            time.sleep(1)
            print('You see a disgusting looking bed with stained sheet. You think to yourself "How could anyone sleep on this?"')
        elif user_move == 'open door':
            if 'Old Brass Key' in player_inventory:
                time.sleep(1)
                print('You unlock the door.')
                time.sleep(1)
                print('You walk through the door to a find a another room...')
                time.sleep(1)
                i += 1
            else:
                time.sleep(1)
                print('The door is locked.')
        else:
            time.sleep(1)
            print('invalid input')

def second_room():
    user_second_move = input('would you like to look around? ')
    if user_second_move == 'yes':
        print('You see stuff')
    else:
        print('Fuck you')
        

# This would act as the start screen of the game
start_game = input('Would you like to play? ')
if start_game == 'yes' or start_game == 'y' or start_game == 'YES' or start_game == 'Yes':
    time.sleep(1)
    print('You wake up in a dingy dark room. You look around and notice a dusty stained armchair in the center of the room, a dusty desk with a few drawers with rusty knobs, and a bed in the corner of the room. The door is sitting opposite of you at the other end of the room.')
    time.sleep(5)
    play_game()
    second_room()
else:
    print('Maybe next time.')