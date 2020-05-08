function = ['+', '-', '*', '/','//', '%', '^', 'rnd', 'v', 'rand', '$']
symbols = ['!', '@', '#', '"', '№', ';', ':', '\'', ' ']

def repl(mess):########
    clean_mess = mess
    for symbol in symbols:
        if symbol in clean_mess:
            clean_mess = clean_mess.replace(symbol, '')
    return clean_mess

def dot(param):
    dot = '.'

    if dot in param: 
        return float(param)
    return int(param)########

def operator(message):
    for i in function: 
        if i in message:
            print(i)
            return i#error
            