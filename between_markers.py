 def between_markers(text: str, begin: str, end: str) -> str:
    """
    You are given a string and two markers (the initial and final).
    You have to find a substring enclosed between these two markers. But there are a few important conditions:
    - the initial and final markers are always different
    - if there is no initial marker, then the first character should be considered the beginning of a string
    - if there is no final marker, then the last character should be considered the ending of a string
    - if the initial and final markers are missing then simply return the whole string
    - if the final marker comes before the initial marker, then return an empty string
    """
    index_begin, index_end = text.index(begin), text.index(end)
    return text[index_begin + 1 : index_end]


print(between_markers('What is >apple<', '>', '<'))     # == "apple"
print(between_markers('What is [apple]', '[', ']'))     # == "apple"
print(between_markers('What is ><', '>', '<'))          # == ""
print(between_markers('>apple<', '>', '<'))             # == "apple"
