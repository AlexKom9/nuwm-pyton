from typing import List
from functools import reduce

def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(str(elem) for elem in row))

def analytic(nums: List[int]):
    return [nums, [x for x in nums if x % 2 == 0], [x for x in nums if x % 2 != 0]]

print_matrix(analytic([5, 4, 6, 2, 3, 8]))
