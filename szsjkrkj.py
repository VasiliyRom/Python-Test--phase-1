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

json_phonebook = open('phonebook.json', 'r')
phonebook = json.load(json_phonebook)

query = 'dima'
for item in phonebook:
    if query in item['first_name']:
        print(item)
    if query in item['last_name']:
        print(item)
    if query in item['full_name']:
        print(item)
    if query in item['number']:
        print(item)
    if query in item['city']:
        print(item)   
    break

            