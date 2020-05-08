def checkio(numbers_array: tuple) -> list:
    """Sort the numbers by their absolute value and return them as the original list."""
    return sorted(numbers_array, key=abs)


print(checkio((-20, -5, 10, 15)))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))
