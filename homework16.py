# Task 1_1
def with_index(iterable, start=0):
    for i in iterable:
        print(str(start), i)
        start += 1

with_index(['one', 'two'])

# Task 1_2
def with_index(iterable, start=0):
    if start >= len(iterable):
        raise ValueError
    yield start, iterable[start]

lst = ['one', 'two']

x = with_index(lst, 0)
print(next(x))



# Task 2
def in_range(start, end, step=1):

    if type(start) != int and type(end) != int and type(step) != int:
        raise ValueError('qwerty')
    else:
        while start <= end:
            yield int(start)
            start += step


print(list(in_range(1, 40)))



# Task 3

class Iter:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        self.index += 1
        return value

x = Iter(1, 2, 3, 4, 5)

for i in x:
    print(i)