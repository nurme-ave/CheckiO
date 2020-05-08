def three_words(words: str) -> bool:
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


print(three_words("Hello World hello"))  # == True, "Hello"
print(three_words("He is 123 man"))  # == False, "123 man"
print(three_words("1 2 3 4"))  # == False, "Digits"
print(three_words("bla bla bla bla"))  # == True, "Bla Bla"
print(three_words("Hi"))  # == False, "Hi"
print(three_words("one two 3 four five six 7 eight 9 ten eleven 12"))  # == True
