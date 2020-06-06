def second_index(text: str, symbol: str) -> [int, None]:
    """
    Returns the second index of a symbol in a given text

    Previous solution:
    
    pos = [pos for pos, char in enumerate(text) if char == symbol]
    if len(pos) >= 2:
        return pos[1]
    return None
    """
    
    # New solution
    pos = [pos for pos, char in enumerate(text) if char == symbol]
    return pos[1] if len(pos) >= 2 else None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))
    print(second_index("find the river", "e"))
    print(second_index("hi", " "))
    print(second_index("hi mayor", " "))
    print(second_index("hi mr Mayor", " "))
    print(second_index("three occurrences", "r"))
