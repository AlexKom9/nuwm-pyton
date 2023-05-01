from typing import List

# Task
# Check odd and even numbers


def check_list(nums: List[int]):
    uniq_nums = list(set(nums))

    return [uniq_nums, [x for x in uniq_nums if x % 2 == 0], [x for x in uniq_nums if x % 2 != 0]]


print(check_list([12, 19, 8, 22, 11, 15, 9, 12, 13, 22, 28, 33, 19, 11]))