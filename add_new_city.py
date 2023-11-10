from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget,
                            QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt
import mysql.connector

class AddNewCity(QMainWindow):
    def __init__(self, admin_window):
        super().__init__()
        self.__admin_window = admin_window

        self.__original_database_name = "users_project_prodonik_unique_db_name"
        self.__database_connection = mysql.connector.connect(
                host = 'localhost',
                username = 'root',
                password = 'Dost0n1k',
                database = self.__original_database_name
        )
        self.__cursor = self.__database_connection.cursor()
        self.__cursor.execute(f"USE {self.__original_database_name};")

        self.setWindowTitle("Add new city")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)

        self.__city_names = set()
        self.__cursor.execute("SELECT name FROM City;")
        cities = self.__cursor.fetchall()
        for row in cities:
            for element in row:
                self.__city_names.add(element)

        self.__requiring_label = QLabel("<html><b><font size='5'>enter new city name</html></b></font>")

        self.__main_line_edit = QLineEdit()
        self.__main_line_edit.setPlaceholderText("enter here")

        self.__button_to_add = QPushButton("add")
        self.__button_to_add.clicked.connect(self.__add_button_is_clicked)
        self.__button_to_add.setMinimumSize(200, 80)

        self.__information_about_operation = QTextEdit()
        self.__information_about_operation.setReadOnly(True)

        self.__main_layout = self.__layout_maker(
                            True,
                            self.__go_back_button,
                            self.__requiring_label,
                            self.__main_line_edit,
                            self.__button_to_add,
                            self.__information_about_operation
        )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)

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
        self.__information_about_operation.clear()
        self.__admin_window.resize(self.width(), self.height())
        self.__admin_window.move(self.pos())
        self.hide()
        self.__admin_window.show()
    
    def __add_button_is_clicked(self):
        city_name = self.__main_line_edit.text()
        self.__main_line_edit.clear()
        city_name = city_name.capitalize()
        if city_name in self.__city_names:
            self.__information_about_operation.setText(
                        "This city already exists in the cities table"
                    )
        else:
            self.__city_names.add(city_name)
            self.__main_line_edit.clear()
            query = f"INSERT INTO city (name) VALUES ('{city_name}');"
            self.__cursor.execute(query)
            self.__database_connection.commit()
            self.__information_about_operation.setText(
                        f"{city_name} has successfully been added ✅"
                    )
