#!/bin/python3
# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

# A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.

# The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :
# Complete the queensAttack function in the editor below. It should return an integer that describes the number of squares the queen can attack.

# queensAttack has the following parameters:
# - n: an integer, the number of rows and columns in the board
# - k: an integer, the number of obstacles on the board
# - r_q: integer, the row number of the queen's position
# - c_q: integer, the column number of the queen's position
# - obstacles: a two dimensional array of integers where each element is an array of  integers, the row and column of an obstacle


import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    top = n - r_q
    bottom = r_q - 1
    right = n - c_q
    left = c_q - 1
    top_right = min(top, right)
    top_left = min(top, left)
    bot_right = min(bottom, right)
    bot_left = min(bottom, left)
    
    for obs in obstacles:
        diff_r = r_q - obs[0]
        diff_c = c_q - obs[1]
        if r_q == obs[0]:
            # same row:
            if diff_c > 0:
                # on the left:
                left = min(left, diff_c - 1)
            else:
                # on the right
                right = min(right, abs(diff_c) - 1)
        elif c_q  == obs[1]:
            if diff_r > 0:
                # on bottom
                bottom = min(bottom, diff_r - 1)
            else:
                # on top
                top = min(top, abs(diff_r) - 1)
        elif diff_r == diff_c:
            if diff_r > 0:
                # on bottom left
                bot_left = min(bot_left, diff_r - 1)
            else:
                # on top right
                top_right = min(top_right, abs(diff_r) - 1)
        elif abs(diff_r) == abs(diff_c):
            if diff_r > 0:
                # on bottom right
                bot_right = min(bot_right, diff_r - 1)
            else:
                # on top left
                top_left = min(top_left, abs(diff_r) - 1)

    return top + bottom + right + left + top_right + top_left + bot_right + bot_left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
