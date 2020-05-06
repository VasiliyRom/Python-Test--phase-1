# Task 1
def oops():
    #raise IndexError
    raise KeyError
    
def catch():
    try:
        oops()
    except IndexError:
        print('IndexError')
catch()

#видасть помилку KeyError і покрашиться
#томущо немає except KeyError в конструкції try\except       

# Task 2
def sqa(a, b):
    if b == 0:
        raise ZeroDivisionError
    return (float(a) / float(b)) * (float(a) / float(b))
        
try:
    x = sqa(input(), input())
    print(x) 
except ZeroDivisionError:
    print('На нуль ділити не можна!')
except ValueError as e:
    print(f'{e} - не є числом!')