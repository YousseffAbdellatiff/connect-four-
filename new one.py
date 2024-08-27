import numpy as np
import pygame
COLUMN=7
ROW=6
def create_board():
    board=np.zeros((6,7))
    return board


def drop_peace(board,row,col):
    if is_valid_location(board,col):
        if turn==0:
            board[row][col]=1
        else:
            board[row][col]=2



def is_valid_location(board,col):
    if board[-1][col]==0:
        return True


def get_next_open_row(board,col):
     for row in range(len(board) ):
         if board[row][col]==0:
             return row
def draw_board(board):
    print(np.flip(board,0))

def winning(board,piece):
    # #check Horizontal win
    for c in range (COLUMN-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
              return True
    #check for vertical win
    for c in range(COLUMN):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board [r+3][c]==piece:
                return True
    #check for slope win
    for c in range(COLUMN-3):
        for r in range(ROW - 3):
            if board[r][c] == piece and board[r + 1][c+1] == piece and board[r + 2][c+2] == piece and board[r + 3][
                c+3] == piece:
                return True
    for c in range(COLUMN-3):
        for r in range(3,ROW):
            if board[r][c] == piece and board[r - 1][c+1] == piece and board[r - 2][c+2] == piece and board[r-3][
                c+3] == piece:
                return True



board = create_board()
print(board)

game_over=False
turn=0
while not game_over:

  #Ask for player one input
    if  turn==0:
      col=int(input("player 1 make your selection(0-6):"))
      if is_valid_location(board,col):
          row=get_next_open_row(board,col)
          drop_peace(board,row,col)
          if winning(board,1):
              print("congrats player 1!")
              game_over=True



    else:
      col=int(input("player 2 make your selection"))
      if is_valid_location(board,col):
          row=get_next_open_row(board,col)
          drop_peace(board, row, col)
          if winning(board, 2):
              print("congrats player 2!")
              game_over = True



    draw_board(board)

    turn += 1
    turn = turn % 2


#

