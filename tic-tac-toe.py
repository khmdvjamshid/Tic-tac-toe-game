#Tic-tac-toe game

import os
from random import randint

#display
def display(board):
    print("\t\t*---*---*---*")
    print(f"\t\t| "+board[7]+" | "+board[8]+" | "+board[9]+" |")
    print("\t\t*---*---*---*")
    print(f"\t\t| "+board[4]+" | "+board[5]+" | "+board[6]+" |")
    print("\t\t*---*---*---*")
    print(f"\t\t| "+board[1]+" | "+board[2]+" | "+board[3]+" |")
    print("\t\t*---*---*---*")

#Who starts first
def who_first(player1,player2):
    r = randint(0,1)
    if r == 0:
        return(f'{player1}')
        
    else:
        return(f'{player2}')
    
#players markers
def player_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input(f"{player1} choose your marker 'X' or 'O': ")
        marker = marker.upper()
        
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

#check the position is full or not
def marker_place(board,marker,position):
    board[position] = marker
#checking for the position is full or not
def space_check(board,position):
    if board[position] not in ['X','O']:
        return True
    else:
        pass 
    return False
#Full boar check
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#check who win the game
def win_check(board,marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
           (board[4]  == marker and board[5] == marker and board[6] == marker) or
           (board[7]  == marker and board[8] == marker and board[9] == marker) or
           (board[1]  == marker and board[5] == marker and board[9] == marker) or
           (board[7]  == marker and board[5] == marker and board[3] == marker) or
           (board[1]  == marker and board[4] == marker and board[7] == marker) or
           (board[2]  == marker and board[5] == marker and board[8] == marker) or
           (board[3]  == marker and board[6] == marker and board[9] == marker))

#player choice for the position
def player_choice(board,player1,player2):
    position = 0
    if f'{player1}' in turn:
        while position not in [1,2,3,4,5,6,7,8,9,] or not space_check(board,position):
            position = int(input(f'{player1} please choose a position between 1 to 9: '))
    else:
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
            position = int(input(f'{player2} please choose a position between 1 to 9: '))

    return position

#get answer from user to continue game
def replay():
    ans = input('Do you want play again: Yes(y) or No(n): ')
    if ans[0].lower() == 'y':
        return True
    else:
        pass
    return False 

#main
if __name__ == '__main__':
    print("***---> Welcome To Tic-tac-toe Game! <---***")
    clear = lambda: os.system('cls') #clean's output
    start = True

    while start:
        board = [' ']*10
        display(board)
        player1 = input("Player_1, Enter your name: ")
        player2 = input("Player_2, Enter your name: ")
        clear()
        display(board)
        ply1_marker,ply2_marker = player_marker()

        turn = who_first(player1,player2)
        print(turn + ' will start the game first')

        game_on = True
        while game_on:
               #player1
            if turn == f'{player1}':
                position = player_choice(board,player1,player2)
                marker_place(board,ply1_marker,position)
                clear()
                display(board)
                if win_check(board,ply1_marker):
                    print(f'\t---> Congratulation {player1} Win the game <---')
                    game_on = False
                elif full_board_check(board):
                    print("\t---> TIE GAME <---")
                    game_on = False
                else:
                    turn = player2
                #player2
            else:
                position = player_choice(board,player1,player2)
                marker_place(board,ply2_marker,position)
                clear()
                display(board)
                if win_check(board,ply2_marker):
                    print(f'\t---> Congratulation {player2} Win the game <---')
                    game_on = False  
                elif full_board_check(board):
                    print("\t---> TIE GAME <---")
                    game_on = False   
                else:
                    turn = player1
                  
        start = replay()
        clear()
