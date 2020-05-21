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
class TVController():

    channels = ["BBC", "Discovery", "TV1000"]
    
    def __init__(self):
        self.channel_num = 1

    def get_current_channel(self):
        return self.channels[self.channel_num - 1]

    def first_channel(self):
        print(self.get_current_channel())
        
    def last_channel(self):
        self.channel_num = len(self.channels)
        print(self.get_current_channel())

    def turn_channel(self, index):
        self.channel_num = index % len(self.channels)
        print(self.get_current_channel())

    def next_channel(self):
        if self.channel_num >= len(self.channels):
            self.channel_num = 1
        else:
            self.channel_num += 1
        print(self.get_current_channel())

    def previous_channel(self):
        if self.channel_num >= len(self.channels):
            self.channel_num = 1
        else:
            self.channel_num -= 1
        print(self.get_current_channel())

    def current_channel(self):
        print(self.get_current_channel())

    def is_exist(self, name):
        if type(name) == str:
            if name in self.channels:
                print('ТАК')
            else:
                print('НІ')
    
        elif type(name) == int:
            if len(self.channels) >= name:
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
controller.is_exist(4)
controller.is_exist("BBC")
