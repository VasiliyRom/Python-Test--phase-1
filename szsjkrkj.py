import json

json_phonebook = open('phonebook.json', 'r')

phonebook = json.load(json_phonebook)



query = 'dima'
for item in phonebook:
    if query in phonebook:
        print(item)
        break

            