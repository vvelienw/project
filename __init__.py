import sys

import args as args
import self as self
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
        self.second_form = SecondForm(True, False, False)
        self.second_form.show()
        self.close()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_third_form()
        else:
            print('Подумай ещё')

    def open_third_form(self):
        third_form = ThirdForm(True, False, False)
        third_form.show()
        self.close()

class ThirdForm(QWidget):
     def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.third_form.label_3.setText('Готовы ли вы пожертвовать всем ради человечества?')
        self.third_form.radioButton.setText('Заклятие')
        self.third_form.radioButton_2.setText('Семь жизней')
        self.third_form.radioButton_3.setText('Атака Титанов')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

     def run(self, vern):
         if vern:
             self.open_second_form()
         else:
             print('Подумай ещё')

     def open_second_form(self):
         second_form = SecondForm()
         second_form.show()
         self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())