# 2 different solutions for this task: 'in range' & slice

def checkio1(array):
    """Sums even-indexes elements and multiply at the last."""
    if array:
        return sum([array[i] for i in range(0, len(array), 2)]) * (array[-1])
    return 0


def checkio2(array):
    return 0 if not array else sum(array[::2]) * (array[-1])


print(checkio1([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30")
print(checkio1([1, 3, 5]) == 30, "(1+5)*5=30")
print(checkio1([6]) == 36, "(6)*6=36")
print(checkio1([]) == 0, "An empty array = 0")
