from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class DeleteData(QMainWindow):
    def __init__(self, admin_window):
        super().__init__()
        self.__admin_window = admin_window

        self.setWindowTitle("delete data")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)
        self.__opening_label = QLabel(
                "<html><b><font size='25'>choose one of the options</html></b></font>"
            )
        self.__delete_new_city = QPushButton("delete new city")
        self.__delete_new_city.setMinimumHeight(80)
        self.__delete_new_university = QPushButton("delete new university")
        self.__delete_new_university.setMinimumHeight(80)
        self.__delete_new_student = QPushButton("delete new student")
        self.__delete_new_student.setMinimumHeight(80)
        self.__delete_new_businessman = QPushButton("delete new businessman")
        self.__delete_new_businessman.setMinimumHeight(80)

        self.__main_layout = self.__layout_maker(
                                    True,
                                    self.__go_back_button,
                                    self.__opening_label,
                                    self.__delete_new_city,
                                    self.__delete_new_university,
                                    self.__delete_new_student,
                                    self.__delete_new_businessman
                                    )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__opening_label, Qt.AlignCenter)

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __layout_maker(self, style, * widgets):
        if style:
            layout = QVBoxLayout()
        else:
            layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout
    
    def __go_back_button_is_clicked(self):
        self.__admin_window.resize(self.width(), self.height())
        self.__admin_window.move(self.pos())
        self.hide()
        self.__admin_window.show()
