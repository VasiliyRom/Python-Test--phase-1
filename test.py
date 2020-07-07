def vidsotok(self, text):
        try:
            first_arg = self.editArea.text().split('%')[0]
            if self.oper == '+' or self.oper == '-':
                resalt = first_arg.split(self.oper)
                #print(self.editArea.text()[:-1])
                self.editArea.setText(
                    str(float(resalt[0]) / 100 * float(resalt[1])))
            else:
                self.editArea.setText('Error')
        except:
            self.editArea.setText('Error')



arg = self.formula.split('%')[0]
            resalt = arg.split(self.oper)
            if self.oper == '+':
                self.formula = str(float(resalt[0]) + (float(resalt[0]) / 100 * float(resalt[1])))
            elif self.oper == '-':
                self.formula = str(float(resalt[0]) - (float(resalt[0]) / 100 * float(resalt[1])))

            self.update()
            self.label_3.setText(self.formula)
            self.formula = '0'


    def add_oper(self, inst):
        self.oper = str(inst)

    def calc(self):
        try:
            print('++++++++')
            print(self.editArea.text()[:-1])
            value = self.editArea.text()[:-1]
            spl = value.split(self.oper)
            if self.oper == '+':
                if spl[0] == float or spl[0] == float:
                    resalt = float(spl[0]) + float(spl[1])
                else:
                    resalt = int(spl[0]) + int(spl[1])
            elif self.oper == '-':
                if spl[0] == float or spl[0] == float:
                    resalt = float(spl[0]) - float(spl[1])
                else:
                    resalt = int(spl[0]) - int(spl[1])
            elif self.oper == '*':
                if spl[0] == float or spl[0] == float:
                    resalt = float(spl[0]) * float(spl[1])
                else:
                    resalt = int(spl[0]) * int(spl[1])
            elif self.oper == '/':
                if spl[0] == float or spl[0] == float:
                    resalt = float(spl[0]) / float(spl[1])
                else:
                    resalt = int(spl[0]) / int(spl[1])

            self.editArea.setText(self.editArea.text() + str(resalt))
            print('------')
            #self.button.text = '0'  #обнуление, но не работает
        except:
            self.editArea.setText('Error')

    def step(self, text):
        try:
            if self.editArea.text() == '0' and text == 'x^2':
                self.editArea.setText('0')
            else:
                resalt = self.editArea.text()[:-3]
                self.editArea.setText(resalt + '^2=')
                self.editArea.setText(self.editArea.text() +
                                      str(float(resalt) * float(resalt)))
        except:
            self.editArea.setText('Error')







    def maynes(self, text):
        try:
            if self.editArea.text() == '0' and text == '+/-':
                self.editArea.setText('0')
                print('\\\\\\\\')
            elif '=' not in self.editArea.text():
                if self.editArea.text()[0] == '-':
                    self.editArea.setText(self.editArea.text()[1:-3])
                else:
                    self.editArea.setText('-' + self.editArea.text()[:-3])
            elif '=' in self.editArea.text():
                self.editArea.setText(self.editArea.text()[:-3])
                spl = self.editArea.text().split('=')
                first_arg = spl[0]
                second_arg = spl[1]
                if second_arg[0] == '-':
                    print(spl[1])
                    self.editArea.setText(spl[0] + '=' + spl[1][1:])
                    print(self.editArea.text())
                else:
                    self.editArea.setText(spl[0] + '=' + '-' + spl[1])
                    print(self.editArea.text())
        except:
            self.editArea.setText('Error')

    def change_text(self, text):
        try:
            print(self.editArea.text())
            if self.editArea.text() == 'Error':
                self.editArea.setText(text)
            elif self.editArea.text() == '0' and text == '%':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '=':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '+/-':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == 'x^2':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '+':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '-':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '*':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text == '/':
                self.editArea.setText('0')
            elif self.editArea.text() == '0' and text != '.':
                self.editArea.setText(text)
            elif self.editArea.text() == '0' and text == '.':
                self.editArea.setText(self.editArea.text() + text)
            elif self.editArea.text() != '0':
                self.editArea.setText(self.editArea.text() + text)
        except:
            self.editArea.setText('Error')




    def c_del(self):
        try:
            self.editArea.setText('0')
        except:
            self.editArea.setText('Error')
