def checkio(words: str) -> bool:
    """
    You are given a string with words and numbers separated by whitespaces (one space).
    The words contains only letters. This program checks if the string contains three words in succession.
    """

    is_word = []
    to_list = list(words.split())

    if len(to_list) >= 3:
        for word in to_list:
            if word.isalpha():
                is_word.append(word)
                if len(is_word) >= 3:
                    return True
            else:
                is_word = []

    return False


print(checkio("Hello World hello"))  # == True, "Hello"
print(checkio("He is 123 man"))  # == False, "123 man"
print(checkio("1 2 3 4"))  # == False, "Digits"
print(checkio("bla bla bla bla"))  # == True, "Bla Bla"
print(checkio("Hi"))  # == False, "Hi"
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))  # == True
