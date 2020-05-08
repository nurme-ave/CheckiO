def end_zeros(num: int) -> int:
    """Calculate how many zeros a given number has at the end."""
    count = 0
    num = str(num)
    for n in num[::-1]:
        if n == '0':
            count += 1
        else:
            break

    return count


print(end_zeros(0))         # == 1
print(end_zeros(1))         # == 0
print(end_zeros(10))        # == 1
print(end_zeros(101))       # == 0
print(end_zeros(245))       # == 0
print(end_zeros(100100))    # == 2
