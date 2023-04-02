from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton,
                            QSpinBox, QLabel, QGroupBox, QButtonGroup,
                            QRadioButton)
from PyQt5.QtCore import Qt

from appl import app
# створюємо необхідні лейаути
main_card_layout = QVBoxLayout()
line1_card = QHBoxLayout()
line2_card = QHBoxLayout()
# створюємо віджети
btn_menu = QPushButton("Menu")
btn_rest = QPushButton("Take a rest")
btn_rest.hide()

spinb = QSpinBox()
spinb.hide()
time_lb = QLabel("0")
lb_quest = QLabel("Яблуко")
btn_ok = QPushButton("Відповісти")

# розміщуємо віджети на першій горизонтальній лінії
line1_card.addWidget(btn_menu, stretch=1)
line1_card.addStretch(4)
line1_card.addWidget(btn_rest, stretch=1)
line1_card.addWidget(spinb, stretch=1)
line1_card.addWidget(time_lb, stretch=1)
line1_card.addWidget(QLabel("секунд"), stretch=1)

# створюємо групу з перемикачами
group_box = QGroupBox("Варіанти відповідей")
button_group = QButtonGroup()

rb_list = []
for i in range(4):
    r = QRadioButton(" ")
    rb_list.append(r)
    button_group.addButton(r)

box_line = QHBoxLayout()
box_line1 = QVBoxLayout()
box_line2 = QVBoxLayout()

box_line1.addWidget(rb_list[0])
box_line1.addWidget(rb_list[1])
box_line2.addWidget(rb_list[2])
box_line2.addWidget(rb_list[3])

box_line.addLayout(box_line1)
box_line.addLayout(box_line2)

group_box.setLayout(box_line)
# group_box.hide()
# прихований групбокс
group_box2 = QGroupBox("Результат теста")

result_lb = QLabel("Вірно/невірно")
answ_lb = QLabel("apple")

box_line3 = QVBoxLayout()
box_line3.addWidget(result_lb, alignment=(Qt.AlignTop | Qt.AlignLeft))
box_line3.addStretch(1)
box_line3.addWidget(answ_lb, alignment=Qt.AlignCenter, stretch=1)
box_line3.addStretch(1)

group_box2.setLayout(box_line3)

group_box2.hide()



# лінія для кнопки унизу
line2_card = QHBoxLayout()
line2_card.addStretch(1)
line2_card.addWidget(btn_ok, stretch=2)
line2_card.addStretch(1)

# розміщуємо горизонтальні лейаути та віджети на основному лейауті
main_card_layout.addLayout(line1_card, stretch=1)
main_card_layout.addWidget(lb_quest, alignment=Qt.AlignCenter, stretch=1)
main_card_layout.addWidget(group_box, stretch=5)
main_card_layout.addWidget(group_box2, stretch=5)
main_card_layout.addLayout(line2_card, stretch=1)

def show_question():
    group_box.show()
    group_box2.hide()
    btn_ok.setText("Відповісти")
def show_results():
    group_box2.show()
    group_box.hide()
    btn_ok.setText("Наступне питання")