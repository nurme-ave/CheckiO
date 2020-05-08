def backward_string(val: str) -> str:
    """Reverse the string."""
    return val[::-1] if val else val



print(backward_string('val'))   # == 'lav'
print(backward_string(''))  # == ''
print(backward_string('ohho'))  # == 'ohho'
print(backward_string('123456789'))     # == '987654321'
