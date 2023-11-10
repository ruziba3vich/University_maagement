from PyQt5.QtWidgets import (QLabel, QMainWindow, QPushButton,
                            QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from add_data_by_admin import AddData
from delete_data_by_admin import DeleteData

class AdminWindow(QMainWindow):
    def __init__(self, admin_panel):
        super().__init__()
        self.__add_data_window = AddData(self)
        self.__delete_data_window = DeleteData(self)
        self.__admin_panel = admin_panel

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)

        self.__welcome_window = QLabel()
        self.__welcoming_text = "<html></b><font size='20'>WELCOME</html></b></font>"
        self.__welcome_window.setText(self.__welcoming_text)

        self.setWindowTitle("Admin")
        self.__add_rows_into_table = QPushButton("add data")
        self.__add_rows_into_table.clicked.connect(self.__add_data_button_is_clicked)
        self.__add_rows_into_table.setMinimumSize(300, 80)
        self.__delete_rows_from_table = QPushButton("delete data")
        self.__delete_rows_from_table.clicked.connect(self.__delete_data_button_is_clicked)
        self.__delete_rows_from_table.setMinimumSize(300, 80)

        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__go_back_button)
        self.__main_layout.addWidget(self.__welcome_window)
        self.__main_layout.setAlignment(self.__welcome_window, Qt.AlignCenter)
        self.__main_layout.addWidget(self.__add_rows_into_table)
        self.__main_layout.addWidget(self.__delete_rows_from_table)
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main_widget)

    def __go_back_button_is_clicked(self):
        self.__admin_panel.resize(self.width(), self.height())
        self.__admin_panel.move(self.pos())
        self.hide()
        self.__admin_panel.show()

    def __add_data_button_is_clicked(self):
        self.__add_data_window.resize(self.width(), self.height())
        self.__add_data_window.move(self.pos())
        self.hide()
        self.__add_data_window.show()
    
    def __delete_data_button_is_clicked(self):
        self.__delete_data_window.resize(self.width(), self.height())
        self.__delete_data_window.move(self.pos())
        self.hide()
        self.__delete_data_window.show()
