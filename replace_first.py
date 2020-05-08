from typing import Iterable


def replace_first(items: list) -> Iterable:

    if len(items) > 1:
        return items[1::] + items[0:1]
    return items


print(replace_first([1, 2, 3, 4]))   # == [2, 3, 4, 1]
print(replace_first([1]))   # == [1]
print(replace_first([]))     # == []
