from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import *

app = QApplication([])
win = QWidget()
win.resize(400, 250)
win.setWindowTitle('Memory card')
ques = QLabel('Какой национальности не существует?')
ans_btn = QPushButton('Ответить')
win.total = 0
win.score = 0
class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

qlist = []
qlist.append(Question('Самая большая страна в мире?', 'Россия', 'Канада', 'Бразилия', 'Китай'))
qlist.append(Question('Какое животнное выше всех из списка?', 'Жираф', 'Тигр', 'Бегемот', 'Волк'))
#создание группы ответов
group = QGroupBox('Варианты ответов')

btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(btn1)
layout2.addWidget(btn2)
layout3.addWidget(btn3)
layout3.addWidget(btn4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

group.setLayout(layout1)

radiogroup = QButtonGroup()
radiogroup.addButton(btn1)
radiogroup.addButton(btn2)
radiogroup.addButton(btn3)
radiogroup.addButton(btn4)

def show_res():
    group.hide()
    ans_group.show()
    ans_btn.setText('Следующий вопрос')

def show_ques():
    ans_group.hide()
    group.show()
    ans_btn.setText('Ответить')
    radiogroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    radiogroup.setExclusive(True)

# def test():
#     if ans_btn.text() == 'Ответить':
#         show_res()
#     else:
#         show_ques()
answers = [btn1, btn2, btn3, btn4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ques.setText(q.question)
    ans_label2.setText(q.right_ans)
    show_ques()

def check_ans():
    if answers[0].isChecked():
        show_correct('Правильно')
        win.score += 1
    else:
        show_correct('Неправильно')
    print('Статистика:')
    print('Всего вопросов:', win.total)
    print('Правильных ответов:', win.score)
    print('Рейтинг', win.score / win.total * 100)


def show_correct(res):
    ans_label1.setText(res)
    show_res()


def next_ques():
    win.total += 1
    cur_ques = randint(0, len(qlist)- 1)
    q = qlist[cur_ques]
    ask(q)
    print('Статистика:')
    print('Всего вопросов:', win.total)
    print('Правильных ответов:', win.score)
    
def clickOK():
    if ans_btn.text() == 'Ответить':
        check_ans()
    else:
        next_ques()
#создание группы результатов
ans_group = QGroupBox('Результат теста')

ans_label1 = QLabel('Правильно/Неправильно')
ans_label2 = QLabel('Правильный ответ')

groupline = QVBoxLayout()

groupline.addWidget(ans_label1, alignment = (Qt.AlignLeft|Qt.AlignTop))
groupline.addWidget(ans_label2, alignment = Qt.AlignCenter)
ans_group.setLayout(groupline)

layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()

layout_1.addWidget(ques, alignment = Qt.AlignCenter)
layout_2.addWidget(group)
layout_2.addWidget(ans_group)

layout_3.addWidget(ans_btn)

main_layout = QVBoxLayout()

main_layout.addLayout(layout_1)
main_layout.addLayout(layout_2)
main_layout.addLayout(layout_3)

ans_btn.clicked.connect(clickOK)
next_ques()

ans_group.hide()
win.setLayout(main_layout)
win.show()
app.exec_()