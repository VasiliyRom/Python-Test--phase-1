import asyncio, json, time


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, clients, messages):
        self.clients = clients
        self.msg = messages
        self.new_client = None

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        self.transport = transport
        print(f'З\'єднано з: {self.peername[1]}')
        if self.transport not in self.clients:
            print(f'Новий клієнт: {self.peername[1]}')
            self.new_client = self.transport
            if len(self.msg) != 0:
                last_messages = json.dumps({'last_messages': self.msg})
                self.new_client.write(last_messages.encode())

            self.clients.append(self.new_client)
            #self.new_client = None

    def data_received(self, data):
        decode_data = data.decode()
        json_message = json.loads(decode_data)
        user_name = json_message.get('user_name')
        message = json_message.get('message')

        print(f'Отримано меседж: {message} від {user_name}/id{self.peername[1]}')
        json_messages = json.dumps({'client': user_name, 'message': message})
        print(f'Відправлено: {message} для {user_name}/id{self.peername[1]}')

        for client in self.clients:
            client.write(json_messages.encode())
        self.msg.append(json.loads(json_messages))


    def connection_lost(self, exc):
        print(f'Закрито сокет для: {self.peername[1]}')

        self.transport.close()
        self.clients.remove(self.transport)
        message = f'Відєднався: {self.peername[1]}'
        mess = json.dumps({'client': 'SERVER', 'message': message}).encode()

        for client in self.clients:
            client.write(mess)



async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_event_loop()
    clients = []
    msg = []

    server = await loop.create_server(lambda: EchoServerProtocol(clients, msg), '127.0.0.1', 8888)
    print('[START SERVER]')
    async with server:
        try:
            await server.serve_forever()
        finally:
            EchoServerProtocol.connection_lost()
            loop.close()

if __name__ == '__main__':
    asyncio.run(main())
