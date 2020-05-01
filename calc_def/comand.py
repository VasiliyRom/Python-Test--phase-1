import random
import math


oper_dict = {
    '+': '{x} {oper} {y} = {result}',
    '-': '{x} - {y} = {result}',
    '*': '{x} * {y} = {result}',
    '/': '{x} / {y} = {result}',
    '//': '{x} // {y} = {result}',
    '%': '{x} % {y} = {result}', 
    '**': '{x} В {y} степінь = {result}',
    'rnd':  '{x}, {y} знаків після коми = {result}', 
    'v': 'V{x} = {result}',
    'rand': 'Випадкове число від {x} до {y} = {result}',
    '$': 'Сума {x}, по курсу {y} = {result}',   
    }

def comand(x, y, oper):          
    if oper == '+':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x+y))  
    elif oper == '-':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x-y)) 
    elif oper == '*':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x*y))      
    elif oper == '/':
        if y == 0:
            print('На нуль не ділиться!')
        else:
            print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x/y)) 
    elif oper == '//':
        if y == 0:
            print('На нуль не ділиться!')
        else:
            print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x//y))   
    elif oper == '%':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x%y))        
    elif oper == '**':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x**y))         
    elif oper == 'rnd':   
        if minus_right == 1:           #ошибка
            print('{y} - значення неможе бути від\'ємним')
        else:
            print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=round(float(x), int(y))))
    elif oper == 'v':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=math.sqrt(x)))         
    elif oper == 'rand':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=random.randint(x,y)))
    elif oper == '$':
        print(oper_dict.get(oper).format(x=x, y=y, oper=oper, result=x*y)) 