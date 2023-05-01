import copy
from typing import List
from functools import reduce

def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(str(elem) for elem in row))

def symmetry(matrix: List[List[int]]):
    _matrix = copy.deepcopy(matrix)

    for i in range(len(_matrix)):
        _matrix[i][i] = round(_matrix[i][i] / 1.0, 1)

        for j in range(i + 1, len(_matrix[i])):
            symmetry_sum_half = round((_matrix[i][j] + _matrix[j][i]) / 2, 1)

            _matrix[i][j] = symmetry_sum_half
            _matrix[j][i] = symmetry_sum_half
    
    return _matrix


print_matrix(symmetry([
                [0,1,2,3,4,5],
                [5,4,3,2,1,0],
                [0,1,2,3,4,5],
                [5,4,3,2,1,0],
                [0,1,2,3,4,5],
                [5,4,3,2,1,0],
                ])
    )
