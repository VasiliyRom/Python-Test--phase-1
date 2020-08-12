import sys, asyncio, random
from quamash import QEventLoop
from client import EchoClientProtocol
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow,
                             QPushButton, QLineEdit, QListWidget)


class MyWindow(QMainWindow):
    def __init__(self, loop, client_new, **kwargs):
        super(__class__, self).__init__(**kwargs)
        self.client_new = client_new
        self.client_new.set_callback(self.output)
        self.client_new.output = self.output
        self.loop = loop
        self.setWindowTitle('Чат')
        self.setGeometry(600, 200, 300, 450)
        self.main()

    def output(self, data):
        self.history.addItem(data)

    def main(self):
        widget = QWidget()
        headLayout = QHBoxLayout()

        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText('Введіть нік')
        ok_butt = QPushButton('OK')


        headLayout.addWidget(self.user_name)
        headLayout.addWidget(ok_butt)

        self.history = QListWidget()
        self.editArea = QLineEdit('')
        self.editArea.setPlaceholderText('Введіть повідомлення')
        self.editArea.setEnabled(False)

        button = QPushButton('Надіслати')

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(headLayout)
        mainLayout.addWidget(self.history)
        mainLayout.addWidget(self.editArea)
        mainLayout.addWidget(button)

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        button.clicked.connect(self.send_message)
        self.editArea.returnPressed.connect(button.click)
        ok_butt.clicked.connect(self.check_user)

    def check_user(self):
        user = self.user_name.text()
        if user == '':
            self.user_name.setText(f'User_{int(random.random() * 1000)}')
        else:
            self.user_name.setText(user)
        self.editArea.setEnabled(True)
        self.user_name.setEnabled(False)


    def send_message(self):
        try:
            message = self.editArea.text()
            if message != '':
                self.client_new.send(message, self.user_name.text())
            self.editArea.clear()
        except Exception as e:
            print(e)
            print('Error')
            self.history.addItem('Error')


class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.loop = QEventLoop(self)
        asyncio.set_event_loop(self.loop)
        self.userClient = EchoClientProtocol(self.loop, 'user')

        self.loop.create_task(self.start())

        self.window = MyWindow(self.loop, self.userClient)
        self.window.show()
        self.loop.run_forever()


    async def start(self):
        print('[START CLIENT]')
        clientConnection = self.loop.create_connection(lambda: self.userClient, '127.0.0.1', 8888)

        await asyncio.wait_for(clientConnection, 10000, loop=self.loop)


if __name__ == '__main__':
    App()
