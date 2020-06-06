def is_all_upper(text: str) -> bool:
    """
    Previous solution:
    
    text = text.strip()
    if not text or text.isdigit():
        return True
    elif text:
        return text.isupper()
    """

    # New solution
    text = text.strip()
    return True if not text or text.isdigit() else text.isupper()


print(is_all_upper('ALL UPPER'))                # == True
print(is_all_upper('all lower'))                # == False
print(is_all_upper('mixed UPPER and lower'))    # == False
print(is_all_upper(''))                         # == True
print(is_all_upper("     "))                    # == True
print(is_all_upper("123"))                      # == True
