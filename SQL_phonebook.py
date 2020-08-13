import sys, psycopg2
from functools import partial
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow,
                             QPushButton, QLineEdit, QLabel, QListWidget, QListWidgetItem)

connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='1234')

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Телефонна книга')
        self.setGeometry(500, 400, 400, 200)
        self.main_menu()

    def main_menu(self):
        root_widget = QWidget()
        self.btn_new = QPushButton('Додати запис до тел. книги', self)
        self.btn_search = QPushButton('Пошук контактів', self)
        self.btn_del = QPushButton('Видалити запис по номеру телефону', self)
        HLayout = QVBoxLayout()
        HLayout.addWidget(self.btn_new)
        HLayout.addWidget(self.btn_search)
        HLayout.addWidget(self.btn_del)
        root_widget.setLayout(HLayout)
        self.setCentralWidget(root_widget)

        self.btn_new.clicked.connect(self.add_contact)
        self.btn_search.clicked.connect(self.search_contact)
        self.btn_del.clicked.connect(self.delete_contact)

    def add_contact(self):
        new_contact_widget = QWidget()
        label1 = QLabel('Ім\'я', self)
        label2 = QLabel('Прізвище', self)
        label3 = QLabel('Телефон', self)
        label4 = QLabel('Місто', self)
        VLayout = QVBoxLayout()
        VLayout.addWidget(label1)
        VLayout.addWidget(label2)
        VLayout.addWidget(label3)
        VLayout.addWidget(label4)

        RLayout = QVBoxLayout()
        first_name = QLineEdit()
        last_name = QLineEdit()
        tel = QLineEdit()
        city = QLineEdit()
        RLayout.addWidget(first_name)
        RLayout.addWidget(last_name)
        RLayout.addWidget(tel)
        RLayout.addWidget(city)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(VLayout)
        mainlayout.addLayout(RLayout)

        self.btn_ok = QPushButton('OK', self)

        btn_main_menu = QPushButton('Назад в головне меню', self)
        rootlayout = QVBoxLayout()
        rootlayout.addLayout(mainlayout)
        rootlayout.addWidget(self.btn_ok)
        rootlayout.addWidget(btn_main_menu)
        new_contact_widget.setLayout(rootlayout)
        self.setCentralWidget(new_contact_widget)

        self.btn_ok.clicked.connect(partial(self.new_contact, first_name, last_name, tel, city))
        btn_main_menu.clicked.connect(self.main_menu)

    def new_contact(self, first_name, last_name, tel, city):
        try:
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO contacts(first_name, last_name, tel, city) values(%s, %s, %s, %s)',
                           (first_name.text(), last_name.text(), tel.text(), city.text()))

            connection.commit()
            self.btn_ok.setEnabled(False)
        except:
            connection.rollback()
            self.btn_ok.setEnabled(False)
            self.btn_ok.setText('Error')

    def search_contact(self):
        search_widget = QWidget()
        self.btn_f_name = QPushButton('Пошук по імені', self)
        self.btn_l_name = QPushButton('Пошук по прізвищу', self)
        self.btn_tel = QPushButton('Пошук по номеру тел.', self)
        self.btn_city = QPushButton('Пошук по місту', self)
        self.btn_main_menu = QPushButton('Назад в головне меню', self)
        SearchLayout = QVBoxLayout()

        SearchLayout.addWidget(self.btn_f_name)
        SearchLayout.addWidget(self.btn_l_name)
        SearchLayout.addWidget(self.btn_tel)
        SearchLayout.addWidget(self.btn_city)
        SearchLayout.addWidget(self.btn_main_menu)
        search_widget.setLayout(SearchLayout)
        self.setCentralWidget(search_widget)

        self.btn_f_name.clicked.connect(partial(self.search, 'Ім\'я'))
        self.btn_l_name.clicked.connect(partial(self.search, 'Прізвище'))
        self.btn_tel.clicked.connect(partial(self.search, 'Телефон'))
        self.btn_city.clicked.connect(partial(self.search, 'Місто'))
        self.btn_main_menu.clicked.connect(self.main_menu)

    def search(self, btn):
        widget = QWidget()
        self.editArea = QLineEdit()
        label = QLabel(btn, self)
        btn_ok = QPushButton('OK', self)

        search = QHBoxLayout()
        search.addWidget(label)
        search.addWidget(self.editArea)
        search.addWidget(btn_ok)
        self.search_resalt = QListWidget()

        HLayout1 = QHBoxLayout()

        HLayout1.addWidget(self.search_resalt)

        self.rootLayout = QVBoxLayout()
        self.rootLayout.addLayout(search)
        self.rootLayout.addLayout(HLayout1)
        self.rootLayout.addWidget(self.btn_main_menu)

        widget.setLayout(self.rootLayout)
        self.setCentralWidget(widget)

        btn_ok.clicked.connect(partial(self.resalt_search, btn))
        self.editArea.returnPressed.connect(btn_ok.click)
        self.btn_main_menu.clicked.connect(self.main_menu)

    def resalt_search(self, btn):
        try:
            write_text = self.editArea.text()
            cursor = connection.cursor()
            if btn == 'Ім\'я':
                cursor.execute(f"SELECT * FROM contacts WHERE first_name=(%s)", (write_text.capitalize(), ))
            elif btn == 'Прізвище':
                cursor.execute(f"SELECT * FROM contacts WHERE last_name=(%s)", (write_text.capitalize(), ))
            elif btn == 'Телефон':
                cursor.execute(f"SELECT * FROM contacts WHERE tel=(%s)", (write_text, ))
            elif btn == 'Місто':
                cursor.execute(f"SELECT * FROM contacts WHERE city=(%s)", (write_text.capitalize(), ))
            result = cursor.fetchall()
            print(result)
            for i in result:
                self.search_resalt.addItem(f"Ім\'я: {i[1]}\nПрізвище: {i[2]}\n"
                                          f"Телефон: {i[3]}\nМісто: {i[4]}\n")
        except:
            self.search_resalt.setText('Error')

    def delete_contact(self):
        delete_widget = QWidget()

        self.editArea = QLineEdit()
        label = QLabel('Телефон', self)
        self.btnDel_ok = QPushButton('OK', self)
        deleteLayout = QHBoxLayout()
        deleteLayout.addWidget(label)
        deleteLayout.addWidget(self.editArea)
        deleteLayout.addWidget(self.btnDel_ok)

        VLayout = QVBoxLayout()
        VLayout.addLayout(deleteLayout)
        self.delete_resalt = QListWidget()
        VLayout.addWidget(self.delete_resalt)
        self.btn_main_menu = QPushButton('Назад в головне меню', self)
        VLayout.addWidget(self.btn_main_menu)

        delete_widget.setLayout(VLayout)
        self.setCentralWidget(delete_widget)

        self.btnDel_ok.clicked.connect(self.resalt_delete)
        self.editArea.returnPressed.connect(self.btnDel_ok.click)
        self.btn_main_menu.clicked.connect(self.main_menu)

    def resalt_delete(self):
        try:
            tel = self.editArea.text()
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM contacts WHERE tel=(%s)", (tel, ))
            result = cursor.fetchall()
            for i in result:
                self.delete_resalt.addItem(f"Ім\'я: {i[1]}\nПрізвище: {i[2]}\n"
                                            f"Телефон: {i[3]}\nМісто: {i[4]}\n")
            # можна не робити але зробив
            self.telefon = tel
            self.delete_resalt.itemClicked.connect(self.delete_item)
        except:
            self.delete_resalt.setText('Error')

    def delete_item(self, item: QListWidgetItem):  # це з нета бо незнав як підципити конект
        try:
            last_name = item.text().split('\n')[1].split(': ')[1]

            cursor = connection.cursor()
            cursor.execute("DELETE FROM contacts WHERE last_name=(%s) AND tel=(%s)", (last_name, self.telefon))
            connection.commit()
            cursor.close()

            self.delete_resalt.setEnabled(False)
            self.btnDel_ok.setText('Delete')
            self.btnDel_ok.setEnabled(False)
        except:
            connection.rollback()
            cursor.close()
            self.delete_resalt.setText('Error')



def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)

if __name__ == '__main__':
    main_window()