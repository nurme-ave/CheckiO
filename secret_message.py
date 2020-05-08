
def find_message(text: str) -> str:
    """Gather all capital letters in one word in the order that they appear in the text."""
    result = ""
    for char in text:
        if char.isupper():
            result += char
    return result


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
print(find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello")
print(find_message("hello world!") == "", "Nothing")
print(find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals")
