from typing import Iterable

"""
Previous solution:

    if len(items) > 1:
        return items[1::] + items[0:1]
    return items
"""


# New solution
def replace_first(items: list) -> Iterable:
    return (items[1::] + items[0:1]) if len(items) > 1 else items


print(replace_first([1, 2, 3, 4]))   # == [2, 3, 4, 1]
print(replace_first([1]))   # == [1]
print(replace_first([]))     # == []
