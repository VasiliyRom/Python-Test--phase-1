#Task1
class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Добрий день. Мене звати {greeting.firstname} {greeting.lastname}, мені {greeting.age} років')
        
greeting = Person('Vasiliy', 'Romaniuk', '27')
greeting.talk()

#Task2
class Dog():
    age_factor = 7

    def __init__(self, age):
        self.age = age
    def human_age(self):
        print(self.age + self.age_factor)

dog = Dog(int(input('Введіть вік: ')))
dog.human_age()

#Task3
channels = ["BBC", "Discovery", "TV1000"]

class TVController():

    def first_channel(self):
        print(channels[0])
        
    def last_channel(self):
        print(channels[-1])

    def turn_channel(self, N):
        self.N = N
        print(channels[N - 1])
        
    def next_channel(self):
        if self.N == 3:
            print(channels[0])
        else:
            print(channels[self.N])

    def previous_channel(self):
        if self.N == 1:
            self.chan = channels[0]
            print(channels[0])
        else:
            self.chan = channels[self.N - 1]
            print(channels[self.N - 1])
        
    def current_channel(self):
        print(self.chan)

    def is_exist(self, name):
        if type(name) == str:
            if name in channels:
                print('ТАК')
            else:
                print('НІ')
    
        elif type(name) == int:
            if len(channels) >= name:
                print('ТАК')
            else:
                print('НІ')

controller = TVController()

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist("BBC")
controller.is_exist(3)

