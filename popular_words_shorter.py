def popular_words(text: str, words: list) -> dict:
    """
    Note: I used a dictionary comprehension here which makes the solution significally shorter.
    Determine the popularity of certain words in the text.
    Conditions:
    - the words should be sought in all registers
    - the search words are always indicated in the lowercase
    - if the word isn’t found even once, it has to be returned in the dictionary with 0 (zero) value
    """
    text = text.lower().split()
    return {word: text.count(word) if word in words else 0 for word in words}


print(popular_words('''
                    It's flying from somewhere
                    As fast as it can
                    I couldn't keep up with it
                    Not if I ran
                    ''',
                    ["it's", "ran", "i"]))

# == {"it's":1,"ran":1,"i":2}

print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

# == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
