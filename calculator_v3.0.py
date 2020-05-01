#VER.3.0
from calc_def.validation import dot, operator, repl
from calc_def.comand import comand

name = input('Введіть Ім\'я: ')
name = name.strip(' ').capitalize()

oper = None
minus_left = None
minus_right = None


func_text = print(f'''\n{name}, калькулятор може виконувати наступні дії:
Додавання___________________________(+)
Віднімання__________________________(-)
Множення____________________________(*)
Ділення_____________________________(/)
Ділення націло______________________(//)
Остача від цілочисельного ділення___(%)
Піднести число в степінь____________(**)
Округлити число_____________________(rnd)
Корінь числа________________________(v)
Випадкове число від x до y)_________(rand)
Конвертер валют_____________________($)
Вийти з програми____________________(exit, q)

Приклад: 257 + 26\n''')
      
        
while True:
    mess = input()
    
    
    mess = repl(mess)
    if mess[0] == '-':
        mess = mess[1:]
        minus_left = 1
    
    if mess == 'exit' or mess == 'Exit' or mess == 'EXIT' or mess == 'q':
        print(f'Допобачення, {name}!')
        break  
        

    oper = operator(mess)
    
    if oper == None:
            print(f'Програма не знайшла функцію!')
            continue
    
    
    
    if oper == 'v':         # корінь квадратний
        s = mess.split(oper)    
        x=s[0]
        y=1
        if x.isalpha():
            print(f'{x} не є числом!')
            continue
        else:    
            x=dot(x)  
            comand(x, y, oper)
            continue
    
    #############        
    s = mess.split(oper)    
    x=s[0]
    y=s[1]
           
    if y[0] == '-':
        y = y[1:]
        minus_right = 1
    
    ########################
    if oper == '$':
        if minus_left == 1:
            print(f'-{x} - неможе бути від\'ємним!')
        if minus_right == 1:
            print(f'-{y} - неможе бути від\'ємним!')
        continue
            
    if x.isalpha() or y.isalpha():
        print(f'{x} або {y} не є числом!')
        continue     
    else:    
        x=dot(x)
        y=dot(y)
  
    if minus_left == 1:    
        x = -x
    if minus_right == 1:    
        y = -y     
    comand(x, y, oper)