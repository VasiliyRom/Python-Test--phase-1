# Task 1
name = "Василь"
day = "Неділя"
print(f'Добрий день {name}! {day} - ідеальний день для вивчення петону')

# Task 2
name = "Василь"
last_name = "Романюк"
print(f'Привіт {name} {last_name}')


pattern = '{msg} {name} {last_name}'
print(pattern.format(name='Василь', last_name='Романюк', msg='Привіт'))


pattern = '{Романюк}, {Василь}, {Привіт}'
print(pattern.format(1,2))

# Task 3
a, b = 3.2, 5.6
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
print(a//b)
print(a%b)


name = ‘Dostoyevsky’
lenght_of_name = len(name)
print(lenght_of_name)
