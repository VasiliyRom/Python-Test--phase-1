#Task1
import random
result = []
while len(result) != 10: 
    numbers = random.randint(1,6892)
    result.append(numbers)
print(result)
print(max(result))


#Task2
import random
collection_1 = []
collection_2 = []
collection_3 = []
result = []
while len(collection_1) != 10 and (collection_2) != 10: 
    numbers = random.randint(1,10)
    collection_1.append(numbers)
    numbers1 = random.randint(1,10)
    collection_2.append(numbers1)

collection_3 = collection_1 + collection_2
result = list(set(collection_3))
print('Результат -', result)




#Task3
a = []
b = []
i = 1
while True:
    a.append(i)
    i += 1
    if i == 101:
        break
    
i = 0
while True:
    item = a[i]
    if item % 7 == 0 and item % 5 != 0:
        b.append(item)
    i += 1
    if i >= len(a):
        break
print(b)





##Task3 FOR
a = []
b = []
i = 1
while True:
    a.append(i)
    i += 1
    if i == 101:
        break
print(a)
print()
for x in a:
    if x % 7 == 0 and x % 5 != 0:
        b.append(x)
print(b) 