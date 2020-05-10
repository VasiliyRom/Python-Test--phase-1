import json

phonebook = json.load(open('phonebook.json'))

user_info = {"phonebook": "1",
    "first_name": "2",
    "last_name": "3",
    "full_name": "4",
    "number": "5",
    "city": "6"
}

phonebook.append(user_info)

with open('phonebook.json', 'w') as filee:
    json.dump(phonebook, filee, indent=4)
    




