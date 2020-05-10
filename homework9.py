# Task 1
my_file = open('myfile.txt', 'w+')
my_file.write('Hello file world!')
my_file.close()

my_file = open('myfile.txt', 'r+')
print(my_file.read(100000))
my_file.write('\nMy name is Vasiliy')
my_file.seek(0)
print(my_file.read(100000))
my_file.close()

#Відповіді:
#1) Так файл відображається
#2) Якщо додати інший шлях то буде помилка, так як патон незнайде файл в директорії
#new_file1 = open('..\myfile.txt', 'r')


# Task 2
