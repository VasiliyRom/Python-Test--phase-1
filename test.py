
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
        if name.isalpha():
            if name in channels:
                print('ТАК')
            else:
                print('НІ')
    
        elif name.isdigit():
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


