
def split_pairs(a):
    newlst = []
    split_in_pairs = [a[i:i + 2] for i in range(0, len(a), 2)]

    for elem in split_in_pairs:
        if len(elem) != 2:
            newlst.append(''.join(elem + '_'))
        else:
            newlst.append(elem)

    return newlst


print(split_pairs('abcd'))    # == ['ab', 'cd']
print(split_pairs('abc'))     # == ['ab', 'c_']
print(split_pairs('abcdf'))   # == ['ab', 'cd', 'f_']
print(split_pairs('a'))       # == ['a_']
print(split_pairs(''))        # == []
