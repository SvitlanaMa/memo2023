from PyQt5.QtWidgets import (QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

menu_layout = QVBoxLayout()

test_btn = QPushButton("Розпочати тестування")
learn_btn = QPushButton("Розпочати навчання")

menu_layout.addWidget(test_btn, alignment=Qt.AlignCenter)
menu_layout.addWidget(learn_btn, alignment=Qt.AlignCenter)
