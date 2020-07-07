import QApplication


def main_widget():
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('My first window')
    mainWidget.setFixedSize(500, 500)
    helloWorldLabel = QLabel('<h1>Привіт світ</h1>')
    helloWorldLabel.move(100, 250)
    mainWidget.show()
    return_code = app.exec()
    sys.exit(return_code)


def main_window():
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()