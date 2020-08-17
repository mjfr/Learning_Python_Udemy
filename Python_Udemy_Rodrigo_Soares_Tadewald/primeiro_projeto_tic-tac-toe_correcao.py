# -*- coding: utf-8 -*-

from IPython.display import clear_output
def display_board(board):

    clear_output()
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Which one will you choose? (X/O) ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #Top
    (board[4] == mark and board[5] == mark and board[6] == mark) or  #Middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or  #Bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or  #Left
    (board[8] == mark and board[5] == mark and board[2] == mark) or  #Middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or  #Right
    (board[7] == mark and board[5] == mark and board[3] == mark) or  #Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #Diagonal

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(0, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your play (1-9) ')
    return int(position)

def replay():
    return input('Play again? (Y/N)').lower().startswith('y')

print('Welcome to the worst Tic Tac Toe game ever!')
while True:
    #Setting up the game
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Start!')

    game_on = True
    
    #Player1
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! You won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 2'
    #Player2
        else:
            if turn == 'Player 2':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)
                
                if win_check(board, player2_marker):
                    display_board(board)
                    print('Congratulations! You won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('Draw!')
                        break
                    else:
                        turn = 'Player 1'

    if not replay():
        break