def frequency_sort(items):
    """
    Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
    the number of times they appear in elements. If two elements have the same frequency,
    they should end up in the same order as the first appearance in the iterable.
    """
    new_dict = {}
    if len(items) == len(set(items)):
        return items
    else:
        for item in items:
            new_dict[item] = items.count(item)
        result = sorted([[key] * value for key, value in new_dict.items()], key=len, reverse=True)
        return [item for lst in result for item in lst]


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))  # [4, 4, 4, 4, 6, 6, 2, 2]
print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))  # [4, 4, 4, 4, 2, 2, 2, 6, 6]
print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))  # ['bob', 'bob', 'bob', 'carl', 'alex']
print(frequency_sort([17, 99, 42]))  # [17, 99, 42]
print(frequency_sort([]))  # []
print(frequency_sort([1]))  # [1]
