def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    index_begin, index_end = text.index(begin), text.index(end)
    if index_end - index_end == 1:
        return '" "'
    return text[index_begin + 1 : index_end]


print(between_markers('What is >apple<', '>', '<'))     # == "apple"
print(between_markers('What is [apple]', '[', ']'))     # == "apple"
print(between_markers('What is ><', '>', '<'))          # == ""
print(between_markers('>apple<', '>', '<'))             # == "apple"
