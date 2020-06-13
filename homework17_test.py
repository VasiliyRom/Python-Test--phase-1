def test(value):
    if type(value) != int and type(value) != float:
        raise ValueError
    else:
        return value ** 2
        