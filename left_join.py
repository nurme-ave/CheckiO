def left_join(phrases):
    """Join strings and replace "right" to "left"."""
    new_string = ''

    for word in phrases:
        new_string += word.replace('right', 'left')
        new_string += ','
    return new_string[:-1]


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop"))) # left,left,left,stop
    print(left_join(("bright aright", "ok")))           # bleft aleft,ok
    print(left_join(("brightness wright",)))            # bleftness wleft
    print(left_join(("enough", "jokes")))               # enough,jokes
