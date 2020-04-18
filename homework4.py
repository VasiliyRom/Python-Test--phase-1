name = input('Введіть Ім\'я: ')
name = name.strip(' ')
while True:
    operator = input(f'''{name.capitalize()}, виберіть операцію зі списку наступних:
    Додавання___________________________(+)
    Віднімання__________________________(-)
    Множення____________________________(*)
    Ділення_____________________________(/)
    Ділення націло______________________(//)
    Остача від цілочисельного ділення___(%)
    Піднести число в степінь____________(**)
    Округлити число_____________________(round)
    Знайти квадрат числа________________(x^2)
    Випадкове число від x до y)_________(abc)
    Конвертер валют_____________________(con)
    Вийти з програми____________________(exit)\n''')
    
    if operator == '+':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} + {y} = {float(x) + float(y)}')
    
    elif operator == '-':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} - {y} = {float(x) - float(y)}')
            
    elif operator == '*':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} * {y} = {float(x) * float(y)}')
    
    elif operator == '/':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            x = float(x)
            y = float(y)
            if y == 0:
                print('На нуль не ділиться') 
            else:
                print(f'{x} / {y} = {x / y}')  
                
    elif operator == '//':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} // {y} = {int(x) // int(y)}')       
    
    elif operator == '%':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} % {y} = {int(x) % int(y)}')        
   
    elif operator == '**':
        x = input('x= ')
        x = x.strip(' ')
        y = input('В яку степінь: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} ^ {y} = {float(x) ** int(y)}')        
    
    elif operator == 'round':
        x = input('x= ')
        x = x.strip(' ')
        y = input('кількість знаків після коми: ')
        y = y.strip(' ')        
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x}, {y} знаків після коми = {round(float(x), int(y))}')         
    elif operator == 'x^2':
        x = input('x= ')
        if x.isalpha() and y.isalpha():
            print(f'{x} не є числом.')
        else:
            print(f'{x} в квадраті = {int(x) * int(x)}')  
            
    elif operator == 'abc':
        import random
        x = input('Від: ')
        x = x.strip(' ')
        y = input('До: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            x = int(x)
            y = int(y)
            com = random.randint(x,y)
            print(com)   
    
    elif operator == 'con':
        x = input('Сума: ')
        x = x.strip(' ')
        y = input('Курс: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'Отримаєте {float(x) * float(y)}')
            
    elif operator == 'exit' or operator == 'Exit' or operator == 'EXIT' or operator == 'q':
        print(f'До побачення, {name.capitalize()}!')
        break
    else:
        print(f'{operator} - неправильний знак')