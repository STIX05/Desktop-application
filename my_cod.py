import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt

global score 
score = 0
class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Вступление')
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Приветвствую в моем приложении!')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
 
    def init_handlers(self):  # обработка нажатия для октрытия 2 окна

        self.button.clicked.connect(self.show_window_2)
 
    def show_window_2(self):  # открытие 2  окна 
        self.w2 = Window2()
        #self.w1 = Window1()
        self.hide()
        self.w2.show()
        #self.w1.hide()
    

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Вступление')
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Эта программа создана для поддержки людей во время карантина! \n Тест состоит из 10 вопросов. \n Удачи!')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Понятно')
        self.button.show()
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 3 окна
        self.button.clicked.connect(self.show_window_3)
 
    def show_window_3(self):  # открытие 3  окна 
        self.w3 = Window3()
        #self.w2 = Window2()
        self.hide()
        self.w3.show()
        #self.w2.hide()
 
class Window3(QWidget):
    def __init__(self):
        super(Window3, self).__init__()
        self.setWindowTitle('Вопрос 1')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Как вы проводите свой карантин?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Весело")
        self.radio_button_2 = QRadioButton("Скучно")
        self.radio_button_3 = QRadioButton("Ну такое")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 4 окна
        self.button.clicked.connect(self.show_window_4)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Весело":
            score +=1
        if button.text() =="Скучно":
            score -=1

    def show_window_4(self):  # открытие 4  окна 
        self.w4 = Window4()
        #self.w3 = Window3()
        self.hide()
        self.w4.show()
        #self.w3.hide()

       
class Window4(QWidget):
    def __init__(self):
        super(Window4, self).__init__()
        self.setWindowTitle('Вопрос 2')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Нравится ли вам на карантине?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Да)")
        self.radio_button_2 = QRadioButton("Нет(")
        self.radio_button_3 = QRadioButton("Не могу сказать")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 5 окна
        self.button.clicked.connect(self.show_window_5)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Нет(":
            score +=1
        if button.text() =="Да)":
            score -=1

    def show_window_5(self):  # открытие 5  окна 
        self.w5 = Window5()
        #self.w4 = Window4()
        self.hide()
        self.w5.show()
        #self.w4.hide()

class Window5(QWidget):
    def __init__(self):
        super(Window5, self).__init__()
        self.setWindowTitle('Вопрос 3')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Занимаетесь ли вы спортом на карантине?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Да")
        self.radio_button_2 = QRadioButton("Нет")
        self.radio_button_3 = QRadioButton("Не могу сказать")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 6 окна
        self.button.clicked.connect(self.show_window_6)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Да":
            score +=1
        if button.text() =="Нет":
            score -=1

    def show_window_6(self):  # открытие 6  окна 
        self.w6 = Window6()
        #self.w5 = Window5()
        self.hide()
        self.w6.show()
        #self.w5.hide()

class Window6(QWidget):
    def __init__(self):
        super(Window6, self).__init__()
        self.setWindowTitle('Вопрос 4')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Нарушали ли вы самоизоляцию?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Да, было дело)")
        self.radio_button_2 = QRadioButton("Нет, вы что, хотите заразиться?")
        self.radio_button_3 = QRadioButton("Не могу ответить")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 7 окна
        self.button.clicked.connect(self.show_window_7)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Нет, вы что, хотите заразиться?":
            score +=1
        if button.text() =="Да, было дело)":
            score -=1

    def show_window_7(self):  # открытие 7  окна 
        self.w7 = Window7()
        #self.w6 = Window6()
        self.hide()
        self.w7.show()
        #self.w6.hide()

class Window7(QWidget):
    def __init__(self):
        super(Window7, self).__init__()
        self.setWindowTitle('Вопрос 5')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Появились ли новые знакомые на карантине?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Да, появились")
        self.radio_button_2 = QRadioButton("Увы нет, (я и сам себе друг)")
        self.radio_button_3 = QRadioButton("Не могу отвтетить")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 8 окна
        self.button.clicked.connect(self.show_window_8)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Да, появились":
            score +=1
        if button.text() =="Увы нет, (я и сам себе друг)":
            score -=1

    def show_window_8(self):  # открытие 8  окна 
        self.w8 = Window8()
        #self.w7 = Window7()
        self.hide()
        self.w8.show()
        #self.w7.hide()

class Window8(QWidget):
    def __init__(self):
        super(Window8, self).__init__()
        self.setWindowTitle('Вопрос 6')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Работали ли вы дистанционно?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Да, мне понравилось")
        self.radio_button_2 = QRadioButton("Нет, мне было слишком лень")
        self.radio_button_3 = QRadioButton("Я задрот!")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 9 окна
        self.button.clicked.connect(self.show_window_9)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Да, мне понравилось":
            score +=1
        if button.text() =="Нет, мне было слишком лень":
            score -=1
        if button.text() =="Я задрот!":
            score -=0.5

    def show_window_9(self):  # открытие 9  окна 
        self.w9 = Window9()
        #self.w8 = Window8()
        self.hide()
        self.w9.show()
        #self.w8.hide()

