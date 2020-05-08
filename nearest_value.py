def nearest_value(values: set, one: int):
    values = list(sorted(values))
    if one in values:
        return one
    elif one < values[0]:
        return values[0]
    elif one > values[-1]:
        return values[-1]
    else:
        for i in range(len(values)-1):
            if values[i] < one < values[i + 1]:
                lower, upper = values[i], values[i+1]
                if (one - lower) > (upper - one):
                    return upper
                return lower


print(nearest_value({4, 7, 10, 11, 12, 17}, 9))     # == 10
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))     # == 7
print(nearest_value({4, 8, 10, 11, 12, 17}, 9))     # == 8
print(nearest_value({4, 9, 10, 11, 12, 17}, 9))     # == 9
print(nearest_value({4, 7, 10, 11, 12, 17}, 0))     # == 4
print(nearest_value({4, 7, 10, 11, 12, 17}, 100))   # == 17
print(nearest_value({5, 10, 8, 12, 89, 100}, 7))    # == 8
print(nearest_value({-1, 2, 3}, 0))                 # == -1
