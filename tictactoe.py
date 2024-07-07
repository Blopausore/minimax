"""
This script will be used to create a tictactoe game using python.
The game will be played by two players, one using 'X' and the other using 'O'.

Player one have id 1 and player two id 2.

"""
##
#%%
import numpy as np


RULES = """

Hello on Tic Tac Toe ! 
The game is played on a grid that's 3 squares by 3 squares.
To play, you simply type the number of the square you want to place your 'X' or 'O' in.
The board is displayed as follows:
            1 | 2 | 3
            ---------
            4 | 5 | 6
            ---------
            7 | 8 | 9
====================================
=========== LET'S PLAY =============

"""
board = np.zeros((3, 3), dtype=int)

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

def del_board():
    for _ in range(6):
        print("\033[A\033[K", end='', flush=True)
    
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

def check_end(board):
    """
    Check if the board is complete
    Return True if it is 
    """
    return not np.any(board == 0)

def sign_choice():
    """
    Return the identifier choosen by the player
    """
    player = None
    while not player in {'X', 'O'}:
        print("X or O? ", end="", flush=True)
        player = input()
        # Delete the last line
        print("\033[A\033[K", end='', flush=True)

    return 1 if player == "X" else 2

def ask_to_play(board, player):
    """
    Return the cell where the player play at
    """
    print("Your turn ! ", end="", flush=True)
    x = int(input()) -1
    
    # Create board coordinate
    i, j = x//3, x%3
    print("\033[A\033[K", end='', flush=True)
    # If the cell do not exist or is already occupied
    if (not 0<= x< 9) or (not board[i, j] == 0):
        ask_to_play(player)
    
    board[i, j] = player
    
def play_random(board, id):
    """
    Let the player id, play randomly
    """
    # Search the coordinates of free cell
    coords = np.argwhere(board == 0)
    if coords.shape[0] == 0:
        raise 
    coord = coords[np.random.randint(0, coords.shape[0]-1)]
    board[coord[0], coord[1]] = id

##
#%%

def maximin(board, player_id, computer_id, depth):
    # print(f"Iteration {depth}")
    # print(board)
    # input("\n")
    # del_board()
    winner = check_win(board)
    if winner == player_id:
        return -1
    elif winner != 0:
        return 1
    
    moves = np.argwhere(board == 0)
    if moves.shape[0] == 0:
        return 0
    scores = np.zeros(moves.shape[0])
    for i in range(moves.shape[0]):
        board[moves[i][0], moves[i][1]] = player_id
        scores[i] = minimax(board, player_id, computer_id, depth+1)
        board[moves[i][0], moves[i][1]] = 0
    return np.min(scores)

def minimax(board, player_id, computer_id, depth=0):
    # print(f"Iteration {depth}")
    # print(board)
    # input("\n")
    # del_board()

    winner = check_win(board)
    if winner == computer_id:
        return 1
    elif winner != 0:
        return -1
    
    moves = np.argwhere(board == 0)
    if moves.shape[0] == 0:
        return 0
    scores = np.zeros(moves.shape[0]) 
    for i in range(moves.shape[0]):
        board[moves[i][0], moves[i][1]] = computer_id
        scores[i] = maximin(board, player_id, computer_id, depth+1)
        board[moves[i][0], moves[i][1]] = 0
    if depth == 0:
        return moves[np.argmax(scores)]
    return np.max(scores)

def computer_play(board, player, computer):
    move = minimax(board, player, computer)
    board[move[0], move[1]] = computer

##
#%%

def main():
    done = False
    print(RULES)
    board = np.zeros((3, 3), dtype=int)
    player = sign_choice()
    computer = 1 if player == 2 else 2
        
    print_board(board)
    if player == 1:
        ask_to_play(board, player)
    del_board()
    while not done:
        # Computer turn
        computer_play(board, player, computer)
        winner = check_win(board)
        # del_board()
        if winner != 0:
            done = True
        elif check_end(board):
            done = True
            winner = 0
        print_board(board)
        ask_to_play(board, player)
        del_board()
    print_board(board)
    print(winner)
        
main()

# %%


def custom_board1():
    board[1, 1] = 1
    board[1, 2] = 2
    board[2, 2] = 1
    board[2, 1] = 2
    board[0, :] = 0
    board[:, 0] = 0