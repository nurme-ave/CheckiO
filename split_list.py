from math import ceil


def split_list(items: list) -> list:
    """
    Split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements.
    If it has no elements, then two empty arrays should be returned.
    """
    if len(items) % 2 == 0:
        half_of_items = len(items) // 2
        first_half, second_half = items[:half_of_items], items[half_of_items:]
        return [first_half, second_half]
    else:
        more_items = ceil(len(items) / 2)
        first_part, second_part = items[:more_items], items[more_items:]
        return [first_part, second_part]


print(split_list([1, 2, 3, 4, 5, 6]))   # == [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))     # == [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))   # == [[1, 2, 3], [4, 5]]
print(split_list([1]))  # == [[1], []]
print(split_list([]))   # == [[], []]
