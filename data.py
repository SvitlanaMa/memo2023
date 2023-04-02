class Question:
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    def show_quest(self, q_lb, rb_list):
        q_lb.setText(self.question)
        rb_list[0].setText(self.right)
        rb_list[1].setText(self.wrong1)
        rb_list[2].setText(self.wrong2)
        rb_list[3].setText(self.wrong3)
    def show_res(self, r_lb, answ_lb, rb_list):
        if rb_list[0].isChecked():
            r_lb.setText("Вірно")
        else:
            r_lb.setText("Невірно")
        answ_lb.setText(self.right)

q1 = Question("Як називається віджет-кнопка", "QRadioButton", "QLabel", "QSpinBox",
               "QWidget")
q2 = Question("Як називається віджет-напис", "QLabel", "QRadioButton", "QSpinBox",
               "QWidget")
q3 = Question("Як називається віджет-вікно", "QWidget", "QLabel", "QRadioButton", "QSpinBox")

q_list = [q1, q2, q3]