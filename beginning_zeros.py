def beginning_zeros(number: str) -> int:
    """Calculate how many zero digits ("0") are at the beginning of the given string."""
    count = 0
    for char in number:
        if char == '0':
            count += 1
        else:
            break
    return count


print(beginning_zeros('100'))   # == 0
print(beginning_zeros('001'))   # == 2
print(beginning_zeros('100100'))    # == 0
print(beginning_zeros('001001'))    # == 2
print(beginning_zeros('012345679'))     # == 1
print(beginning_zeros('0000'))      # == 4
