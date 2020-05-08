from datetime import date


def days_diff(a, b):
    start_date = date(a[0], a[1], a[2])
    end_date = date(b[0], b[1], b[2])
    difference = end_date - start_date
    return abs(difference.days)


print(days_diff((1982, 4, 19), (1982, 4, 22)))  # == 3
print(days_diff((2014, 1, 1), (2014, 8, 27)))   # == 238
print(days_diff((2014, 8, 27), (2014, 1, 1)))   # == 238
