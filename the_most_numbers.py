def most_numbers(*args):
    """
    Find the difference between the maximum and minimum element.
    For an empty argument list, the function should return 0.
    """
    if len(args) > 1:
        if min(args) < 0 and max(args) < 0:
            return -(abs(max(args)) - abs(min(args)))
        return abs(max(args)) - min(args)
    return 0


print((most_numbers(1, 2, 3)))  # , 2, 3), "3-1=2"
print((most_numbers(5, -5)))  # , 10, 3), "5-(-5)=10"
print((most_numbers(10.2, -2.2, 0, 1.1, 0.5)))  # , 12.4, 3), "10.2-(-2.2)=12.4"
print((most_numbers()))  # , 0, 3), "Empty"
print(most_numbers(-0.07))
print(most_numbers(-0.036, -0.11, -0.55, -64))
