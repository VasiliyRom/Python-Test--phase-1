def count_lines(name):
    if type(name) != str:
        raise ValueError
    with open(f'{name}', "r") as f:
        len_lines = len(f.readlines ())
        return len_lines


def count_chars(name):
    if type(name) != str:
        raise ValueError
    with open(f'{name}', "r") as f:
        chars = len(f.read())
        return chars

    
def test(name):
    if type(name) != str:
        raise ValueError
    lines = count_lines(name)
    cou_chars = count_chars(name)
    return f'Кількість рядків: {lines}, Кількість символів: {cou_chars}'