class Window9(QWidget):
    def __init__(self):
        super(Window9, self).__init__()
        self.setWindowTitle('Вопрос 7')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Чем развлекаетесь на карантине?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Играю в компуктер")
        self.radio_button_2 = QRadioButton("Работаю")
        self.radio_button_3 = QRadioButton("Учусь")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 10 окна
        self.button.clicked.connect(self.show_window_10)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)
    
    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Учусь":
            score +=1
        if button.text() =="Играю в компуктер":
            score -=1
        if button.text() =="Работаю":
            score +=0.5

    def show_window_10(self):  # открытие 10  окна 
        self.w10 = Window10()
        #self.w9 = Window9()
        self.hide()
        self.w10.show()
        #self.w9.hide()

class Window10(QWidget):
    def __init__(self):
        super(Window10, self).__init__()
        self.setWindowTitle('Вопрос 8')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Насколько вам было грустно, когда узнали о введении карантина?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Очень грустно:(")
        self.radio_button_2 = QRadioButton("Грустно(")
        self.radio_button_3 = QRadioButton("Весело)")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    def init_handlers(self):  # обработка нажатия для октрытия 11 окна
        self.button.clicked.connect(self.show_window_11)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Очень грустно:(":
            score +=1
        if button.text() =="Весело)":
            score -=1
        if button.text() =="Грустно(":
            score -=0.5

    def show_window_11(self):  # открытие 11  окна 
        self.w11 = Window11()
        #self.w10 = Window10()
        self.hide()
        self.w11.show()
        #self.w10.hide()

class Window11(QWidget):
    def __init__(self):
        super(Window11, self).__init__()
        self.setWindowTitle('Вопрос 9')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Как вы себя чувствуете?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Далее')
        self.button.show()
        self.radio_button_1 = QRadioButton("Отлично:D")
        self.radio_button_2 = QRadioButton("Ну нормально:/")
        self.radio_button_3 = QRadioButton("КОРОНАВИРУС!")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 12 окна
        self.button.clicked.connect(self.show_window_12)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Отлично:D":
            score +=1
        if button.text() =="Ну нормально:/":
            score -=0.5
        if button.text() =="КОРОНАВИРУС!":
            score -=1

    def show_window_12(self):  # открытие 12  окна 
        self.w12 = Window12()
        #self.w11 = Window11()
        self.hide()
        self.w12.show()
        #self.w11.hide()

class Window12(QWidget):
    def __init__(self):
        super(Window12, self).__init__()
        self.setWindowTitle('Вопрос 10')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        self.text.setText('Вы рады, что карантин закончился?')
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Завершить')
        self.button.show()
        self.radio_button_1 = QRadioButton("Конечно!!")
        self.radio_button_2 = QRadioButton("Да мне и дома хорошо сиделось")
        self.radio_button_3 = QRadioButton("Что? Карантин уже отменили!?")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.radio_button_1, id = 1)
        self.button_group.addButton(self.radio_button_2, id = 2)
        self.button_group.addButton(self.radio_button_3, id = 3)
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_1, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_2, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.radio_button_3, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для октрытия 13 окна
        self.button.clicked.connect(self.show_window_13)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

    def _on_radio_button_clicked(self,button):
        global score
        if button.text() =="Конечно!!":
            score +=1
        if button.text() =="Да мне и дома хорошо сиделось":
            score -=1
        if button.text() =="Что? Карантин уже отменили!?":
            score -=0.5

    def show_window_13(self):  # открытие 13  окна 
        self.w13 = Window13()
        #self.w12 = Window12()
        self.hide()
        self.w13.show()
        #self.w12.hide()

class Window13(QWidget):
    def __init__(self):
        super(Window13, self).__init__()
        self.setWindowTitle('Конец')
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        self.v_line = QVBoxLayout(self)
        #self.h_line = QHBoxLayout(self)
        self.text = QLabel(self)
        global score
        self.text.setText('Ну что, вот он и конец.\n Спасибо за прохождение моего теста и надеюсь он вам понравился. \n Я искренно верю, что вы провели карантин очень весело. \n #КАРАНТИН_ВСЕГО_ЛИШЬ_ФОРМАЛЬНОСТЬ \n Если ты набрал > 7 баллов, \n то ты провел карантин с "ПОЛЬЗОЙ" \n Если ты набрал > 5 баллов, \n то ты провел карантин "НЕПЛОХО" \n Если ты набрал > 3 баллов, \n то ты "ЛЕНИВЫЙ" \n Если ты набрал > 0, \n то ты "ОЧЕНЬ ЛЕНИВЫЙ" \n Если ты набрал < 0, \n то "ТЫ ВООБЩЕ НА КАРАНТИНЕ ЧТО ТО ДЕЛАЛ!?" \n Твой счет:'+str(score))
        self.text.show()
        self.button = QPushButton(self)
        self.button.setText('Выход')
        self.button.show()
        self.v_line.addWidget(self.text, alignment = Qt.AlignTop)
        self.v_line.addWidget(self.button, alignment = Qt.AlignRight)
        self.init_handlers()
    
    def init_handlers(self):  # обработка нажатия для закрытия 13 окна
        #self.w13 = Window13()
        self.button.clicked.connect(self.hide_window_13)
    
    def hide_window_13(self):  # закрытие 13  окна 
        #self.w13 = Window13()
        self.hide()
        sys.exit(app.exec_())
        #self.w13.hide()


 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window1()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())