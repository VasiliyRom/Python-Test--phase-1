import sys
import requests
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QVBoxLayout,
                             QHBoxLayout,
                             QComboBox,
                             QFormLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QLabel)
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Погода')
        self.setGeometry(500, 400, 400, 200)
        widget = QWidget()
        widget.setStyleSheet('background-color: white')

        #
        self.editArea = QLineEdit()
        f = self.editArea.font()
        f.setPointSize(8)
        self.editArea.setFont(f)
        #
        self.label = QLabel('Введіть місто', self)
        #
        self.btn = QPushButton('OK', self)
        #
        HLayout = QHBoxLayout()

        #
        combo = QComboBox(self)
        combo.addItem('Зараз')
        combo.addItem('На 3 дні')
        combo.addItem('На 5 днів')
        self.combo = 'Зараз'
        combo.activated[str].connect(self.on)
        #

        HLayout.addWidget(self.label)
        HLayout.addWidget(self.editArea)
        HLayout.addWidget(combo)
        HLayout.addWidget(self.btn)



        HLayout1 = QHBoxLayout()
        rootLayout = QVBoxLayout()

        rootLayout.addLayout(HLayout)
        rootLayout.addLayout(HLayout1)

        #self.btn.move(200, 20)


        self.resalt = QLabel('', self)
        font = self.resalt.font()
        font.setPointSize(12)
        self.resalt.setFont(font)
        #self.resalt.setGeometry(8, 0, 190, 85)
        #self.resalt.setStyleSheet('background-color: red')
        HLayout1.addWidget(self.resalt)
        self.img = QLabel(self)

        HLayout1.addWidget(self.img)

        widget.setLayout(rootLayout)
        self.setCentralWidget(widget)

        self.btn.clicked.connect(self.weather)  # вивод текста в поле

    # сохраняю змінну
    def on(self, text):
        self.combo = text



    def weather(self):
        try:
            if self.combo == 'Зараз':
                location = self.editArea.text()
                #location = 'Рівне'
                appid = '9ccceec878f6a3e707cb75d92d2d63af'
                URL = requests.get(
                    'https://api.openweathermap.org/data/2.5/weather',
                                params = {'q': location, 'units': 'metric', 'appid': appid, 'lang': '42'})
                resalt = URL.json()
                print(resalt)

                temp = resalt['main']['temp']
                pressure = resalt['main']['pressure']
                humidity = resalt['main']['humidity']
                wind = resalt['wind']['speed']
                description = resalt['weather'][0]['description']
                if description == 'clear sky':
                    clouds = 'Ясно'
                elif description == 'few clouds':
                    clouds = 'Невелика хмарність'
                elif description == 'scattered clouds':
                    clouds = 'Розсіяні хмари'
                elif description == 'broken clouds':
                    clouds = 'Хмарно'
                elif description == 'shower rain':
                    clouds = 'Злива'
                elif description == 'rain':
                    clouds = 'Дощ'
                elif description == 'thunderstorm':
                    clouds = 'Гроза'
                elif description == 'snow':
                    clouds = 'Сніг'
                elif description == 'mist':
                    clouds = 'Туман'
                self.resalt.setText(f"Температура {temp} °C\nВологість - {humidity} %\nТиск - {pressure} гПа\nВітер - {wind} м/с\n{clouds}")
                pixmap = QPixmap(f"{description}.png")
                self.img.setPixmap(pixmap)
            else:
                #location = 'Rivne'
                location = self.editArea.text()
                appid = '9ccceec878f6a3e707cb75d92d2d63af'
                URL = requests.get(
                    'http://api.openweathermap.org/data/2.5/forecast',
                                params = {'q': location, 'units': 'metric', 'cnt': '60', 'appid': appid})

                resalt = URL.json()['list']
                timer = 0
                ###########
                list = []
                for i in resalt:
                    spl = i['dt_txt'].split(' ')
                    if timer == 6:
                        timer = 0
                        break
                    else:
                        if spl[1] == '12:00:00':
                            day = [{
                                "date": spl[0],
                                "temp": i['main']['temp'],
                                "id": i['weather'][0]['id'],
                            }]
                            print(i['weather'][0]['id'])
                            timer += 1
                            list.append(day)
                if self.combo == 'На 3 дні':
                    self.resalt.setText(
                        f"{list[0][0]['date']}\nТемп. {list[0][0]['temp']} °C {self.change(list[0][0]['id'])}\n\n"
                        f"{list[1][0]['date']}\nТемп. {list[1][0]['temp']} °C {self.change(list[1][0]['id'])}\n\n"
                        f"{list[2][0]['date']}\nТемп. {list[2][0]['temp']} °C {self.change(list[2][0]['id'])}\n\n")

                else:
                    self.resalt.setText(
                        f"{list[0][0]['date']}\nТемп. {list[0][0]['temp']} °C {self.change(list[0][0]['id'])}\n\n"
                        f"{list[1][0]['date']}\nТемп. {list[1][0]['temp']} °C {self.change(list[1][0]['id'])}\n\n"
                        f"{list[2][0]['date']}\nТемп. {list[2][0]['temp']} °C {self.change(list[2][0]['id'])}\n\n"
                        f"{list[2][0]['date']}\nТемп. {list[2][0]['temp']} °C {self.change(list[3][0]['id'])}\n\n"
                        f"{list[2][0]['date']}\nТемп. {list[2][0]['temp']} °C {self.change(list[4][0]['id'])}\n\n")
        except:
            self.resalt.setText('Error')

    def change(self, id_desc):
        id = str(id_desc)[0]
        if id == '2':
            clouds = 'Гроза'
        elif id == '3':
            clouds = 'Мряка'
        elif id == '5':
            clouds = 'Дощ'
        elif id == '6':
            clouds = 'Сніг'
        elif id == '7':
            clouds = 'Туман'
        elif id_desc == '800':
            clouds = 'Ясно'
        elif id == '8':
            clouds = 'Хмарно'
        return clouds






def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()