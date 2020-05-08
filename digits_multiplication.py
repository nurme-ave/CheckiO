def checkio(number: int) -> int:
    convert_into_list = map(int, str(number))
    total = 1
    for num in convert_into_list:
         if num != 0:
             total *= num
    return total


print(checkio(123405))
print(checkio(123405) == 120)
print(checkio(999) == 729)
print(checkio(1000) == 1)
print(checkio(1111) == 1)
