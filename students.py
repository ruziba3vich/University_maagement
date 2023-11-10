from PyQt5.QtWidgets import (QLabel, QMainWindow, QHBoxLayout,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class Students(QMainWindow):
    def __init__(self, user_window):
        super().__init__()
        self.__user_window = user_window

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__opening_label = QLabel(
            "<html><b><font size='20'>CHOOSE ONE OF THE OPTIONS BELOW</html></b></font>"
            )

        self.__show_all_students_button = QPushButton("SHOW ALL STUDENTS")
        self.__show_all_students_button.setMinimumHeight(60)
        self.__search_by_id_button = QPushButton("search by student ID")
        self.__search_by_id_button.setMinimumHeight(60)
        self.__search_by_name_button = QPushButton("search by student NAME")
        self.__search_by_name_button.setMinimumHeight(60)
        self.__search_by_university_button = QPushButton("search by student UNIVERSITY")
        self.__search_by_university_button.setMinimumHeight(60)
        self.__search_by_age_button = QPushButton("search by student AGE")
        self.__search_by_age_button.setMinimumHeight(60)
        self.__search_by_city_button = QPushButton("search by student CITY")
        self.__search_by_city_button.setMinimumHeight(60)

        self.__main_layout = self.__layout_maker(
                  True,
                  self.__go_back_button,
                  self.__opening_label,
                  self.__show_all_students_button,
                  self.__search_by_id_button,
                  self.__search_by_name_button,
                  self.__search_by_university_button,
                  self.__search_by_age_button,
                  self.__search_by_city_button
        )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__opening_label, Qt.AlignCenter)
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main_widget)

    def __layout_maker(self, is_vertical, * widgets):
        if is_vertical:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout
    
    def __go_back_button_clicked(self):
        self.__user_window.resize(self.width(), self.height())
        self.__user_window.move(self.pos())
        self.hide()
        self.__user_window.show()
