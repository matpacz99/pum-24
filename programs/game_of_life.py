import random
from IPython.display import clear_output
import time
import argparse
import os

def get_empty_board(n): # return n x n table of dead cells (a list of lists)
    board = []
    for i in range(n):
        board.append([0]*n)
    return board

def print_board(grid): # print the table
    for a in grid:
        print(a)

def get_random_board(n): # return n x n table where each cell is alive with probability 0.2
    board = get_empty_board(n)
    for i in range(n):
        for j in range(n):
            random_element = random.random()
            if random_element <= args.prob:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board

def add_glider(board): # return a board with a glider
    board[0][2] = 1
    board [1][2] = 1
    board[2][2] = 1
    board[2][1] = 1
    board[1][0] = 1
    board[0][0] = 0
    board[1][1] = 0
    board[2][0] = 0
    return board

def count_live_neighbors(board, x, y): # return the number of live neighbors of cell x, y
    nb = 0
    list_x = [x-1, x, x+1]
    list_y = [y-1, y, y+1]
    if (y > 0 and y < (len(board)-1) and x > 0 and x < (len(board[0])-1)):
        for i in range(3):
            for j in range(3):
                nb += board[list_y[i]][list_x[j]]
        nb += -board[list_y[1]][list_x[1]]
    if y == 0:
        if x == 0:
            for i in range(2):
                for j in range(2):
                    nb += board[list_y[i+1]][list_x[j+1]]
            nb += -board[list_y[1]][list_x[1]]
        elif x == len(board[0])-1:
            for i in range(2):
                for j in range(2):
                    nb += board[list_y[i+1]][list_x[j]]
            nb += -board[list_y[1]][list_x[1]]
        else:
            for i in range(2):
                for j in range(3):
                    nb += board[list_y[i+1]][list_x[j]]
            nb += -board[list_y[1]][list_x[1]]
    elif y == len(board)-1:
        if x == 0:
            for i in range(2):
                for j in range(2):
                    nb += board[list_y[i]][list_x[j+1]]
            nb += -board[list_y[1]][list_x[1]]
        elif x == len(board[0])-1:
            for i in range(2):
                for j in range(2):
                    nb += board[list_y[i]][list_x[j]]
            nb += -board[list_y[1]][list_x[1]]
        else:
            for i in range(2):
                for j in range(3):
                    nb += board[list_y[i]][list_x[j]]
            nb += -board[list_y[1]][list_x[1]]
    else:
        if x == 0:
            for i in range(3):
                for j in range(2):
                    nb += board[list_y[i]][list_x[j+1]]
            nb += -board[list_y[1]][list_x[1]]  
        if x == len(board[0])-1:
            for i in range(3):
                for j in range(2):
                    nb += board[list_y[i]][list_x[j]]
            nb += -board[list_y[1]][list_x[1]]  
    return nb

def step(board): # return board at the next timestep
    board1 = get_empty_board(len(board))
    for k in range(len(board)):
        for m in range(len(board[0])):
            amount = count_live_neighbors(board, m, k)
            if board[k][m] == 0:
                if amount == 3:
                    board1[k][m] = 1
            if board[k][m] == 1:
                if amount == 2:
                    board1[k][m] = 1
                elif amount == 3:
                    board1[k][m] = 1
                else:
                    board1[k][m] = 0
    return board1

def run_game_of_life(board):
    for _ in range(args.steps):    # run for 20 steps
        os.system('clear')    # clear the output
        print_board(board)          # print the board
        time.sleep(0.5)               # wait for half a second
        new_board = step(board)     # generate the next step
        board = new_board 

parser = argparse.ArgumentParser()
parser.add_argument("--size", "-s", type=int, default=20, help="Size of the board")
parser.add_argument("--prob", "-p", type=float, default=0.3, help="Probability of a cell being alive")
parser.add_argument("--steps", "-n", type=int, default=40, help="Number of steps to run the simulation for")

args = parser.parse_args()
args.size   # this will contain the size of the board
args.prob   # this will contain the probability of a cell being alive
args.steps  # this will contain the number of steps to run the simulation for

# Specify the table
table = get_random_board(args.size)
#table = get_empty_board(10)
#table = add_glider(table)
run_game_of_life(table) # Start the game