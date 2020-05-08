def between_markers_2(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    """
    The initial and final markers are always different.
    If there is no initial marker, then the first character should be considered the beginning of a string.
    If there is no final marker, then the last character should be considered the ending of a string.
    If the initial and final markers are missing then simply return the whole string.
    If the final marker comes before the initial marker, then return an empty string.
    """
    if end not in text and begin not in text:
        return text
    elif begin not in text:
        return text[:text.index(end)]
    elif end not in text:
        return text[text.index(begin) + len(begin):]
    elif text.index(begin) > text.index(end):
        return ""
    else:
        return text[text.index(begin) + len(begin):text.index(end)]


print(between_markers_2('What is >apple<', '>', '<'))                   # == "apple", "One sym"
print(between_markers_2("<head><title>My new site</title></head>",
                        "<title>", "</title>"))                         # == "My new site", "HTML"
print(between_markers_2('No[/b] hi', '[b]', '[/b]'))                    # == 'No', 'No opened'
print(between_markers_2('No [b]hi', '[b]', '[/b]'))                     # == 'hi', 'No close'
print(between_markers_2('No hi', '[b]', '[/b]'))                        # == 'No hi', 'No markers at all'
print(between_markers_2('No <hi>', '>', '<'))                           # == '', 'Wrong direction'
