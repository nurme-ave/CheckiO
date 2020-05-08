
def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


print(checkio(3))
print(checkio(5))
print(checkio(15))
print(checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5")
print(checkio(6) == "Fizz", "6 is divisible by 3")
print(checkio(5) == "Buzz", "5 is divisible by 5")
print(checkio(7) == "7", "7 is not divisible by 3 or 5")
