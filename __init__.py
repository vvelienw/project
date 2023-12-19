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
        self.second_form = SecondForm(True, False, False)
        self.second_form.show()
        self.close()


class SecondForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_third_form()
        else:
            print('Подумай ещё')

    def open_third_form(self):
        third_form = ThirdForm(True, False, False)
        third_form.show()
        self.close()


class ThirdForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label_3.setText('Готовы ли вы пожертвовать всем ради человечества?')
        self.radioButton.setText('Атака Титанов')
        self.radioButton_2.setText('Семь жизней')
        self.radioButton_3.setText('Заклятие')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_fourth_form()
        else:
            print('Подумай ещё')

    def open_fourth_form(self):
        fourth_form = FourthForm(True, False, False)
        fourth_form.show()
        self.close()


class FourthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label_3.setText('Совести-то у меня вагон, а вот времени нету')
        self.radioButton.setText('Мимино')
        self.radioButton_2.setText('Афоня')
        self.radioButton_3.setText('Белое солнце пустыни')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_fith_form()
        else:
            print('Подумай ещё')

    def open_fith_form(self):
        fith_form = FithForm(True, False, False)
        fith_form.show()
        self.close()


class FithForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label_3.setText('Невиноватая я, он сам пришел!')
        self.radioButton.setText('Ирония судьбы')
        self.radioButton_2.setText('Титаник')
        self.radioButton_3.setText('Бриллиантовая рука')
        self.radioButton.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_sixth_form()
        else:
            print('Подумай ещё')

    def open_sixth_form(self):
        sixth_form = SixthForm(True, False, False)
        sixth_form.show()
        self.close()


class SixthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label_3.setText('Хочешь сделать хорошо - сделай сам!')
        self.radioButton.setText('Пятый элемент')
        self.radioButton_2.setText('Игра престолов')
        self.radioButton_3.setText('Клон')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_seventh_form()
        else:
            print('Подумай ещё')

    def open_seventh_form(self):
        seventh_form = SeventhForm(True, False, False)
        seventh_form.show()
        self.close()


class SeventhForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Где не играл этот актёр?')
        self.label_2.setText('Тип задания 2')
        self.label_3.setText('Александр Петров')
        self.radioButton.setText('Лёд')
        self.radioButton_2.setText('Анна')
        self.radioButton_3.setText('Снежная королева')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[1]))

    def run(self, vern):
        if vern:
            self.open_eighth_form()
        else:
            print('Подумай ещё')

    def open_eighth_form(self):
        eighth_form = EighthForm(True, False, False)
        eighth_form.show()
        self.close()


class EighthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Где не играл этот актёр?')
        self.label_2.setText('Тип задания 2')
        self.label_3.setText('Леонардо ДиКаприо')
        self.radioButton.setText('Остров проклятых')
        self.radioButton_2.setText('Матрица')
        self.radioButton_3.setText('Титаник')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_ninth_form()
        else:
            print('Подумай ещё')

    def open_ninth_form(self):
        ninth_form = NinthForm(True, False, False)
        ninth_form.show()
        self.close()


class NinthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Где не играл этот актёр?')
        self.label_2.setText('Тип задания 2')
        self.label_3.setText('Том Фелтон')
        self.radioButton.setText('Судная ночь')
        self.radioButton_2.setText('Гарри Поттер')
        self.radioButton_3.setText('Флэш')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_ninth_form()
        else:
            print('Подумай ещё')

    def open_ninth_form(self):
        ninth_form = NinthForm(True, False, False)
        ninth_form.show()
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
