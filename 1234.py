symbols = ['!','@','#','$',' ']
text = input()
for symbol in symbols:
    if symbol in text:
        print(text.replace(symbol,''))
        if text.isalpha:
            print('В стрічці є недопустимі символи чи пробіли')