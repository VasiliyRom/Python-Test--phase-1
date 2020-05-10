import json

json_phonebook = open('phonebook.json', 'r')
phonebook = json.load(json_phonebook)


print('''
    Додати запис_____________________________(1)
    Пошук за імені___________________________(2)
    Пошук за прізвищу________________________(3)
    Пошук за повним іменем___________________(4)
    Пошук за номером телефону________________(5)
    Пошук по місту___________________________(6)
    Видаліть запис для номера телефону_______(7)
    Оновіть запис на даний номер телефону____(8)
    Вийти з програми_________________________(q)\n''')

while True:
    operator = input('Виберіть операцію: ')
    if operator == '1':
        print('не є числом.')
        

    elif operator == '2':
        query = input('Введіть ім\'я: ')
        for item in phonebook:
            if query in item['first_name']:
                print(item)
                continue
    elif operator == '3':
        query = input('Введіть прізвище: ')
        for item in phonebook:
            if query in item['last_name']:
                print(item)
                continue
    elif operator == '4':
        query = input('Введіть повне ім\'я: ')
        for item in phonebook:
            if query in item['full_name']:
                print(item)
                continue
    elif operator == '5':
        query = input('Введіть номер телефону: ')
        for item in phonebook:
            if query in item['number']:
                print(item)
                continue
    elif operator == '6':
        query = input('Введіть місто: ')
        for item in phonebook:
            if query in item['city']:
                print(item)
                continue            
       
       

    elif operator == '7':
        item = input('Введіть прізвище: ')
        for item in phonebook_json:
            if query == item['last_name']:
                print(item)
                continue       

    elif operator == 'exit' or operator == 'q':
        print('До побачення!')
        break        
