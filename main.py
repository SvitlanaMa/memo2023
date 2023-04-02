from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QTimer
from appl import app
from card_layout import *
from data import *
from random import shuffle
from menu_layout import *
from study_layout import *


quest_num = 0
timer = QTimer()
timer.setInterval(1000)
t = 0

def ok_click():
    global quest_num, t
    if btn_ok.text() == "Відповісти":
        q_list[quest_num].show_res(result_lb, answ_lb, rb_list)
        show_results()
        quest_num += 1
        timer.stop()
    else:
        shuffle(rb_list)
        q_list[quest_num].show_quest(lb_quest, rb_list)
        show_question()
        time_lb.setText("0")
        t = 0
        timer.start()

def test_click():
    shuffle(q_list)
    shuffle(rb_list)
    q_list[quest_num].show_quest(lb_quest, rb_list)
    # print("Натиснули кнопку!!!!")
    window_menu.hide()
    window_test.show()
    timer.start()

def open_menu():
    window_test.hide()
    window_study.hide()
    window_menu.show()
    timer.stop()

def start_study():
    list_widget.clear()
    for item in q_list:
        list_widget.addItem(item.question)
    window_study.show()
    window_menu.hide()

def time_out():
    global t
    t += 1
    time_lb.setText(str(t))
    if t == 5:
        msg = QMessageBox()
        msg.setText("Час вийшов!")
        msg.exec_()

window_test = QWidget()
window_test.resize(600, 500)
window_test.setWindowTitle("Memory Card")
window_test.setLayout(main_card_layout)

# window_test.show()

window_menu = QWidget()
window_menu.resize(300, 400)
window_menu.setWindowTitle("Memory Card")
window_menu.setLayout(menu_layout)

window_menu.show()

window_study = QWidget()
window_study.resize(600, 500)
window_study.setWindowTitle("Memory Card")
window_study.setLayout(study_layout)
window_study.hide()

btn_ok.clicked.connect(ok_click)
test_btn.clicked.connect(test_click)
btn_menu.clicked.connect(open_menu)
learn_btn.clicked.connect(start_study )
menu_btn2.clicked.connect(open_menu)
timer.timeout.connect(time_out)

app.exec_()