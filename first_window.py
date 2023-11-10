from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QPushButton,
                            QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

from admin_panel import AdminPanel
from user_window import UserWindow


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.admin_panel = AdminPanel(self)
        self.user_panel = UserWindow(self)

        self.__password_button = QPushButton("password: prodonik14")
        self.__password_button.setEnabled(False)
        self.setWindowTitle("Panel")
        self.choice_label = QLabel(
            "<html><b><font size='20'>Choose one of the options below</html></b></font>"
            )
        self.left_label = QLabel()
        self.right_label = QLabel()

        self.admin_button = QPushButton("Admin")
        self.admin_button.setMinimumSize(100, 80)
        self.admin_button.clicked.connect(self.__admin_is_clicked)
        self.user_button = QPushButton("User")
        self.user_button.setMinimumSize(100, 80)
        self.user_button.clicked.connect(self.__user_is_clicked)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.admin_button)
        self.buttons_layout.addWidget(self.user_button)

        self.buttons_widget = QWidget()
        self.buttons_widget.setLayout(self.buttons_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.choice_label)
        self.main_layout.addWidget(self.buttons_widget)
        self.main_layout.addWidget(self.__password_button)
        self.main_layout.setAlignment(self.choice_label, Qt.AlignCenter)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def __admin_is_clicked(self):
        self.admin_panel.move(self.pos())
        self.admin_panel.resize(self.width(), self.height())
        self.hide()
        self.admin_panel.show()

    def __user_is_clicked(self):
        self.user_panel.move(self.pos())
        self.user_panel.resize(self.width(), self.height())
        self.hide()
        self.user_panel.show()
