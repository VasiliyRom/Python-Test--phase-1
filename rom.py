class CustomException(Exception):
    def __init__(self, msg, *args):
        self.msg = msg

    def __str__(self):
        return ''.join(self.msg)


error = CustomException('Custom error')

try:
    name = 'aaaa'
    if len(name) < 5:
        raise CustomException(f'{name} - має містити 5 символів')
except CustomException as e:
    print(type(e))
    print(str(e))
    log = []
    log.append(str(e))
    new_file = open('logs.txt', 'a')
    new_file.writelines(log)
    new_file.close()
    