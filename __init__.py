import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QRadioButton
from PyQt5.QtGui import QPixmap


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
            self.open_tenth_form()
        else:
            print('Подумай ещё')

    def open_tenth_form(self):
        tenth_form = TenthForm(True, False, False)
        tenth_form.show()
        self.close()


class TenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Где не играла эта актриса?')
        self.label_2.setText('Тип задания 2')
        self.label_3.setText('Юлия Пересильд')
        self.radioButton.setText('Первые')
        self.radioButton_2.setText('Край')
        self.radioButton_3.setText('Вызов')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_eleventh_form()
        else:
            print('Подумай ещё')

    def open_eleventh_form(self):
        eleventh_form = EleventhForm(True, False, False)
        eleventh_form.show()
        self.close()


class EleventhForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Где не играла эта актриса?')
        self.label_2.setText('Тип задания 2')
        self.label_3.setText('Анжелина Джоли')
        self.radioButton.setText('За гранью')
        self.radioButton_2.setText('Турист')
        self.radioButton_3.setText('Монстр')
        self.radioButton.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_twelfth_form()
        else:
            print('Подумай ещё')

    def open_twelfth_form(self):
        twelfth_form = TwelfthForm(True, False, False)
        twelfth_form.show()
        self.close()


class TwelfthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Какой из этих фильмов...')
        self.label_2.setText('Тип задания 3')
        self.label_3.setText('Самый кассовый')
        self.radioButton.setText('Игра в кальмара')
        self.radioButton_2.setText('Начало')
        self.radioButton_3.setText('Унесённые ветром')
        self.radioButton.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_thirteenth_form()
        else:
            print('Подумай ещё')

    def open_thirteenth_form(self):
        thirteenth_form = ThirteenthForm(True, False, False)
        thirteenth_form.show()
        self.close()


class ThirteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Какой из этих фильмов...')
        self.label_2.setText('Тип задания 3')
        self.label_3.setText('Был выпущен раньше всех')
        self.radioButton.setText('Звонок')
        self.radioButton_2.setText('Холоп')
        self.radioButton_3.setText('Дивергент')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_fourteenth_form()
        else:
            print('Подумай ещё')

    def open_fourteenth_form(self):
        fourteenth_form = FourteenthForm(True, False, False)
        fourteenth_form.show()
        self.close()


class FourteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Какой из этих фильмов...')
        self.label_2.setText('Тип задания 3')
        self.label_3.setText('Самый новый')
        self.radioButton.setText('Одна')
        self.radioButton_2.setText('Бешенство')
        self.radioButton_3.setText('Помнить')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_fifteenth_form()
        else:
            print('Подумай ещё')

    def open_fifteenth_form(self):
        fifteenth_form = FifteenthForm(True, False, False)
        fifteenth_form.show()
        self.close()


class FifteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Какой из этих фильмов...')
        self.label_2.setText('Тип задания 3')
        self.label_3.setText('Самый не бюджетный')
        self.radioButton.setText('Русалочка')
        self.radioButton_2.setText('Форсаж 10')
        self.radioButton_3.setText('Аватар: Путь воды')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[1]))

    def run(self, vern):
        if vern:
            self.open_sixteenth_form()
        else:
            print('Подумай ещё')

    def open_sixteenth_form(self):
        sixteenth_form = SixteenthForm(True, False, False)
        sixteenth_form.show()
        self.close()


class SixteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Какой из этих фильмов...')
        self.label_2.setText('Тип задания 3')
        self.label_3.setText('Самый страшный')
        self.radioButton.setText('Иллюзия обмана')
        self.radioButton_2.setText('Домовой')
        self.radioButton_3.setText('Сплит')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[1]))

    def run(self, vern):
        if vern:
            self.open_seventeenth_form()
        else:
            print('Подумай ещё')

    def open_seventeenth_form(self):
        seventeenth_form = SeventeenthForm(True, False, False)
        seventeenth_form.show()
        self.close()


class SeventeenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Отгадай фильм по 3 словам')
        self.label_2.setText('Тип задания 4')
        self.label_3.setText('Кукуруза, космос, шкаф')
        self.radioButton.setText('Леон')
        self.radioButton_2.setText('Интерстеллар')
        self.radioButton_3.setText('Изгой')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_eighteenth_form()
        else:
            print('Подумай ещё')

    def open_eighteenth_form(self):
        eighteenth_form = EighteenthForm(True, False, False)
        eighteenth_form.show()
        self.close()


class EighteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Отгадай фильм по 3 словам')
        self.label_2.setText('Тип задания 4')
        self.label_3.setText('Клоун, револьвер, ток-шоу')
        self.radioButton.setText('Джокер')
        self.radioButton_2.setText('Оно')
        self.radioButton_3.setText('Ла-Ла Ленд')
        self.radioButton.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[2]))

    def run(self, vern):
        if vern:
            self.open_nineteenth_form()
        else:
            print('Подумай ещё')

    def open_nineteenth_form(self):
        nineteenth_form = NineteenthForm(True, False, False)
        nineteenth_form.show()
        self.close()


class NineteenthForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Отгадай фильм по 3 словам')
        self.label_2.setText('Тип задания 4')
        self.label_3.setText('Репетитор, камень, полуподвал')
        self.radioButton.setText('Жизнь Пи')
        self.radioButton_2.setText('Амели')
        self.radioButton_3.setText('Паразиты')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[0]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[1]))

    def run(self, vern):
        if vern:
            self.open_twentieth_form()
        else:
            print('Подумай ещё')

    def open_twentieth_form(self):
        twentieth_form = TwentiethForm(True, False, False)
        twentieth_form.show()
        self.close()


class TwentiethForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Отгадай фильм по 3 словам')
        self.label_2.setText('Тип задания 4')
        self.label_3.setText('Ребёнок, аэропорт, Новый Год')
        self.radioButton.setText('Гладиатор')
        self.radioButton_2.setText('Один дома 2')
        self.radioButton_3.setText('Гринч')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.open_twentithirst_form()
        else:
            print('Подумай ещё')

    def open_twentithirst_form(self):
        twentithirst_form = TwentithirstForm(True, False, False)
        twentithirst_form.show()
        self.close()


class TwentithirstForm(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        answers = args[:]
        uic.loadUi('untitled_1.ui', self)
        self.label.setText('Отгадай фильм по 3 словам')
        self.label_2.setText('Тип задания 4')
        self.label_3.setText('Грузия, горы, снег')
        self.radioButton.setText('Солдаты')
        self.radioButton_2.setText('Пусть идёт снег')
        self.radioButton_3.setText('Любовь и голуби')
        self.radioButton.clicked.connect(lambda: self.run(args[2]))
        self.radioButton_3.clicked.connect(lambda: self.run(args[1]))
        self.radioButton_2.clicked.connect(lambda: self.run(args[0]))

    def run(self, vern):
        if vern:
            self.close()
        else:
            print('Подумай ещё')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())