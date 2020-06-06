def all_the_same(elements) -> bool:
    """Check if all elements in the given list are equal.
    
    Previous version:
    if len(elements) < 1:
        return True
    return len(elements) == elements.count(elements[0])
    """
    
    # New version:
    return True if len(elements) < 1 else (len(elements) == elements.count(elements[0]))


print(all_the_same([1, 1, 1]))  # == True
print(all_the_same([1, 2, 1]))  # == False
print(all_the_same(['a', 'a', 'a']))    # == True
print(all_the_same([])) # == True
print(all_the_same([1]))    # == True
