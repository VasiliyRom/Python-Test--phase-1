function = ['+', '-', '*', '/','//', '%', '^', 'rnd', 'v', 'rand', '$']
symbols = ['!', '@', '#', '"', '№', ';', ':', '\'', ' ']

def repl(mess):
    for symbol in symbols:
        if symbol in mess:
            return mess.replace(symbol,'')

def dot(param):
    dot = '.'
    for i in dot:
        if i in param: 
            return float(param)
        else:
            return int(param)

def operator(message):
    for i in function: 
        if i in message:
            print(i)
            return i#error
            