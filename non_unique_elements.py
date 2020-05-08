"""
Some hints
You can use list.count(element) method for counting.
Create new list with non-unique elements
Loop over original list
"""


def non_unique_elements(data: list) -> list:
    if len(data) == len(set(data)):
        return []
    else:
        result = [elem for elem in data if data.count(elem) > 1]
        return result


print(non_unique_elements([1, 2, 3, 1, 3]))         # == [1, 3, 1, 3]
print(non_unique_elements([1, 2, 3, 4, 5]))         # == []
print(non_unique_elements([5, 5, 5, 5, 5]))         # == [5, 5, 5, 5, 5]
print(non_unique_elements([10, 9, 10, 10, 9, 8]))   # == [10, 9, 10, 10, 9]
print(non_unique_elements([10, 20, 30, 10]))        # == [10,10]
