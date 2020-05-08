def correct_sentence(text):
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[0].islower() and text[-1] != '.':
        return text[0].upper() + text[1:] + '.'
    elif text[0].isupper() and text[-1] != '.':
        return text + '.'
    elif text[0].islower() and text[-1] == '.':
        return text[0].upper() + text[1:]
    else:
        return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))
    print(correct_sentence("hi."))
    print(correct_sentence("welcome to New York"))
