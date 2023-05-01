from typing import List


def recalculate_prices(prices: List[int]):
    if not len(prices):
        return []

    price = prices[0]

    def getByIndex(list: List[int], index: int):
        return list[index] if index < len(list) else 0

    discount_index = 1
    discount = getByIndex(prices, discount_index)

    while discount_index < len(prices) and (discount > price or discount == 0):
        discount_index += 1
        discount = getByIndex(prices, discount_index)

    return [price - discount, *recalculate_prices(prices[1:])]


print(recalculate_prices([8, 4, 6, 2, 3]))
print(recalculate_prices([1,2,3,4,5]))
print(recalculate_prices([10,1,1,6]))
