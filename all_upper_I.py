def is_all_upper(text: str) -> bool:
    """
    Check if the string consists of all upper case letters.
    Note: Digits, empty string etc should also return True.
    """
    text = text.strip()
    if not text or text.isdigit():
        return True
    elif text:
        return text.isupper()


print(is_all_upper('ALL UPPER'))                # == True
print(is_all_upper('all lower'))                # == False
print(is_all_upper('mixed UPPER and lower'))    # == False
print(is_all_upper(''))                         # == True
print(is_all_upper("     "))                    # == True
print(is_all_upper("123"))                      # == True
