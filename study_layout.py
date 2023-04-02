from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QHBoxLayout,
                             QListWidget, QLabel)
from PyQt5.QtCore import Qt

study_layout = QVBoxLayout()
menu_btn2 = QPushButton("Menu")

study_layout2 = QHBoxLayout()
list_widget = QListWidget()
right_lb = QLabel("Вірна відповідь")

study_layout2.addWidget(list_widget, stretch=1)
study_layout2.addWidget(right_lb, stretch=1)

study_layout.addWidget(menu_btn2, alignment=(Qt.AlignTop | Qt.AlignLeft))
study_layout.addLayout(study_layout2)