def count_digits(text: str) -> int:
    """Count the number of digits in a given string."""
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count


print(count_digits('hi'))   # 0
print(count_digits('who is 1st here'))  # 1
print(count_digits('my numbers is 2'))  # 1
print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))    # 8
print(count_digits('5 plus 6 is'))  # 2
print(count_digits(''))   # 0
