import numpy as np


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


position = (4,5)

def get_submatrix(pos):
    x, y = pos[0], pos[1]
    x_mod, y_mod  = pos[0] % 3, pos[1] % 3    
    start_x, end_x =x-x_mod, x-x_mod+3
    start_y, end_y = y-y_mod, y-y_mod+3
    return matrix[start_x:end_x, start_y: end_y]

def check_submatrix(pos):
    submatrix = get_submatrix(pos)
    if np.any(submatrix == 0):
        return True
    else:
        unique_values = np.unique(submatrix[0])
        if unique_values.size == 9:
            return True
        else: 
            return False

def check_row(pos):
    pass

def check_col(pos):
    pass

def assign_value(pos):
    pass

print(check_submatrix(position))
