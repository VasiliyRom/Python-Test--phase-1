import asyncio, json


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, user):
        self.user = user
        self.loop = loop
        self.callback = None

    def connection_made(self, transport):
        self.transport = transport

    def send(self, data, user_name):
        self.message = data
        json_message = json.dumps({'user_name': user_name, 'message': self.message})
        print(f'Відправлено: {self.message}')
        self.transport.write(json_message.encode())

    def data_received(self, data):
        json_load = json.loads(data.decode())
        if json_load.get('last_messages'):
            for i in json_load.get('last_messages'):
                user = i.get("client")
                message = i.get("message")
                self.callback(f'[{user}] {message}')
        else:
            user = json_load.get('client')
            message = json_load.get('message')
            print(f'Отримано: {message}')
            print(user)
            print(message)
            self.callback(f'[{user}] {message}')

    def set_callback(self, output):
        self.callback = output

    def connection_lost(self, exc):
        print('Сервер закрив зв\'язок')
        self.loop.stop()


def main():
    loop = asyncio.get_event_loop()
    #message = 'Hello World!'
    loop.run_until_complete(loop.create_connection(lambda: EchoClientProtocol(loop, 'client_name'), '127.0.0.1', 8888))
    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    main()