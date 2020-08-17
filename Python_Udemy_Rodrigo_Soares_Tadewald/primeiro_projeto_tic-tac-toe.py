# -*- coding: utf-8 -*-

"""
Primeiro projeto do curso de Python do professor Rodrigo Soares Tadewald;
*Instrução: Fazer um jogo da velha para dois jogadores
*Regra: O programa deverá aceitar entrada do jogador e deverá redesenhar o quadro a cada jogada
"""

#Variable area
circle_player = ''
x_player = ''
columns = '  A   B   C'
first_row = {'row1' : '\n1', '1A' : '___', 'aux1' : '|', '1B' : '___', 'aux2' : '|', '1C' : '___'}
second_row = {'row2' : '\n2', '2A' : '___', 'aux3' : '|', '2B' : '___', 'aux4' : '|', '2C' : '___'}
third_row = {'row3' : '\n3', '3A' : '___', 'aux5' : '|', '3B' : '___', 'aux6' : '|', '3C' : '___'}
circle_player = '1º to start is the circle. What is your name? '
x_player = 'You are the X player, what is your name? '
row = 'Chose which row will you place your symbol: '
column = 'Choose which column will your symbol be placed: '
now_playing = ''

def define_player():
    global circle_player
    global x_player
    global now_playing
    print('Welcome to the best Tic Tac Toe app ever made by me! Lord Matheus :3')
    print('First, let us decide who will use which symbol.')
    input(circle_player)
    print('Okay ' + circle_player + ', you will be the first one to place your symbol in the board.')
    input(x_player)
    print('Okay, ' + x_player + ', you are the second one to place your symbol in the board.')
    now_playing = circle_player

def board_draw():
    print(columns + first_row['row1'] + first_row['1A'] + first_row['aux1'] + first_row['1B'] + first_row['aux2'] + first_row['1C'])
    print(second_row['row2'] + second_row['2A'] + second_row['aux3'] + second_row['2B'] + second_row['aux4'] + second_row['2C'])
    print(third_row['row3'] + third_row['3A'] + third_row['aux5'] + third_row['3B'] + third_row['aux6'] + third_row['3C'])

def place_symbol(row, column):
    print('The game started. Type the row and column that you wish to place your symbol!')
    last_playing = ''
    if True:
        if circle_player:
            #print('p1')
            player = '_O_'
        else:
            #print('p2')
            player = '_X_'
        if row == '1':
            #print('p3')
            first_row[row + column] = player
        elif row == '2':
            #print('p4')
            second_row[row + column] = player
        elif row == '3':
            #print('p5')
            third_row[row + column] = player
            #print('p6')
    pass
        
def board_redraw():
    pass

def verify_position():
    pass

def reset_board():
    pass

def start():
    define_player()
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()
    place_symbol(input(row), input(column.upper()))
    board_draw()

start()
#------------------------Test area------------------------
#print('_0_|_1_|_2_\n_3_|_4_|_5_\n 6 | 7 | 8 ')
#       012 456 890
#          3   7
list_board = list(range(0, 9))