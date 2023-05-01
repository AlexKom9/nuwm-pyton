import copy
from typing import List

# Task
# Create new list which is merge of 2 others within only uniq elements

def check_list(list_a: List[int], list_b: List[int]):
    a_set = set(list_a)
    b_set = set(list_b)

    result = list(a_set.union(b_set))

    return [len(result), result]

print(check_list([1, 2, 3, 2, 1, 6], [2, 4, 1, 8, 9]))