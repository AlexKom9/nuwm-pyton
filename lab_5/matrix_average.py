from typing import List
from functools import reduce

def average(matrix: List[List[int]]):
    return reduce(lambda acc, row: acc + (sum(row) / len(row)), matrix, 0)

print(average([[0,1,2,3,4,5], [0,1,2,3,4,5], [0,1,2,3,4,5], [0,1,2,3,4,5]]))
