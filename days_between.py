from datetime import date


def days_diff(a, b):
    """Find the difference in days between the given dates."""
    start_date = date(*a)
    end_date = date(*b)
    difference = end_date - start_date
    return abs(difference.days)


print(days_diff((1982, 4, 19), (1982, 4, 22)))  # == 3
print(days_diff((2014, 1, 1), (2014, 8, 27)))   # == 238
print(days_diff((2014, 8, 27), (2014, 1, 1)))   # == 238
