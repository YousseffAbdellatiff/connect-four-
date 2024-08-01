import numpy as np
import pygame
import sys
import math
ROWS = 6
COLUMNS = 7
GRAY = (150, 150, 150)
CIRLCES_GARY=(100,100,100)
RED=(230,0,0)
YELLOW=(255,255,0)
BLACK=(0,0,0)

# Function to create a matrix (6*7) of zeros
board =[]


def boardcreation():
    board = np.zeros((6, 7))
    return board





board = boardcreation()
# def boardcreation():
#     for  row in range(ROWS):
#         row=[]
#         for columns in range(COLUMNS):
#             row.append("1 ")
#         board.append(row)
#     return board
# #
# board=boardcreation()

print(board)
# def consoledisplay():
#     for row in board:
#      joined="|".join(row)
#      separator="-"*(COLUMNS*2)
#      print(joined)
#      print(separator)
#
# consoledisplay()

print(board[0][0])
# Function to check if there are still free places for the user to insert in the column he chose
def is_valid(board, col):

  for r in range(ROWS):
        return board[r][col]==0


# to know to which element will the user input be added
def drop_to_which_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    # check horizontal win
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # check vertical win
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # check slope win #1
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True
    # check slope win #1
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
          pygame.draw.rect(screen, GRAY, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
          if board[r][c]==0:
              pygame.draw.circle(screen, CIRLCES_GARY,
                                 (c * SQUARESIZE + SQUARESIZE / 2, r * SQUARESIZE + SQUARESIZE / 2 + SQUARESIZE),
                                 RADIUS)

          elif board[r][c]==1:
            pygame.draw.circle(screen,RED,(c*SQUARESIZE+SQUARESIZE/2,r*SQUARESIZE+SQUARESIZE/2 +SQUARESIZE),RADIUS)
          else:
              pygame.draw.circle(screen, YELLOW,
                                 (c * SQUARESIZE + SQUARESIZE / 2, r * SQUARESIZE + SQUARESIZE / 2 + SQUARESIZE),
                                 RADIUS)

def dropsympol(board,row,column,sympol):
    board[row][column]=sympol

SQUARESIZE=100
WIDTH=COLUMNS*SQUARESIZE
HEIGHT=SQUARESIZE*ROWS+SQUARESIZE
SIZE=(WIDTH,HEIGHT)
screen=pygame.display.set_mode(SIZE)
RADIUS=SQUARESIZE/2 -5
draw_board(board)
pygame.display.update()

gameover=False
whichplayer=0
while  not gameover :


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                  sys.exit()
            if event.type==pygame.MOUSEMOTION:
                 pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                 posx=event.pos[0]
                 if whichplayer==0:
                        pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
                 else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)



            if event.type == pygame.MOUSEBUTTONDOWN:


                if whichplayer == 0:
                     posx=event.pos[0]
                     column= int(math.floor(posx//100))
                     while column  not in range(column+1) :
                         print("invalid columne please select again")
                         column = int(math.floor(posx // 100))

                     if is_valid(board,column):
                         row=drop_to_which_row(board,column)
                         dropsympol(board,row,column,1)
                         if winning_move(board, 1):

                             print("CONGRATS!!! PLAYER 1 ")
                             draw_board(board)
                             pygame.display.update()
                             play_again = input("Do you want to play again? (yes/no): ")
                             if play_again.lower() == "yes":
                                 board = boardcreation()
                                 draw_board(board)
                                 pygame.display.update()
                             else:
                                 gameover=True











                else:
                    posx = event.pos[0]
                    column= int(math.floor(posx//100))
                    if is_valid(board,column):
                         row=drop_to_which_row(board,column)
                         dropsympol(board,row,column,2)
                         if winning_move(board, 2):
                             print("CONGRATS!!! PLAYER 2 ")
                             draw_board(board)
                             pygame.display.update()
                             if play_again.lower() == "yes":
                                 board = boardcreation()
                                 draw_board(board)
                                 pygame.display.update()
                             else:
                                 gameover=True




                draw_board(board)
                pygame.display.update()
                print(board)
                whichplayer+=1
                whichplayer=whichplayer%2







#######################################################################################################################################################################################################
# import numpy as np
# import pygame
# import sys
# import math
# ROWS = 6
# COLUMNS = 7
# GRAY = (150, 150, 150)
# CIRLCES_GARY=(100,100,100)
# RED=(230,0,0)
# YELLOW=(255,255,0)
# BLACK=(0,0,0)
#
# # Function to create a matrix (6*7) of zeros
# def boardcreation():
#     board = np.zeros((6, 7))
#     return board
# board=boardcreation()
#
# # Function to check if there are still free places for the user to insert in the column he chose
# def is_valid(board, col):
#
#   for r in range(ROWS):
#         return board[r][col]==0
#
#
# # to know to which element will the user input be added
# def drop_to_which_row(board, col):
#     for r in range(ROWS - 1, -1, -1):
#         if board[r][col] == 0:
#             return r
#
#
# def winning_move(board, piece):
#     # check horizontal win
#     for c in range(COLUMNS-3):
#         for r in range(ROWS):
#             if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
#                 return True
#
#     # check vertical win
#     for c in range(COLUMNS):
#         for r in range(ROWS - 3):
#             if board[r][c] == piece and board[r + 1][c] == piece and board[r + 1][c] == piece and board[r + 3][
#                 c] == piece:
#                 return True
#
#     # check slope win #1
#     for c in range(COLUMNS - 3):
#         for r in range(ROWS - 3):
#             if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
#                     board[r + 3][c + 3] == piece:
#                 return True
#     # check slope win #1
#     for c in range(COLUMNS - 3):
#         for r in range(3, ROWS):
#             if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
#                     board[r - 3][c + 3] == piece:
#                 return True
#
# def draw_board(board):
#     for c in range(COLUMNS):
#         for r in range(ROWS):
#           pygame.draw.rect(screen, GRAY, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
#           if board[r][c]==0:
#               pygame.draw.circle(screen, CIRLCES_GARY,
#                                  (c * SQUARESIZE + SQUARESIZE / 2, r * SQUARESIZE + SQUARESIZE / 2 + SQUARESIZE),
#                                  RADIUS)
#
#           elif board[r][c]==1:
#             pygame.draw.circle(screen,RED,(c*SQUARESIZE+SQUARESIZE/2,r*SQUARESIZE+SQUARESIZE/2 +SQUARESIZE),RADIUS)
#           else:
#               pygame.draw.circle(screen, YELLOW,
#                                  (c * SQUARESIZE + SQUARESIZE / 2, r * SQUARESIZE + SQUARESIZE / 2 + SQUARESIZE),
#                                  RADIUS)
#
# def dropsympol(board,row,column,sympol):
#     board[row][column]=sympol
#
# SQUARESIZE=100
# WIDTH=COLUMNS*SQUARESIZE
# HEIGHT=SQUARESIZE*ROWS+SQUARESIZE
# SIZE=(WIDTH,HEIGHT)
# screen=pygame.display.set_mode(SIZE)
# RADIUS=SQUARESIZE/2 -5
# draw_board(board)
# pygame.display.update()
# #
#
# game_mode = input("Do You Want To Play Against a Random Player/Your friend: ")
# while game_mode not in ["my friend", "friend", "random player", "random"]:
#   game_mode = input("Please choose 'my friend' or 'random player': ")
# #
# #
#
#
# gameover=False
# whichplayer=0
# while  not gameover :
#
#
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                   sys.exit()
#             if event.type==pygame.MOUSEMOTION:
#                  pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
#                  posx=event.pos[0]
#                  if whichplayer==0:
#                         pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
#                  else:
#                         pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
#
#
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#
#                 if game_mode.lower() == "my friend" or game_mode.lower() == "friend":
#                         if whichplayer == 0:
#                              posx=event.pos[0]
#                              column= int(math.floor(posx//100))
#                              while column  not in range(column+1) :
#                                  print("invalid columne please select again")
#                                  column = int(math.floor(posx // 100))
#
#                              if is_valid(board,column):
#                                  row=drop_to_which_row(board,column)
#                                  dropsympol(board,row,column,1)
#                                  if winning_move(board, 1):
#
#                                      print("CONGRATS!!! PLAYER 1 ")
#                                      play_again = input("Do you want to play again? (yes/no): ")
#                                      if play_again.lower() == "yes":
#                                          board = boardcreation()
#                                          draw_board(board)
#                                          pygame.display.update()
#                                      else:
#                                          sys.exit()
#
#
#
#
#
#
#
#
#
#
#
#                         else:
#                             posx = event.pos[0]
#                             column= int(math.floor(posx//100))
#                             if is_valid(board,column):
#                                  row=drop_to_which_row(board,column)
#                                  dropsympol(board,row,column,2)
#                                  if winning_move(board, 2):
#                                      print("CONGRATS!!! PLAYER 2 ")
#                                      if play_again.lower() == "yes":
#                                          board = boardcreation()
#                                          draw_board(board)
#                                          pygame.display.update()
#                                      else:
#                                          sys.exit()
#
#
#
#
#                         draw_board(board)
#                         pygame.display.update()
#                         print(board)
#                         whichplayer+=1
#                         whichplayer=whichplayer%2
#                 elif game_mode.lower() == "random player" or game_mode.lower() == "random":
#                         if whichplayer == 0:
#                             posx = event.pos[0]
#                             column = int(math.floor(posx // 100))
#                             while column not in range(column + 1):
#                                 print("invalid columne please select again")
#                                 column = int(math.floor(posx // 100))
#
#                             if is_valid(board, column):
#                                 row = drop_to_which_row(board, column)
#                                 dropsympol(board, row, column, 1)
#                                 if winning_move(board, 1):
#                                     print("CONGRATS!!! PLAYER 1 ")
#                                     play_again = input("Do you want to play again? (yes/no): ")
#                                     if play_again.lower() == "yes":
#                                         board = boardcreation()
#                                         draw_board(board)
#                                         pygame.display.update()
#                                     else:
#                                         sys.exit()
#                                 whichplayer += 1
#                                 whichplayer = whichplayer % 2
#
#                         else:
#                             column = int(random.randrange(0, COLUMNS))
#
#                             if is_valid(board, column):
#                                 row = drop_to_which_row(board, column)
#                                 dropsympol(board, row, column, 2)
#                                 if winning_move(board, 2):
#                                     print("CONGRATS!!! PLAYER 2 ")
#                                     if play_again.lower() == "yes":
#                                         board = boardcreation()
#                                         draw_board(board)
#                                         pygame.display.update()
#                                     else:
#                                         sys.exit()
#                                 whichplayer += 1
#                                 whichplayer = whichplayer % 2
#
#                         draw_board(board)
#                         pygame.display.update()


####################################################################################################################################################################################################################
