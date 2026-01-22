from random import randint
from PyQt5.Qtcore import Qt
from PyQt5.QtWidgets import (
    QApplication, Qwidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QButtonGroup,
    QPushButton, QLabel)


from random import shuffle


class Question():
    def init(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question("Як звати персонажа мультфильму Аватар?", 'Аанг', 'Азула', 'Зуко', 'Айро'))
question_list.append(Question("Какие вопросы можно задать другу?", "Чем ты больше всего гордишься", 'Твое самое любимое воспоминание', 'Есть ли у тебя фобии', 'Как ты находишь друзей'))
question_list.append(Question("Лучшие вопросы, чтобы узнать друг друга", "Чему ты завидуешь", 'О чем ты больше всего жалеешь', 'Каким ты видишь себя через 10 лет', 'Какое у тебя самое заветное желание'))
question_list.append(Question("Вопросы для лучшего друга", "О каких поступках ты жалеешь", 'О каких поступках ты жалеешь', 'Что ты ценишь во мне', 'Что тебя во мне раздражает'))
question_list.append(Question("Какое слово всегда пишется неправильно?", 'Правельно', 'Неправельно', 'Всегда', 'пишеться'))
question_list.append(Question("Сколько месяцев в году имеют 28 дней?", 'Один', 'Два', 'Все', 'Семь'))
question_list.append(Question("Что можно легко взять в левую руку, но нельзя в правую?", 'Левая рука', 'Члюч', 'яблоко', ''))
question_list.append(Question("", '', '', '', ''))
question_list.append(Question("", '', '', '', ''))
question_list.append(Question("", '', '', '', ''))


app = QApplication([])


btn_OK = QPushButton('Відповісти')
lb_Question = QLabel("Найскладніше питання світу!")
RadioGroupBox = QGroupBox("Варіанти відповідей")


rbtn_1 = QRadioButton("Відповідь 1")
rbtn_2 = QRadioButton("Відповідь 2")
rbtn_3 = QRadioButton("Відповідь 3")
rbtn_4 = QRadioButton("Відповідь 4")


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addWidget(layout_ans1)
layout_ans1.addWidget(layout_ans1)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат:")
lb_Result = QLabel('Чи ви праві чи ні')
lb_Correct = QLabel('Відповідь буде тут')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlightLeft | Qt.Alightop ))
layout_res.addWidget(lb_Correct, alignment = Qt.AlightHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addChildWidget(lb_Question, aligment=(Qt.AlighnHCenter | Qt.AlighnVCenter ))
layout_line2.addChildWidget(RadioGroupBox)
layout_line3.addChildWidget(AnsGroupBox)
RadioGroupBox.hide()


layout_line1.addStretch(1)
layout_line2.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)


layout_cards = QVBoxLayout()


layout_cards.addLayout(layout_line1, stretch = 2)
layout_cards.addLayout(layout_line2, stretch = 8)
layout_cards.addStretch(1)
layout_cards.addLayout(layout_line2, stretch = 8)
layout_cards.addStretch(1)
layout_cards.setSpacing(5)


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(result):
    lb_Result.setText(result)
    show_results()


def check_answer():
    if answer[0].isChecked():
        show_correct("Правильно!")
        print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked:
            show_correct("Не правильно!")
            print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)


def next_question():
    window.total +- 1
    print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == "відповісти":
        check_answer()
    elif btn_OK.text() =='наступне питання':
        next_question()


window = Qwidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')


window.cur_question = -1
btn_OK.clicked.connect(click_OK)


window.score = 0
window.total = 0


next_question()
window.show()
app.exec()