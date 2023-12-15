import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QRadioButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.pushButton_2.clicked.connect(self.run)
        self.PushButton.clicked.connect(self.open_second_form)

    def run(self):
        print("Ну ладно. Приходи, когда будешь готов")


    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()
        self.close()


class SecondForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('untitled_1.ui', self)
        self.radioButton.clicked.connect(self.run)
        self.radioButton_3.clicked.connect(self.run)
        self.radioButton_2.clicked.connect(self.open_third_form)


    def run(self, vern):
        if vern:
            self.open_third_form()
        else:
            print('Подумай ещё')

    def open_third_form(self):
        self.third_form = SecondForm(self, "Данные для третьей формы")
        self.third_form.label_3.setText('Готовы ли вы пожертвовать всем ради человечества?')
        self.third_form.radioButton.setText('Атака Титанов')
        self.third_form.radioButton_2.setText('Семь жизней')
        self.third_form.radioButton_3.setText('Заклятие')
        self.radioButton_2.clicked.connect(lambda: self.run(False))
        self.radioButton_3.clicked.connect(lambda: self.run(False))
        self.radioButton.clicked.connect(lambda: self.run(True))
        self.third_form.show()
        self.close()

    def run(self, w):
        if w:
            self.open_third_form()
        else:
            print('Подумай ещё')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())