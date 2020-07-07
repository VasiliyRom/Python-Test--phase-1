import sys

from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QMainWindow,
                             QPushButton, QLineEdit, QLabel)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Серйозний калькулятор!')
        self.setGeometry(500, 400, 400, 200)
        widget = QWidget()

        #firstLabel = QLabel('<h1>Давно не бачилися!</h1>')
        #firstLabel.setFixedSize(300, 50)
        self.editArea = QLineEdit('0')
        self.editArea.setReadOnly(True)
        

        #
        f = self.editArea.font()
        f.setPointSize(30)
        self.editArea.setFont(f)
        #

        memoryLayout = QVBoxLayout()

        mainLayout = QVBoxLayout()

        #mainLayout.addWidget(firstLabel)

        #memoryLayout.addWidget(QPushButton('one'))

        mainLayout.addWidget(self.editArea)

        buttonLayout = QGridLayout()  #градація кнопок

        buttons = [{
            'name': '%',
            'row': 0,
            'col': 0
        }, {
            'name': 'x^2',
            'row': 0,
            'col': 1
        }, {
            'name': 'C',
            'row': 0,
            'col': 2
        }, {
            'name': 'x',
            'row': 0,
            'col': 3
        }, {
            'name': '7',
            'row': 1,
            'col': 0
        }, {
            'name': '8',
            'row': 1,
            'col': 1
        }, {
            'name': '9',
            'row': 1,
            'col': 2
        }, {
            'name': '/',
            'row': 1,
            'col': 3
        }, {
            'name': '4',
            'row': 2,
            'col': 0
        }, {
            'name': '5',
            'row': 2,
            'col': 1
        }, {
            'name': '6',
            'row': 2,
            'col': 2
        }, {
            'name': '-',
            'row': 2,
            'col': 3
        }, {
            'name': '1',
            'row': 3,
            'col': 0
        }, {
            'name': '2',
            'row': 3,
            'col': 1
        }, {
            'name': '3',
            'row': 3,
            'col': 2
        }, {
            'name': '+',
            'row': 3,
            'col': 3
        }, {
            'name': '0',
            'row': 4,
            'col': 0,
        }, {
            'name': '+/-',
            'row': 4,
            'col': 0,
        }, {
            'name': '0',
            'row': 4,
            'col': 1,
        }, {
            'name': '.',
            'row': 4,
            'col': 2,
            'qw': 1
        }, {
            'name': '=',
            'row': 4,
            'col': 3,
        }]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)

            self.buttons[name] = btn
            buttonLayout.addWidget(btn, buttonConfig['row'],
                                   buttonConfig['col'], 1, 1)
        mainLayout.addLayout(buttonLayout)

        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

        self.formula = self.editArea.text()
        self.save_resalt = '0'
        self.oper = '0'
        for buttonName in self.buttons:

            btn = self.buttons[buttonName]

            #btn.clicked.connect(partial(self.change_text, buttonName))  # вивод текста в поле

            #отслежует нажатия кнопок
            if (buttonName == '1' or buttonName == '2' or buttonName == '3'
                    or buttonName == '4' or buttonName == '5'
                    or buttonName == '6' or buttonName == '7'
                    or buttonName == '8' or buttonName == '9'
                    or buttonName == '0'):
                btn.clicked.connect(partial(self.change_text, buttonName))

            elif buttonName == 'C':
                btn.clicked.connect(self.c_del)
            elif buttonName == '.':
                btn.clicked.connect(self.point)
            elif buttonName == '+' or buttonName == '-':
                btn.clicked.connect(partial(self.add_oper, buttonName))
            elif buttonName == 'x' or buttonName == '/':
                btn.clicked.connect(partial(self.add_oper, buttonName))
            elif buttonName == '%':
                btn.clicked.connect(partial(self.percent, buttonName))
            elif buttonName == 'x^2':
                btn.clicked.connect(partial(self.step, buttonName))
            elif buttonName == '+/-':
                btn.clicked.connect(self.change_sign)
            elif buttonName == '=':
                btn.clicked.connect(self.calc)


    def step(self, text):
        try:
            if self.formula == '0':
                pass
            else:
                if self.formula == float:
                    resalt = str(float(self.formula) * float(self.formula))
                else:
                    resalt = str(int(self.formula) * int(self.formula))
                self.formula += ('^2=' + resalt)
                self.save_resalt = self.formula
                self.update_text()
                self.formula = '0'
        except:
            self.editArea.setText('Error')


    def change_sign(self):
        try:
            if self.formula == '0':
                pass
            elif '=' not in self.formula:
                if self.formula[0] == '-':
                    self.formula = self.formula[1:]
                    self.update_text()
                else:
                    self.formula = str('-' + self.formula)
                    self.update_text()
            print(self.save_resalt)
            if '=' in self.save_resalt:
                print('--------')
                print(self.save_resalt)
                spl = self.save_resalt.split('=')
                second_arg = spl[1]
                if second_arg[0] == '-':
                    self.formula = (spl[0] + '=' + second_arg[1:])
                    self.update_text()
                else:
                    self.formula = (spl[0] + '=' + '-' + second_arg)
                    self.update_text()
                    self.formula = '0'
        except:
            self.formula = 'Error'
            self.update_text()


    def calc(self):
        try:
            if self.formula == '0':
                pass
            else:
                value = self.formula.split(self.oper)
                print('good')
                if self.oper == '+':
                    if float(value[0]) or float(value[1]):
                        print('12-----3')
                        resalt = float(value[0]) + float(value[1])
                        print('123')
                    else:
                        resalt = int(value[0]) + int(value[1])
                elif self.oper == '-':
                    if float(value[0]) or float(value[1]):
                        resalt = float(value[0]) - float(value[1])
                    else:
                        resalt = int(value[0]) - int(value[1])
                elif self.oper == 'x':
                    if float(value[0]) or float(value[1]):
                        resalt = float(value[0]) * float(value[1])
                    else:
                        resalt = int(value[0]) * int(value[1])
                elif self.oper == '/':
                    if float(value[0]) or float(value[1]):
                        resalt = float(value[0]) / float(value[1])
                    else:
                        resalt = int(value[0]) / int(value[1])

                self.formula += str('=' + str(resalt))
                self.update_text()
                self.save_resalt = self.formula
                #self.label_3.setText(self.formula)
                self.formula = '0'

        except:
            self.formula = 'Error222'
            self.update_text()


    def percent(self, text):
        try:
            spl = self.formula.split(self.oper)

            if self.oper == '+':
                self.formula = str(float(spl[0]) + (float(spl[0]) / 100 * float(spl[1])))
            elif self.oper == '-':
                self.formula = str(float(spl[0]) - (float(spl[0]) / 100 * float(spl[1])))
            elif self.oper == 'x':
                self.formula = str(float(spl[0]) * (float(spl[0]) / 100 * float(spl[1])))
            elif self.oper == '/':
                self.formula = str(float(spl[0]) / (float(spl[0]) / 100 * float(spl[1])))
            self.update_text()
            self.formula = '0'
            print(self.formula)
        except:
            self.formula = 'Error'
            self.update_text()
            self.formula = '0'


    def add_oper(self, text):
            try:
                self.oper = text
                if self.formula == '0':
                    pass
                else:
                    self.formula += self.oper
                    self.update_text()

                if '=' in self.save_resalt:
                    print('000000')
                    print(self.save_resalt)

                    spl = self.save_resalt.split('=')[1]
                    # self.formula += spl[1] + button
                    print(spl + text)
                    self.formula = str(spl + self.oper)
                    self.update_text()

                    self.save_resalt = '0'

            except:
                self.formula = 'Error'
                self.update_text()


    def change_text(self, button):
        try:
            if self.formula == 'Error':
                self.formula = ''

            elif self.formula == '0':
                self.formula = ''

            self.formula += button
            print(self.formula)
            self.update_text()

        except:
            self.formula = 'Error'


    def point(self):
        if self.oper == '0':
            if '.' in self.formula:
                pass
            else:
                self.formula += '.'
        else:
            spl = self.formula.split(self.oper)
            if '.' in spl[1]:
                pass
            else:
                self.formula += '.'

        self.update_text()


    def c_del(self):
        try:
            self.formula = '0'
            self.save_resalt = '0'
            self.update_text()
            self.oper = '0'
        except:
            self.formula = 'Error'
            self.update_text()


    def update_text(self):
        '''if self.formula == '0':
            self.editArea.setText('')
        else:'''
        self.editArea.setText(self.formula)




'''def main_widget():
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Серйозний калькулятор')
    mainWidget.setFixedSize(500, 500)
    mainWidget.show()
    return_code = app.exec()
    sys.exit(return_code)'''


def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()