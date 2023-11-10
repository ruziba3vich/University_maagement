from PyQt5.QtWidgets import (QLabel, QLineEdit, QMainWindow,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from admin_window import AdminWindow

class AdminPanel(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.__first_window = first_window

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)

        self.__admin_window = AdminWindow(self)
        self.__password = 'prodonik14'
        self.__password_acceptor = QLineEdit()
        self.__password_acceptor.setFixedWidth(400)
        self.__password_acceptor.setEchoMode(QLineEdit.Password)
        self.__password_acceptor.setPlaceholderText("enter the password here")
        self.__requiring_label = QLabel("Please enter the password")

        self.__enter_button = QPushButton("ENTER")
        self.__enter_button.clicked.connect(self.__check_password)
        self.__enter_button.setMinimumSize(100, 40)

        self.__label = QLabel()

        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__go_back_button)
        self.__main_layout.addWidget(self.__requiring_label)
        self.__main_layout.addWidget(self.__password_acceptor)
        self.__main_layout.addWidget(self.__enter_button)
        self.__main_layout.addWidget(self.__label)
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.setWindowTitle("Administration")

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __check_password(self):
        password = self.__password_acceptor.text()
        if password == self.__password:
            self.__admin_window.resize(self.width(), self.height())
            self.__admin_window.move(self.pos())
            self.hide()
            self.__admin_window.show()
            self.__password_acceptor.setPlaceholderText("enter the password here")
        else:
            self.__password_acceptor.setPlaceholderText("incorrect password, try again !")
        self.__password_acceptor.clear()

    def __go_back_button_is_clicked(self):
        self.__first_window.resize(self.width(), self.height())
        self.__first_window.move(self.pos())
        self.hide()
        self.__first_window.show()
