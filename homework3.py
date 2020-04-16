#Task 1
str = input('Введіть слово: ')
if len(str) > 2:
    print(f'{str[:2]}{str[-2:]}')
elif len(str) == 2:
    print(f'{str[:] * 2}')
elif len(str) <= 1:
    print('Empty String')

#Task 2
number = input('Введіть номер телефону +38: ')
if number.isdigit() and len(number) == 10:
    print('номер введено!')
else:
    print('Неправильно введений номер!')


#Task 3
name = 'vasiliy'
name1 = input('Введіть ваше ім\'я: ')
if name1.lower() == name:
    print('Ім\'я введено!')
else:
    print('Ім\'я введено неправильно!')