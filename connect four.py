#Name:Youssef Abdellatif   matriculation number:12306410
#This file includes the full implementation of connect 4 game
import random
from abc import ABC, abstractmethod
import sys
# import pygame



#fixed number of row and columns
ROWS = 6
COLUMNS = 7




def board_creation():
    global board
    board = []


    for c in range(ROWS):
        row = []
        for r in range(COLUMNS):
            row.append(" ")
        board.append(row)
    return board

def draw_board(board):
    for row in board:
        joined_row = "|".join(row)
        separator = "--" * (COLUMNS )
        print(joined_row)
        print(separator)


#to clean the board whenever the user decide to restart the game
def board_cleaning():
    for c in range(COLUMNS):
        for r in range(ROWS):
            board[r][c]=" "





class UserSelection():


    def __init__(self):
        self.default= RandomPlayer()

    def userchoice(self,gamemode):
        if gamemode == 1:
            self.default=FriendPlayer()
        elif gamemode == 2:

            self.default=RandomPlayer()









#creating the general or the main class to assure the using of STRATEGY desing pattern

class GameMode(ABC):

    @abstractmethod
    def is_valid(board, col):
        raise NotImplementedError()

    @abstractmethod
    def drop_to_which_row(board, col):
        raise NotImplementedError()
    @abstractmethod
    def winning_move(board, piece):
        raise NotImplementedError()
    @abstractmethod
    def drop_symbol(board, row, column, symbol):
        raise NotImplementedError()





class FriendPlayer(GameMode):
   column = "friend player"

   # to check if the column selected is valid or no

   def is_valid(board, col):
        for r in range(ROWS):
            if board[r][col] == " ":
                return True
        return False

   # to return the first empty cell looping from down upword
   @staticmethod
   def drop_to_which_row(board, col):
       for r in range(ROWS - 1, -1, -1):
           if board[r][col] == " ":
               return r

   # to check the winning cases
   @staticmethod
   def winning_move(board, piece):
        # check horizontal win
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # check vertical win
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # check slope win #1
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True
        # check slope win #2
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True

   # to drop the cell to the first empty cell returned from drop to which row function
   @staticmethod
   def drop_symbol(board, row, column, symbol):
       board[row][column] = symbol




class RandomPlayer(GameMode):

   column="random player"
    #to check if the column selected is valid or no
   @staticmethod
   def is_valid(board, col):
        for r in range(ROWS):
            if board[r][col] == " ":
                return True
        return False
   #to return the first empty cell looping from down upword
   @staticmethod
   def drop_to_which_row(board, col):
       for r in range(ROWS - 1, -1, -1):
           if board[r][col] == " ":
               return r
   #to check the winning cases
   @staticmethod
   def winning_move(board, piece):
        # check horizontal win
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # check vertical win
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # check + slope win
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True
        # check - slope win #2
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
   # to drop the cell to the first empty cell returned from drop to which row function
   @staticmethod
   def drop_symbol(board, row, column, symbol):
       board[row][column] = symbol





#the actual game procedures
def game_process():

    game_over = False


    while not game_over:
            turn = 0
            board = board_creation()
            while not game_over:


                            if turn == 0:

                                column = int(input("Player 1 select column between (0-6): "))
                                while column > 6:
                                    column = int(input("invalid selection ! select between 0 and 6  "))

                                if UserSelection().default.is_valid(board, column):
                                    row = UserSelection().default.drop_to_which_row(board, column)
                                    UserSelection().default.drop_symbol(board, row, column, "X")


                            else:
                               ##in case player 2's turn i have to check whether the user has selected to play with his friend or against the computer in case of computer i have to select random column for the computer to play its turn
                                if userchose.default.column=="friend player":
                                    column = int(input("Player 2 select column between (0-6): "))
                                    while column > 6:
                                        column = int(input("invalid selection ! select between 0 and 6  "))
                                else: column=random.randint(0,6)


                                if UserSelection().default.is_valid(board, column):
                                    row = UserSelection().default.drop_to_which_row(board, column)
                                    UserSelection().default.drop_symbol(board, row, column, "O")

                            draw_board(board)

                            if UserSelection().default.winning_move(board, "X"):

                                game_over = True
                                print("Player 1 wins!")
                            elif UserSelection().default.winning_move(board, "O"):

                                game_over = True
                                print("Player 2 wins!")



                            turn += 1
                            turn %= 2



#storing whether the user wants to start the game or no

game_start=input("type yes to start the game :")
while game_start != "yes":
    game_start=input("please type yes ")


#storing which mode does the user want to play in
choices=[1,2]
#
game_mode = int(input("Press 1 to play With your friend OR press 2 to play with a Random Player "))
while game_mode not in choices:
    game_mode = int(input("Please choose Game Mode 1 or 2 : "))

userchose=UserSelection()
userchose.userchoice(game_mode)



##to start the game when the user decide to
if game_start=="yes":
    game_process()

# a loop to restart the game infinite number of times if the user wants to play again several times
restart=False
while not restart:

    game_restat=input("type \"yes\" to restart the game OR \"no\" to exit ")
    if game_restat == "yes":
        game_mode = int(input("Press 1 to play With your friend OR press 2 to play with a Random Player "))
        while game_mode not in choices:
            game_mode = int(input("Please choose Game Mode 1 or 2 : "))
        userchose = UserSelection()
        userchose.userchoice(game_mode)
        board_cleaning()
        game_process()
    else:
        restart=True



