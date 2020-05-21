class TVController():
    channels = ["BBC", "Discovery", "TV1000"]
    def __init__(self):
        self.channel_num = 1

    def get_current_channel(self):
        return self.channels[self.channel_num - 1]
    
    def turn_channel(self, index):
        self.channel_num = index % len(self.channels)
        print(self.get_current_channel())


    def next_channel(self):
        if self.channel_num >= len(self.channels):
            self.channel_num = 1
        else:
            self.channel_num += 1
        print(self.get_current_channel())

controller = TVController()

controller.turn_channel(4)
controller.next_channel()