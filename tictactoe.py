"""
This script will be used to create a tictactoe game using python.
The game will be played by two players, one using 'X' and the other using 'O'.

Player one have id 1 and player two id 2.

"""
##
#%%
import numpy as np


RULES = """
The game is played on a grid that's 3 squares by 3 squares.
To play, you simply type the number of the square you want to place your 'X' or 'O' in.
The board is displayed as follows:
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
"""

# {0: ' ', 1: 'X', 2: 'O'}
def _int_convert(x):
    mapping = {0: ' ', 1: 'X', 2: 'O'}
    return mapping[x]

to_string = np.vectorize(_int_convert)

##
#%%

def print_board(board) -> None:
    
    if isinstance(board, np.ndarray):
        board = to_string(board)

    print(board[0, 0], '|', board[0, 1], '|', board[0, 2])
    print('---------')
    print(board[1, 0], '|', board[1, 1], '|', board[1, 2])
    print('---------')
    print(board[2, 0], '|', board[2, 1], '|', board[2, 2])
    
# %%

def check_win(board):
    """
    Check if there is a winner.
    If there is one, return is id.
    If there is two winner at the same time (because the rules were not followed),
    it will return the first winner identified (line, then rows, then diags).
    """
    
    # Check each lines
    for line in board:
        # If all the elements of the line are equal to the first one 
        if line[0] != .0 and np.all(line == line[0]):
            return line[0]
    
    # Check each rows
    for row in board.T:
        # If all the elements of the row are equal to the first one
        if row[0] != .0 and np.all(row == row[0]):
            return row[0]
        
    # Check the first diag
    if board[0, 0] != .0 and np.all(np.diagonal(board) == board[0, 0]):
        return board[0, 0]
    
    # Check the second diag
    if board[0, 2] != .0 and np.all(np.diagonal(np.fliplr(board)) == board[0, 2]):
        return board[0, 2]
    
    return 0
    
    
# %%
