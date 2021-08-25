#####################################################################
# main.py 
#
# driver for 2048 game 
#####################################################################
 
# importing the game.py file to access and use the functions we wrote
import game
# set up the game using our start() function
board = game.start()
 
# start the control loop, which drives the process of user input -> board shift
# -> user input -> board shift -> ...
while(True):
 
    # take the user input
    x = input("Your move: ")
 
    # if the input is 'w', call the function which moves the numbers up
    if (x == 'w'):
        board = game.move_up(board)
    elif (x == 's'):                    # if input is 's'...
        board = game.move_down(board)
    elif (x == 'a'):                    # if input is 'a'...
        board = game.move_left(board)
    elif (x == 'd'):                    # if input is 'd'
        board = game.move_right(board)     
    else:                               # otherwise, display error message
        print("Invalid key - please enter 'w', 'a', 's', or 'd'")
        continue                        # and restart loop
        
    
    # if the game board isn't full, we need to add a new 2 after every move
    if not game.board_full(board):
        game.add_new_2(board)
    
    # if the game is over, break out of the loop
    if game.no_more_moves(board):
        break
 
    # print the updated game board
    game.print_board(board);
    

# print the board once more after game ends
game.print_board(board)

# print appropriate message depending on whether user won or lost
# feel free to write your own personalized message!
if game.won_game(board):
    print('you won!')
else:
    print('better luck next time')