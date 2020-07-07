from PyQt5 import QtWidgets
from MainWind import Ui_Calc


class CalcWindow(QtWidgets.QMainWindow, Ui_Calc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.formula = '0'

        self.pushButton_0.clicked.connect(self.change_text)
        self.pushButton_1.clicked.connect(self.change_text)
        self.pushButton_2.clicked.connect(self.change_text)
        self.pushButton_3.clicked.connect(self.change_text)
        self.pushButton_4.clicked.connect(self.change_text)
        self.pushButton_5.clicked.connect(self.change_text)
        self.pushButton_6.clicked.connect(self.change_text)
        self.pushButton_7.clicked.connect(self.change_text)
        self.pushButton_8.clicked.connect(self.change_text)
        self.pushButton_9.clicked.connect(self.change_text)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_plys.clicked.connect(self.add_oper)
        self.pushButton_maynes.clicked.connect(self.add_oper)
        self.pushButton_mno.clicked.connect(self.mult)
        self.pushButton_delete.clicked.connect(self.add_oper)
        self.pushButton_resalt.clicked.connect(self.calc)
        self.pushButton_vid.clicked.connect(self.percent)
        self.pushButton_22.clicked.connect(self.step)
        self.pushButton_decimal.clicked.connect(self.decimal)
        self.pushButton_pl_may.clicked.connect(self.maynes)

    def update(self):
        try:
            self.label.setText(self.formula)
            print(self.formula)
        except:
            self.label.setText('Errorrrrr')

    def mult(self):
        if self.formula == '0':
            self.update()
        else:
            self.formula += '*'
            self.update()

    def change_text(self):
        button = self.sender()
        try:
            print(self.formula)
            if self.formula == '0':
                self.formula = ''
            self.formula += button.text()
            self.label_3.setText(self.formula)
            self.update()

        except:
            self.formula = 'Error'
            self.update()

    def add_oper(self):
        try:
            button = self.sender()
            self.oper = str(button.text())
            if self.formula == '0':
                self.update()
            else:
                self.formula += self.oper
                self.update()

            self.label_3.setText(self.formula)
        except:
            self.formula = 'Error'
            self.update()


    def percent(self, text):
        try:
            arg = self.formula.split('%')[0]
            resalt = arg.split(self.oper)
            if self.oper == '+':
                self.formula = str(float(resalt[0]) + (float(resalt[0]) / 100 * float(resalt[1])))
            elif self.oper == '-':
                self.formula = str(float(resalt[0]) - (float(resalt[0]) / 100 * float(resalt[1])))

            self.update()
            self.label_3.setText(self.formula)
            self.formula = '0'
        except:
            self.formula = 'Error'
            self.update()
            self.formula = '0'

    def clear(self):
        self.formula = '0'
        self.save_resalt = '0'
        self.update()

    def decimal(self):
        try:
            if self.formula == '0':
                self.formula += '.'
                self.update()
            else:
                self.formula += '.'
                self.update()
                self.label_3.setText(self.formula)

        except:
            self.formula = 'Error'
            self.update()

    def calc(self):
        try:
            if self.formula == '0':
                self.update()
            else:
                self.formula += ('=' + str(eval(self.formula)))
                self.update()
                self.save_resalt = self.formula
                self.label_3.setText(self.formula)
                self.formula = '0'

        except:
            self.formula = 'Error'
            self.update()

    def step(self, text):
        try:
            if self.formula == '0':
                self.update()
            else:
                self.formula += ('^2=' + str(float(self.formula) * float(self.formula)))
                self.update()
        except:
            self.formula = 'Error'
            self.update()
            self.formula = '0'


    def maynes(self, text):
        try:
            if self.formula != '0' and '=' not in self.formula:
                if self.formula[0] == '-':
                    self.formula = self.formula[1:]
                    self.update()
                else:
                    self.formula = ('-' + self.formula)
                    self.update()
            else:
                spl = self.save_resalt.split('=')
                second_arg =  spl[1]
                if second_arg[0] == '-':
                    self.formula = spl[1][1:]
                    self.update()
                else:
                    self.formula = ('-' + second_arg)
                    print(self.formula)
                    self.update()
        except:
            self.formula = 'Error'
            self.update()
            self.formula = '0'