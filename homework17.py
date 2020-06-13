import sys
import homework17_test as f
from calc_def import mymod

#Task1

print(f.test(4))


#Task2

#Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
#можемо без проблем міняти список (добавляти і видаляти). 
#Так пайтон буде дивитись в каталогах по дефолту і в тих що ми йому назвали

print(sys.path)
sys.path.append('C:\\Users\\Василий Романюк\\Documents\\GitHub')
print(sys.path)


#Task3

print(mymod.count_lines("homework17_test3.txt"))
print(mymod.count_chars("homework17_test3.txt"))
print(mymod.test("homework17_test3.txt"))
