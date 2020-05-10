import json
        
def new_contact(first_name, last_name, full_name, number, city):
    user_info = {"phonebook": "name",
    "first_name": first_name,
    "last_name": last_name,
    "full_name": full_name,
    "number": number,
    "city": city
}
    try:
        phonebook = json.load(open('phonebook.json'))
    except:
        phonebook = []

    phonebook.append(user_info)

    with open('phonebook.json', 'w') as filee:
        json.dump(phonebook, filee, indent=4, ensure_ascii=False)
    return print('Ok')



print('''
    Додати запис_____________________________(1)
    Пошук за імені___________________________(2)
    Пошук за прізвищу________________________(3)
    Пошук за повним іменем___________________(4)
    Пошук за номером телефону________________(5)
    Пошук по місту___________________________(6)
    Видаліть запис для номера телефону_______(7)
    Оновіть запис для номеру телефону________(8)
    Вийти з програми_________________________(q)\n''')

while True:
    operator = input('Введіть операцію: ')
    try:
        phonebook = json.load(open('phonebook.json'))
    except:
        print('Телефонна книга незнайдена!')
        break

    if operator == '1':
        first_name = input('Введіть ім\'я: ').capitalize()
        last_name = input('Введіть Прізвище: ').capitalize()
        full_name = (f'{first_name} {last_name}')
        number = input('Введіть номер тел: ')
        city = input('Введіть місто: ').capitalize()

        new_contact(first_name, last_name, full_name, number, city)
        

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
            if query == item['number']:
                print(item)
                continue
    elif operator == '6':
        query = input('Введіть місто: ')
        for item in phonebook:
            if query in item['city']:
                print(item)
                continue            
       
       

    elif operator == '7':
        query = input('Введіть номер телефону: ')
     
        for item in range(len(phonebook)):
            if(phonebook[item]["number"] == query):
                del phonebook[item]
                break
        with open('phonebook.json', 'w') as filee:
            json.dump(phonebook, filee, indent=4, ensure_ascii=False)
        print('Ok')

    elif operator == '8':
        query = input('Введіть номер телефону: ')
        for item in phonebook:
            if query == item['number']:
                print('Ви дійсно бажаєте оновити дані?')
                question = input('''
                Так - 1
                Ні - 2 \n''')
                if question == '1':
                    phonebook.remove(item)
                    first_name = input('Введіть ім\'я: ').capitalize()
                    last_name = input('Введіть Прізвище: ').capitalize()
                    full_name = (f'{first_name} {last_name}')
                    number = query
                    city = input('Введіть місто: ').capitalize()

                    new_contact(first_name, last_name, full_name, number, city)
                else:    
                    continue    
       

    elif operator == 'exit' or operator == 'q':
        print('До побачення!')
        break
       
