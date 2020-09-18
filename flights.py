import sys, psycopg2
from functools import partial
from werkzeug.security import generate_password_hash, check_password_hash
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QPushButton,
                             QLineEdit, QLabel, QListWidget, QComboBox, QMessageBox, QCalendarWidget)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Плани польотів')
        self.setGeometry(500, 400, 400, 200)
        self.main_menu()

    def main_menu(self):
        root_widget = QWidget()
        add_user = QPushButton('Зареєструватися')
        login = QPushButton('Ввiйти')

        HLayout = QHBoxLayout()
        HLayout.addWidget(add_user)
        HLayout.addWidget(login)

        add_user.clicked.connect(self.new_user)
        login.clicked.connect(self.login)

        root_widget.setLayout(HLayout)
        self.setCentralWidget(root_widget)

    def new_user(self):
        n_user = QWidget()
        label1 = QLabel('Логін', self)
        label2 = QLabel('Ім\'я', self)
        label3 = QLabel('Прізвище', self)
        label4 = QLabel('Телефон', self)
        label5 = QLabel('Ел. пошта', self)
        label6 = QLabel('Пароль', self)
        label7 = QLabel('Підтвердити пароль', self)

        VLayout = QVBoxLayout()
        VLayout.addWidget(label1)
        VLayout.addWidget(label2)
        VLayout.addWidget(label3)
        VLayout.addWidget(label4)
        VLayout.addWidget(label5)
        VLayout.addWidget(label6)
        VLayout.addWidget(label7)

        RLayout = QVBoxLayout()
        self.username = QLineEdit()
        first_name = QLineEdit()
        last_name = QLineEdit()
        self.tel = QLineEdit('+380')
        self.email = QLineEdit()
        self.pwd1 = QLineEdit()
        self.pwd2 = QLineEdit()

        RLayout.addWidget(self.username)
        RLayout.addWidget(first_name)
        RLayout.addWidget(last_name)
        RLayout.addWidget(self.tel)
        RLayout.addWidget(self.email)
        RLayout.addWidget(self.pwd1)
        RLayout.addWidget(self.pwd2)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(VLayout)
        mainlayout.addLayout(RLayout)

        btn_ok = QPushButton('OK', self)

        btn_main_menu = QPushButton('Назад в головне меню', self)
        rootlayout = QVBoxLayout()
        rootlayout.addLayout(mainlayout)
        rootlayout.addWidget(btn_ok)
        rootlayout.addWidget(btn_main_menu)

        n_user.setLayout(rootlayout)
        self.setCentralWidget(n_user)
        btn_main_menu.clicked.connect(self.main_menu)

        btn_ok.clicked.connect(partial(self.save_user, self.username, first_name, last_name,
                                       self.tel, self.email, self.pwd1, self.pwd2))

    def rec_sql(self, text, parameters):
        try:
            connection = psycopg2.connect(host='localhost', database='postgres', port=5432,
                                          user='postgres', password='1234')
            cursor = connection.cursor()
            cursor.execute(text, parameters)

            if text.split()[0] == 'SELECT':
                result = cursor.fetchall()
                cursor.close()
                connection.close()
                return result
            elif text.split()[0] == 'INSERT' or text.split()[0] == 'UPDATE' or text.split()[0] == 'DELETE':
                connection.commit()
                cursor.close()
                connection.close()
                print('okkkkk')
                return None
        except Exception as error:
            print(error)

    def validation_tel(self, tel):
        if tel[1:].isdigit() and tel[:4] == '+380' and len(tel) == 13:
            return True
        else:
            return False

    def validation_mail(self, email):
        if '@' in email and '.' in email:
            return True
        else:
            return False

    def save_user(self, username, first_name, last_name, tel, email, pwd1, pwd2):
        if username.text() != '' and first_name.text() != '' and last_name.text() != '':
            if pwd1.text() == pwd2.text():
                if self.validation_mail(email.text()) is True:
                    if self.validation_tel(tel.text()) is True:
                        user = self.rec_sql(f"SELECT * FROM users WHERE username=(%s)", (username.text(), ))
                        if len(user) != 0:
                            self.username.clear()
                            self.username.setPlaceholderText('Логін зайнятий')
                        else:
                            self.rec_sql(f"INSERT INTO users(username, first_name, last_name, email, tel, "
                                         f"password_hash, admin) values(%s, %s, %s, %s, %s, %s, %s)",
                                         (username.text(), first_name.text().capitalize(), last_name.text().capitalize(),
                                          email.text().capitalize(), tel, self.set_password(pwd1.text()), False))
                            self.main_menu()
                    else:
                        self.tel.clear()
                        self.tel.setPlaceholderText('Невірний формат чи не починається на +380')
                else:
                    self.email.clear()
                    self.email.setPlaceholderText('Невірний формат')
        else:
            self.pwd1.clear()
            self.pwd2.clear()
            self.pwd1.setPlaceholderText('Всі поля повинні бути заповнені')

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, pwd_hash, pwd):
        return check_password_hash(pwd_hash, pwd)

    def login(self):
        log = QWidget()
        user = QLineEdit()
        self.pwd = QLineEdit()
        label1 = QLabel('Логін', self)
        label2 = QLabel('Пароль', self)

        ok = QPushButton('OK', self)
        btn_main_menu = QPushButton('Назад в головне меню', self)

        LLayout = QVBoxLayout()
        LLayout.addWidget(label1)
        LLayout.addWidget(label2)

        RLayout = QVBoxLayout()
        RLayout.addWidget(user)
        RLayout.addWidget(self.pwd)


        HLayout = QHBoxLayout()
        HLayout.addLayout(LLayout)
        HLayout.addLayout(RLayout)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(ok)
        VLayout.addWidget(btn_main_menu)

        log.setLayout(VLayout)
        self.setCentralWidget(log)

        btn_main_menu.clicked.connect(self.main_menu)
        ok.clicked.connect(partial(self.authorization, user, self.pwd))

    def authorization(self, user, pwd):
        user, pwd = user.text(), pwd.text()
        try:
            if user != '' and pwd != '':
                user_data = self.rec_sql(f"SELECT * FROM users WHERE username=(%s)", (user, ))
                print(user_data)
                if len(user_data) == 0 or not self.check_password(user_data[0][2], pwd):
                    self.pwd.clear()
                    self.pwd.setPlaceholderText('Невірний логін чи пароль')
                else:
                    self.user_data = user_data[0]

                    if self.user_data[7] == True:
                        self.admin_account()
                    else:
                        self.user_account()
        except:
            print('error')

    def admin_account(self):
        self.change = False
        root_widget = QWidget()
        VBox = QVBoxLayout()
        HBox = QHBoxLayout()
        HBox1 = QHBoxLayout()
        HBox2 = QHBoxLayout()
        username = QLabel(f'<h3>Привіт, {self.user_data[3]} {self.user_data[4]} (admin)</h3>')

        admin = QPushButton('Добавити користувача до адмінів')
        info = QPushButton('Моя інформація')
        date = QPushButton('Переглянути дату')
        change = QPushButton('Змінити час чи дату')
        myinfo_change = QPushButton('Змiнити мою інформацію')
        password_change = QPushButton('Змiнити пароль')
        main = QPushButton('Вийти')

        HBox.addWidget(date)
        HBox.addWidget(change)
        HBox1.addWidget(admin)
        HBox1.addWidget(password_change)
        HBox2.addWidget(info)
        HBox2.addWidget(myinfo_change)

        VBox.addWidget(username)
        VBox.addLayout(HBox)
        VBox.addLayout(HBox1)
        VBox.addLayout(HBox2)
        VBox.addWidget(main)
        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)

        admin.clicked.connect(self.user_admin)
        info.clicked.connect(partial(self.user_info, self.user_data))
        date.clicked.connect(self.select_date)
        change.clicked.connect(self.change_date)
        myinfo_change.clicked.connect(self.myinfo_chan)
        password_change.clicked.connect(self.change_password)
        main.clicked.connect(self.exit_account)

    def myinfo_chan(self):
        widget = QWidget()
        label1 = QLabel('Змiнити номер тел.', self)
        label2 = QLabel('Змiнити email', self)
        VLayout = QVBoxLayout()
        VLayout.addWidget(label1)
        VLayout.addWidget(label2)

        RLayout = QVBoxLayout()
        self.change_tel = QLineEdit()
        self.change_email = QLineEdit()

        RLayout.addWidget(self.change_tel)
        RLayout.addWidget(self.change_email)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(VLayout)
        mainlayout.addLayout(RLayout)

        btn_ok = QPushButton('OK', self)

        btn_main_menu = QPushButton('Назад', self)
        rootlayout = QVBoxLayout()
        rootlayout.addLayout(mainlayout)
        rootlayout.addWidget(btn_ok)
        rootlayout.addWidget(btn_main_menu)

        widget.setLayout(rootlayout)
        self.setCentralWidget(widget)
        btn_ok.clicked.connect(self.validation_info)
        if self.user_data[7] == True:
            btn_main_menu.clicked.connect(self.admin_account)
        else:
            btn_main_menu.clicked.connect(self.user_account)

    def validation_info(self):
        tel = self.change_tel.text()
        email = self.change_email.text()
        if tel != '':
            if self.validation_tel(tel) is not True:
                self.change_tel.clear()
                self.change_tel.setPlaceholderText('Невірний формат чи не починається на +380')
            else:
                choice = QMessageBox.question(self, 'Змiна номеру тел.', 'Ви бажаєте змiнити номер телефону?',
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.rec_sql(f"UPDATE users SET tel=(%s) WHERE username=(%s)",
                                 (tel, self.user_data[1]))
        if email != '':
            if self.validation_mail(email) is not True:
                self.change_email.clear()
                self.change_email.setPlaceholderText('Невірний формат чи не починається на +380')
            else:
                choice = QMessageBox.question(self, 'Змiна електронної пошти', 'Ви бажаєте змiнити електронну пошту?',
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.rec_sql(f"UPDATE users SET email=(%s) WHERE username=(%s)",
                                 (email, self.user_data[1]))
        if self.user_data[7] == True:
            self.admin_account()
        else:
            self.user_account()

    def change_date(self):
        self.change = True
        self.select_date()

    def exit_account(self):
        choice = QMessageBox.question(self, 'Вихід', 'Ви дійсно бажаєта вийти з аккаунта?',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.main_menu()

    def user_admin(self):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('<h3>Виберіть користувача:</h3>')
        home = QPushButton('Назад')
        list = QListWidget()

        VBox.addWidget(label)
        VBox.addWidget(list)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)
        home.clicked.connect(self.admin_account)

        data = self.rec_sql(f"SELECT * FROM users", (self.user_data[1],))
        for i in data:
            if i[7] != True:
                list.addItem(f'Логін: {i[1]}\n{i[3]} {i[4]}\n')
        list.itemClicked.connect(self.replase_admin)

    def replase_admin(self, item):
        name = item.text().split('\n')[0].split(': ')[1]
        choice = QMessageBox.question(self, 'Warning!',
                                f"Ви дійсно бажаєта добавити користувача {name} до анміністраторів?",
                                QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.rec_sql(f"UPDATE users SET admin=true WHERE username=(%s)", (name,))
            self.admin_account()

    def user_account(self):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        HBox = QHBoxLayout()
        username = QLabel(f'<h3>Привіт, {self.user_data[3]} {self.user_data[4]}<h3>')

        flight_record = QPushButton('Записатись на політ')
        flight_info = QPushButton('Мої польоти')
        info = QPushButton('Моя інформація')
        password_change = QPushButton('Змiнити пароль')
        myinfo_change = QPushButton('Змiнити мою інформацію')
        main = QPushButton('Вийти')

        HBox.addWidget(username)
        VBox.addWidget(flight_record)
        VBox.addWidget(flight_info)
        VBox.addWidget(info)
        VBox.addWidget(myinfo_change)
        VBox.addWidget(password_change)
        VBox.addWidget(main)

        HBox.addLayout(VBox)
        root_widget.setLayout(HBox)
        self.setCentralWidget(root_widget)

        flight_record.clicked.connect(self.select_date)
        flight_info.clicked.connect(self.my_flight)
        info.clicked.connect(partial(self.user_info, self.user_data))
        myinfo_change.clicked.connect(self.myinfo_chan)
        password_change.clicked.connect(self.change_password)
        main.clicked.connect(self.exit_account)

    def change_password(self):
        widget = QWidget()
        label1 = QLabel('Новий пароль', self)
        label2 = QLabel('Пiдтвердiть пароль', self)
        VLayout = QVBoxLayout()
        VLayout.addWidget(label1)
        VLayout.addWidget(label2)

        RLayout = QVBoxLayout()
        self.pwd1 = QLineEdit()
        self.pwd2 = QLineEdit()

        RLayout.addWidget(self.pwd1)
        RLayout.addWidget(self.pwd2)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(VLayout)
        mainlayout.addLayout(RLayout)

        btn_ok = QPushButton('OK', self)

        btn_main_menu = QPushButton('Назад', self)
        rootlayout = QVBoxLayout()
        rootlayout.addLayout(mainlayout)
        rootlayout.addWidget(btn_ok)
        rootlayout.addWidget(btn_main_menu)

        widget.setLayout(rootlayout)
        self.setCentralWidget(widget)
        btn_ok.clicked.connect(self.confirm_pwd)
        if self.user_data[7] == True:
            btn_main_menu.clicked.connect(self.admin_account)
        else:
            btn_main_menu.clicked.connect(self.user_account)

    def confirm_pwd(self):
        if self.pwd1.text() != '' and self.pwd2.text() != '':
            if self.pwd1.text() != self.pwd2.text():
                self.pwd1.clear()
                self.pwd2.clear()
                self.pwd2.setPlaceholderText('Паролi не спiвпадають')
            else:
                choice = QMessageBox.question(self, 'Змiна паролю', 'Ви бажаєте змiнити пароль?',
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    self.rec_sql(f"UPDATE users SET password_hash=(%s) WHERE username=(%s)",
                                 (self.set_password(self.pwd1.text()), self.user_data[1]))
                if self.user_data[7] == True:
                    self.admin_account()
                else:
                    self.user_account()

    def user_info(self, user):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('<h2>Інформація</h2>')
        VBox.addWidget(label)
        if type(user) is not tuple:
            name = user.text().split('\n')[0].split(': ')[1]
            user = self.rec_sql(f"SELECT * FROM users WHERE username=(%s)", (name,))[0]

        login = QLabel(f'<h3>Логін: {user[1]}</h3>')
        admin = QLabel(f'<h3>Адмін:{user[7]}</h3>')
        id = QLabel(f'<h3>ID: {user[0]}</h3>')
        first_name = QLabel(f'<h3>І\'мя: {user[3]}</h3>')
        last_name = QLabel(f'<h3>Прізвище: {user[4]}</h3>')
        telefon = QLabel(f'<h3>Телефон: {user[5]}</h3>')
        email = QLabel(f'<h3>Email: {user[6]}</h3>')
        home = QPushButton('Назад')

        VBox.addWidget(login)
        VBox.addWidget(id)
        VBox.addWidget(admin)
        VBox.addWidget(first_name)
        VBox.addWidget(last_name)
        VBox.addWidget(telefon)
        VBox.addWidget(email)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)
        if self.user_data[7] == True:
            home.clicked.connect(self.admin_account)
        else:
            home.clicked.connect(self.user_account)

    def my_flight(self):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('<h3>Результат:</h3>')
        home = QPushButton('Назад')
        list = QListWidget()

        VBox.addWidget(label)
        VBox.addWidget(list)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)
        home.clicked.connect(self.user_account)
        data = self.rec_sql(f"SELECT * FROM flights WHERE username=(%s)", (self.user_data[1], ))

        if len(data) == 0:
            list.addItem('Вильоти відсутні')
        else:
            for i in data:
                list.addItem(f'Дата: {i[2]}\nЧас: {i[3]}\n')

    def select_date(self):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('<h3>Виберіть дату</h3>')
        self.label1 = QLabel()
        home = QPushButton('Назад')
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        VBox.addWidget(label)
        VBox.addWidget(self.calendar)
        VBox.addWidget(self.label1)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)

        if self.user_data[7] == True:
            self.calendar.selectionChanged.connect(self.show_item)
            home.clicked.connect(self.admin_account)
        else:
            self.calendar.selectionChanged.connect(self.select_data)
            home.clicked.connect(self.user_account)

    def show_item(self):
        data = self.calendar.selectedDate().toPyDate()
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel(f'<h3>Результат на: {data}</h3>')
        home = QPushButton('Назад')
        list = QListWidget()

        VBox.addWidget(label)
        VBox.addWidget(list)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)
        home.clicked.connect(self.select_date)

        res = self.rec_sql(f"SELECT * FROM flights WHERE date=(%s)", (data,))
        for i in res:
            self.del_date = data
            list.addItem(f'Логін: {i[1]}\n{i[3]}\n')

        if self.change is True:
            list.itemClicked.connect(self.select_d)
        else:
            list.itemClicked.connect(self.user_info)

    def select_d(self, user):
        self.login = user.text().split('\n')[0].split(': ')[1]
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('<h3>Виберіть дату</h3>')
        self.label1 = QLabel()
        home = QPushButton('Назад')
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        VBox.addWidget(label)
        VBox.addWidget(self.calendar)
        VBox.addWidget(self.label1)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)


        self.calendar.selectionChanged.connect(self.select_data)
        home.clicked.connect(self.admin_account)

    def select_data(self):
        self.data = self.calendar.selectedDate().toPyDate()

        self.flight_data = self.rec_sql(f"SELECT * FROM flights WHERE date=(%s)", (self.data, ))
        if len(self.flight_data) == 6:
            self.label1.setText('<h3>Немає доступних вильотів. Виберіть іншу дату</h3>')
        else:
            self.select_time()

    def select_time(self):
        root_widget = QWidget()
        VBox = QVBoxLayout()
        label = QLabel('Виберіть час')
        self.error_label1 = QLabel()
        self.btn_save = QPushButton('Ok')
        home = QPushButton('Назад')

        combo = QComboBox(self)
        combo.addItem('09:00')
        combo.addItem('10:30')
        combo.addItem('12:00')
        combo.addItem('13:30')
        combo.addItem('15:00')
        combo.addItem('16:30')
        self.combo = '09:00:00'

        combo.activated[str].connect(self.on)

        VBox.addWidget(label)
        VBox.addWidget(combo)
        VBox.addWidget(self.error_label1)
        VBox.addWidget(self.btn_save)
        VBox.addWidget(home)

        root_widget.setLayout(VBox)
        self.setCentralWidget(root_widget)
        self.btn_save.clicked.connect(self.result)
        home.clicked.connect(self.user_account)

    def on(self, text):
        self.combo = f'{text}:00'

    def result(self):
        self.check = False
        self.error_label1.clear()
        if len(self.flight_data) == 0:
            self.save_choice()
        else:
            for i in self.flight_data:
                if str(i[3]) == self.combo:
                    self.check = True
                    self.error_label1.setText('Час зайнятий')
                    pass
            self.save_choice()

    def save_choice(self):
        if self.change is True and self.check is not True:
            choice = QMessageBox.question(self, 'Зберегти', 'Ви бажаєте продовжити?',
                                          QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                self.rec_sql(f"DELETE FROM flights WHERE username=(%s) AND date=(%s)",
                             (self.login, self.del_date))
                self.rec_sql(f"INSERT INTO flights(username, date, time) VALUES (%s, %s, %s)",
                             (self.login, self.data, self.combo))
                self.change = False
                self.admin_account()
        else:
            if self.check != True:
                    choice = QMessageBox.question(self, 'Зберегти', 'Ви бажаєте продовжити?',
                                                  QMessageBox.Yes | QMessageBox.No)
                    if choice == QMessageBox.Yes:
                        self.rec_sql(f"INSERT INTO flights(username, date, time) VALUES (%s, %s, %s)",
                                       (self.user_data[1], self.data, self.combo))

                        self.user_account()


def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)

if __name__ == '__main__':
    main_window()