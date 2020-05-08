def number_length(a: int) -> int:
    """Return the length of the given number."""
    return len(str(a))


print(number_length(10))    # == 2
print(number_length(0))     # == 1
print(number_length(4))     # == 1
print(number_length(44))    # == 2
