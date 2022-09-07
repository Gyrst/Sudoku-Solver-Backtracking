from logging import exception
import numpy as np
from random import randint


sudoku = [[0, 0, 0, 1, 0, 5, 0, 6, 8],
          [0, 0, 0, 0, 0, 0, 7, 0, 1],
          [9, 0, 1, 0, 0, 0, 0, 3, 0],
          [0, 0, 7, 0, 2, 6, 0, 0, 0],
          [5, 0, 0, 0, 0, 0, 0, 0, 3],
          [0, 0, 0, 8, 7, 0, 4, 0, 0],
          [0, 3, 0, 0, 0, 0, 8, 0, 5],
          [1, 0, 5, 0, 0, 0, 0, 0, 0],
          [7, 9, 0, 4, 0, 1, 0, 0, 0],
          ]


matrix = np.matrix(sudoku)

# Keep in mind that your y-axis is pos[0] and x-axis is pos[]
position = (3,0)

def get_submatrix(matrix, pos):
    x, y = pos[1], pos[0]
    x_mod, y_mod = pos[0] % 3, pos[1] % 3    
    start_x, end_x =x-x_mod, x-x_mod+3
    start_y, end_y = y-y_mod, y-y_mod+3
    return matrix[start_x:end_x, start_y: end_y]

def check_submatrix(matrix, pos):
    submatrix = get_submatrix(pos)
    if np.any(submatrix==0):
        return True
    else:
        unique_values = np.unique(submatrix[0])
        if unique_values.size==9:
            return True
        else: 
            return False

def check_row(matrix, pos):
    row = matrix[pos[1],:]
    print(row)
    if np.any(row==0):
        return True
    else:
        unique_values = np.unique(row)
        if unique_values.size==9:
            return True
        else: 
            return False
    
def check_col(matrix, pos):
    col = matrix[:,pos[0]]
    print(col)
    if np.any(col==0):
        return True
    else:
        unique_values = np.unique(col)
        if unique_values.size==9:
            return True
        else: 
            return False


def check_validity(matrix, pos):
    if check_row(matrix, pos) & check_col(matrix, pos) & check_submatrix(matrix, pos):
        return True
    else:
        return False
    

def assign_value(matrix, pos):
    x, y = pos[1], pos[0]
    if matrix[x,y]==0:
        matrix[x,y] = randint(1,9)
    else:
        raise Exception(ValueError)


# Look at the pseudo-code to implement

def backtracking(matrix, pos):
     for row in matrix:
         for value in row:
            print(value)
            if position==0:
                assign_value(matrix, pos) 
                if check_validity(matrix, pos):
                    return backtracking(matrix, pos)
                else:
                    return False


backtracking(matrix, position)

