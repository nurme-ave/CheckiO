def backward_string_by_word(text: str) -> str:
    """Return each word backwards."""
    text = list(text.split(" "))
    result = [word[::-1] for word in text]

    return " ".join(result)


print(backward_string_by_word(''))  # == ''
print(backward_string_by_word('world'))     # == 'dlrow'
print(backward_string_by_word('hello world'))   # == 'olleh dlrow'
print(backward_string_by_word('hello   world'))     # == 'olleh   dlrow'
print(backward_string_by_word('welcome to a game'))     # == 'emoclew ot a emag'
