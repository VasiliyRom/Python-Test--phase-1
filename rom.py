items_list = [64, 128, 256]

def oops():  
    i = items_list[4]
    raise KeyError
    return i
    
def catch():
    try:
        x = oops1()
        print(x)
    except IndexError:
        print('Індекс неіснує')
    except KeyError:   
        print('Індекс')
catch()