from typing import List
# Task
# Iterate list of numbers and print YES if this number have been seen already


def check_list(list: List[int]):
    nums_set = set()

    for num in list:
        if num in nums_set:
            print("Yes")
        else:
            print("No")

        nums_set.add(num)

check_list([1, 2, 3, 2, 3, 4])