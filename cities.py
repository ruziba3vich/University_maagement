from PyQt5.QtWidgets import (QLabel, QMainWindow,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from citygetter import ShowAll
from search_city_by_id import SearchById
from search_city_by_name import SearchCityByName

class Cities(QMainWindow):
    def __init__(self, user_window):
        super().__init__()
        self.__show_all = ShowAll(self)
        self.setWindowTitle("Cities")
        self.__main_label = QLabel()
        self.__main_label.setText("<html><b><font size='14'>choose options below</b></html></font>")

        self.__user_window = user_window

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)

        self.__show_all_button = QPushButton("SHOW ALL")
        self.__show_all_button.clicked.connect(self.__show_all_button_pressed)
        self.__show_all_button.setFixedSize(int(self.width() * 8 / 9), int(self.height() / 7))
        self.__by_name_button = QPushButton("search by name")
        self.__by_name_button.setFixedSize(int(self.width() * 8 / 9), int(self.height() / 7))
        self.__by_name_button.clicked.connect(self.___search_by_city_name_button_clicked)
        self.__by_id_button = QPushButton("search by id")
        self.__by_id_button.clicked.connect(self.__search_by_id_button_clicked)
        self.__by_id_button.setFixedSize(int(self.width() * 8 / 9), int(self.height() / 7))

        self.__buttons_layout = QVBoxLayout()
        self.__buttons_layout.addWidget(self.__show_all_button)
        self.__buttons_layout.addWidget(self.__by_name_button)
        self.__buttons_layout.addWidget(self.__by_id_button)
        self.__buttons_widget = QWidget()
        self.__buttons_widget.setLayout(self.__buttons_layout)

        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__go_back_button)
        self.__main_layout.addWidget(self.__main_label)
        self.__main_layout.addWidget(self.__buttons_widget)
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__main_label, Qt.AlignCenter)
        self.__main_layout.setAlignment(self.__buttons_widget, Qt.AlignCenter)

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __go_back_button_is_clicked(self):
        self.__user_window.resize(self.width(), self.height())
        self.__user_window.move(self.pos())
        self.hide()
        self.__user_window.show()

    def __search_by_id_button_clicked(self):
        self.__search_by_id_window = SearchById(self)
        self.__search_by_id_window.resize(self.width(), self.height())
        self.__search_by_id_window.move(self.pos())
        self.hide()
        self.__search_by_id_window.show()

    def ___search_by_city_name_button_clicked(self):
        self.__search_city_by_name_window = SearchCityByName(self)
        self.__search_city_by_name_window.resize(self.width(), self.height())
        self.__search_city_by_name_window.move(self.pos())
        self.hide()
        self.__search_city_by_name_window.show()

    def __show_all_button_pressed(self):
        self.__show_all.refresh_table()
        self.__show_all.resize(self.width(), self.height())
        self.__show_all.move(self.pos())
        self.hide()
        self.__show_all.show()
