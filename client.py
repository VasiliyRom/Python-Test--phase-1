import sys
import asyncio
import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QListWidget,
                             QLabel,
                             QSizePolicy)
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Чат')
        self.setGeometry(1200, 500, 300, 450)
        widget = QWidget()
        self.history = QListWidget()
        #self.history.setPalette()

        self.editArea = QLineEdit('')
        self.editArea.setPlaceholderText('Введіть повідомлення')
        button = QPushButton('Надіслати')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.history)

        mainLayout.addWidget(self.editArea)
        mainLayout.addWidget(button)

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        button.clicked.connect(self.change_text)

        self.editArea.returnPressed.connect(button.click)



    def change_text(self):
        try:
            message = self.editArea.text()
            self.history.addItem(message)
            self.editArea.clear()
            sel

        except:
            print('Error')
            self.history.addItem('Error')


    def end(self):
        self.editArea.setText('')

'''async def client(self):
    while True:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

        message = input()
        print(f'Send to server: {message}')
        data = json.dumps({'sender': 'First', 'message': message})
        writer.write(data.encode())
        data = await reader.read(100)
        if data:
            print(f'Received: {data.decode()}')
            await asyncio.sleep(1)
'''








async def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    #reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    #print('[Client started]')


    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'
    transport, protocol = await asyncio.open_connection('127.0.0.1', 8889)

    try:
        await on_con_lost
    finally:

        transport.close()


if __name__ == '__main__':
    asyncio.run(main_window())
