import json


def replace_contact():
    first_name = input('Введіть ім\'я: ').capitalize()
    last_name = input('Введіть Прізвище: ').capitalize()
    full_name = (f'{first_name} {last_name}')      
    city = input('Введіть місто: ').capitalize()
    
    
    with open('phonebook.json') as file1:
        phonebook = json.load(file1)
        print(phonebook)
        phonebook["first_name"] = first_name
        phonebook["last_name"] = last_name
        phonebook["full_name"] = full_name
        phonebook["city"] = city
    with open('phonebook.json', 'w') as f:
        json.dump(phonebook, ensure_ascii=False, indent=4)



phonebook = json.load(open('phonebook.json'))
query = '6555'
for item in phonebook:
    if query == item['number']:
        print('Ви дійсно бажаєте оновити дані?')
        question = input('''
        Так - 1
        Ні - 2 ''')
        if question == '1':
            json.dump(open('phonebook.json', 'w'))
            first_name = input('Введіть ім\'я: ').capitalize()
            last_name = input('Введіть Прізвище: ').capitalize()
            full_name = (f'{first_name} {last_name}')      
            city = input('Введіть місто: ').capitalize()
            phonebook["first_name"] = first_name
            phonebook["last_name"] = last_name
            phonebook["full_name"] = full_name
            phonebook["city"] = city



            
            json.dump(phonebook, ensure_ascii=False, indent=4)
        else:    
            continue
        


