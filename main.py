import numpy as np
import pygame
import sys

ROW_COUNT=6
COLUMN_COUNT=7
BLUE=(0,0,255)
BLACK=(0,0,0)
def create_board():
    board=np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):

    board[row][col]=piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):

    #check all of horizontal location
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

#   check all vertical location
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

#   check positively sloped diagnal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

#   check negatively sloped diagnal
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)

board=create_board()
print_board(board)
game_over=False
turn=0

pygame.init()

SQUARESIZE=100
width=COLUMN_COUNT*SQUARESIZE
height=(ROW_COUNT+1)*SQUARESIZE

size=(width,height)
RADIUS=int((SQUARESIZE/2)-5)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            continue
#     ask for player1 input
#             if turn==0:
#                 col=int(input("Player1 make your selection(0-6):"))
#                 if is_valid_location(board,col):
#                     row=get_next_open_row(board,col)
#                     drop_piece(board,row,col,1)
#
#                     if winning_move(board,1):
#                         print("Player 1 wins")
#                         game_over=True
#                         break
#             #  ask for player 2 input
#             else:
#                 col= int(input("Player2 make your selection(0-6)"))
#                 if is_valid_location(board,col):
#                     row=get_next_open_row(board,col)
#                     drop_piece(board,row,col,2)
            print_board(board)

            turn+=1
            turn=turn%2
