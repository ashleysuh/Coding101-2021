#####################################################################
# game_SOL.py 
#
# contains logic functions to be called in driver code SOLUTION
# for tufts summer coding 101
#####################################################################

# importing random package for methods to generate random numbers
import random

# constant for winning number. you can set this to be any number (as long as 
# it's a power of 2) - try lower targets like 128 or 64 for testing, and
# higher targets like 4096 or 8192 for a challenge!
TARGET = 2048
 
# function start 
# params: 
# return: game board with two 2s in random position
# does:   starts up the game by providing controls to the user and initializing
#         the game board as a 2D list filled with 0s and two 2s
def start():
 
    # create an empty list and put four lists in it, each with four zeroes
    board = []
    for i in range(4):
        board.append([0] * 4)
    
    # notice that it is a list of lists, commonly called a 2D list or 2D array
    # uncomment the line below to see the structure of the list
    
    # print(board)
 
    # print a welcome message and the contrss to the user
    print("Welcome to 2048! Controls are as follows:")
    print("'w' : move up")
    print("'s' : move down")
    print("'a' : move left")
    print("'d' : move right")
 
    # add two 2s to the board and print it to the user
    add_new_2(board)
    add_new_2(board)
    print_board(board)
    return board


# function to add a new 2 in
# grid at any random empty cell
def add_new_2(board):
 
    # choose a random value between 0 and 3 to act as row and column for new 2
    r = random.randint(0, 3)
    c = random.randint(0, 3)
 
    # while the chosen coordinates already contain a value, find a new pair
    while(board[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
 
    # place a 2 at the coordinates 
    board[r][c] = 2


# function board_full
# params: game board
# return: true if board full, false otherwise
# does:   determines whether the board is full, i.e. if it contains any zeroes
def board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True


# function no_more_moves
# params: game board 
# return: true if more moves are still possible, false otherwise
# does:   determines whether there are still possible moves in the game 
#         there are a number of cases where moves are still possible, make sure 
#         you cover them all
def no_more_moves(board):
 
    # if you won the game, the game ends
    if won_game(board):
        return True 
    
    # if there are still empty spaces on the board, can still make more moves
    if not board_full(board):
        return False
 
    # if any two neighboring cells contain the same numbers, the game is 
    # not over and more moves are possible (i.e. a move to merge the numbers)
    for row in board:
        if row[0] == row[1] or row[1] == row[2] or row[2] == row[3]:
            return False
 
    for j in range(4):
        if (board[0][j] == board[1][j] or board[1][j] == board[2][j] or 
            board[2][j] == board[3][j]):
            return False
 
    # otherwise, no more move are possible and the game is over
    return True


# function won_game
# params: game board
# return: true if the target is on the board, false otherwise
# does:   determines whether the values on the board qualify to win, i.e. if 
#         the target is on the board
def won_game(board):
    for row in board:
        if TARGET in row:
            return True
    return False


# function compress 
# params: original game board 
# return: game board with numbers shifted to the left 
# does:   shifts numbers as far to the left as possible, i.e. 0 2 0 2 -> 2 2 0 0
def compress(board):
    
    for row in board:
        
        if row[0] == 0:
            row[0] = row[1]
            row[1] = 0
            
        if row[1] == 0:
            row[1] = row[2]
            row[2] = 0
            if row[0] == 0:
                row[0] = row[1]
                row[1] = 0
                
        if row[2] == 0:
            row[2] = row[3]
            row[3] = 0
            if row[1] == 0:
                row[1] = row[2]
                row[2] = 0
                if row[0] == 0:
                    row[0] = row[1]
                    row[1] = 0
    return board
 

# function merge 
# params: original game board
# return: game board with neighboring numbers merged
# does:   merges numbers to the left, i.e. 2 2 0 0 -> 4 0 0 0 
def merge(board):
     
    for row in board: 
        if row[0] == row[1]:
            row[0] = row[0] * 2
            row[1] = 0
        if row[1] == row[2]:
            row[1] *= 2
            row[2] = 0
        if row[2] == row[3]:
            row[2] *= 2
            row[3] = 0
 
    return board


# function flip
# params: original game board
# return: flipped game board
# does:   flips the content of the board horizontally, i.e. 0 0 2 4 -> 4 2 0 0
def flip(board):
    new_board =[]
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][3 - j])
    return new_board


# function transpose
# params: original game board
# return: transposed game board 
# does:   switches rows and columns of the board, so each row becomes a column 
#         and vice versa
def transpose(board):
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[j][i])
    return new_board


# function move_left 
# params: original game board 
# return: game board with numbers moved and merged to the left 
# does:   moves and merges numbers on the board toward the left
def move_left(board):

    # move numbers to the left
    board = compress(board)

    # merge neighboring numbers to the left
    board = merge(board)               #  2  2  4  4  ->  4  0  8  0 -> 4  8  0  0 

    # move numbers to the left once more
    board = compress(board)

    # return updated game board
    return board


# function move_right
# params: original game board 
# return: game board with numbers moved and merged to the right 
# does:   moves and merges numbers on the board toward the right
def move_right(board):
 
    # flip the board horizontally
    board = flip(board)
 
    # move left
    board = move_left(board)
 
    # flip the board back to get original board layout
    board = flip(board)
    
    return board


# function move_up
# params: original game board 
# return: game board with numbers moved and merged upwards
# does:   moves and merges numbers on the board upwards
def move_up(board):
 
    # transpose the board (switch rows and columns)
    board = transpose(board)
 
    # move left
    board = move_left(board)
 
    # transpose back to get original board layout
    board = transpose(board)
    
    return board


# function move_down
# params: original game board 
# return: game board with numbers moved and merged downwards
# does:   moves and merges numbers on the board downwards
def move_down(board):
 
    # transpose the board (switch rows and columns)
    board = transpose(board)
 
    # move right
    board = move_right(board)
 
    # transpose back to get original board layout
    board = transpose(board)
    
    return board


# function print_board 
# params: game board 
# return: 
# does:   formats and prints game board 
def print_board(grid):
    
    print()
    for row in grid:
        for square in row:
            if square == 0:
                print('-\t', end = '')
            else:
                print(str(square) + '\t', end = '')
        print('\n')