from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QPushButton,
                            QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from cities import Cities
from students import Students
from businessmen import Businessmen
from university import University

class UserWindow(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.__first_window = first_window
        self.__university_window = University(self)
        self.__businessmen_window = Businessmen(self)
        self.__cities_window = Cities(self)
        self.__students_window = Students(self)

        self.setWindowTitle("User")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setMaximumWidth(40)

        self.__menu_label = QLabel("<html><b><font size='14'>select searching options</html></b></font>")
        self.__cities_button = QPushButton("Cities")
        self.__cities_button.setMinimumHeight(80)
        self.__cities_button.clicked.connect(self.__cities_button_clicked)
        self.__student_button = QPushButton("Students")
        self.__student_button.clicked.connect(self.__students_button_clicked)
        self.__student_button.setMinimumHeight(80)
        self.__businessmen_button = QPushButton("Businessmen")
        self.__businessmen_button.clicked.connect(self.__businessmen_button_clicked)
        self.__businessmen_button.setMinimumHeight(80)
        self.__universities_button = QPushButton("Universities")
        self.__universities_button.clicked.connect(self.__university_button_clicked)
        self.__universities_button.setMinimumHeight(80)

        self.__main_layout = self.layout_maker(
                            True, self.__go_back_button,
                            self.__menu_label,
                            self.__cities_button,
                            self.__student_button,
                            self.__businessmen_button,
                            self.__universities_button
                                            )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__menu_label, Qt.AlignCenter)
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()

        for widget in widgets:
            layout.addWidget(widget)
        return layout
    
    def __go_back_button_clicked(self):
        self.__first_window.resize(self.width(), self.height())
        self.__first_window.move(self.pos())
        self.hide()
        self.__first_window.show()

    def __cities_button_clicked(self):
        self.__cities_window.resize(self.width(), self.height())
        self.__cities_window.move(self.pos())
        self.hide()
        self.__cities_window.show()

    def __students_button_clicked(self):
        self.__students_window.resize(self.width(), self.height())
        self.__students_window.move(self.pos())
        self.hide()
        self.__students_window.show()

    def __businessmen_button_clicked(self):
        self.__businessmen_window.resize(self.width(), self.height())
        self.__businessmen_window.move(self.pos())
        self.hide()
        self.__businessmen_window.show()

    def __university_button_clicked(self):
        self.__university_window.resize(self.width(), self.height())
        self.__university_window.move(self.pos())
        self.hide()
        self.__university_window.show()
    
