# Task1
class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list = [i for i in item]

    def pop(self):
        return self.list.pop()

    def stack(self):
        self.list = [self.pop() for i in range(len(self.list))]
        print(self.list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = Stack()
s.push(list)
s.stack()

# Task2

balanced = "({{[}])"
parentheses = 0
brackets = 0
curly_brackets = 0

if len(balanced) == 0:
    print("Збалансовано")
else:
    for i in balanced:

        if i == "(":
            curly_brackets += 1
        elif i == ")":
            curly_brackets -= 1
        elif i == "[":
            brackets += 1
        elif i == "]":
            brackets -= 1
        elif i == "{":
            parentheses += 1
        elif i == "}":
            parentheses -= 1
if parentheses == 0 and brackets == 0 and curly_brackets == 0:
    print("Збалансовано")
else:
    print("Незбалансовано")


# Task3

class StackNew:

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list = [i for i in item]

    def pop(self):
        return self.list.pop()

    def stack(self):
        self.list = [self.pop() for i in range(len(self.list))]
        print(self.list)

    def get_from_stack(self, item):
        for i in range(len(self.list)):
            if i == self.pop():
                self.item = self.pop()
            else:
                self.list.insert(0, self.pop)

        if self.item == None:
            raise ValueError('Значення відсутнє')
        return self.item

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = StackNew()
s.push(list)
print(s.get_from_stack(3))
