from typing import List


def modify_cities(cities: List[str]):
     if (len(cities) != 6):
         raise ValueError('cites arg should have length 6')
     result = cities.copy()
     result.insert(-1, 'and')

     return result

print(modify_cities(['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']))
