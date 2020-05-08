def digits_multiplication(number: int) -> int:
    """Calculate the product of the digits excluding any zeroes."""
    convert_into_list = map(int, str(number))
    total = 1
    for num in convert_into_list:
         if num != 0:
             total *= num
    return total


print(digits_multiplication(123405))
print(digits_multiplication(123405) == 120)
print(digits_multiplication(999) == 729)
print(digits_multiplication(1000) == 1)
print(digits_multiplication(1111) == 1)
