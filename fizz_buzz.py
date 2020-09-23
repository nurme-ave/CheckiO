def checkio(number: int) -> str:

    fizzes_buzzes = {
        3: "Fizz",
        5: "Buzz",
    }

    result = ""

    for key, value in fizzes_buzzes.items():
        if number % key == 0:
            result += value

    return result if result else f"{number} not divisible either by 3 or 5."


print(checkio(3))
print(checkio(5))
print(checkio(15))
print(checkio(7))
print(checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5")
print(checkio(6) == "Fizz", "6 is divisible by 3")
print(checkio(5) == "Buzz", "5 is divisible by 5")
print(checkio(7) == "7", "7 is not divisible by 3 or 5")
