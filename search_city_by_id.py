from PyQt5.QtWidgets import (QMainWindow, QLineEdit,
                            QPushButton, QVBoxLayout, QWidget,
                            QTableWidget, QTableWidgetItem,
                            QHeaderView, QScrollArea)
from PyQt5.QtCore import Qt
import mysql.connector

class SearchById(QMainWindow):
    def __init__(self, cities_menu):
        super().__init__()
        self.__cities_menu = cities_menu

        self.setWindowTitle("search by id")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)
        self.__go_back_button.setMaximumWidth(40)

        self.__database_name = "users_project_prodonik_unique_db_name"
        self.__database = mysql.connector.connect(
            host = "localhost",
            username = 'root',
            password = 'Dost0n1k',
            database = self.__database_name
        )
        self.__database_cursor = self.__database.cursor()

        self.__search_bar = QLineEdit()
        self.__search_bar.setPlaceholderText("enter the id")

        self.__search_button = QPushButton("search")
        self.__search_button.setMinimumHeight(40)
        self.__search_button.clicked.connect(self.__search_button_is_clicked)

        self.__scrolling_area = QScrollArea(self)
        self.__scrolling_area.setWidgetResizable(True)

        self.__database_cursor.execute("SELECT COUNT(id) FROM City;")
        self.__rows = self.__database_cursor.fetchall()

        self.__table = QTableWidget(self)
        self.__table.setRowCount(len(self.__rows))
        self.__table.setColumnCount(2)
        self.__table.setHorizontalHeaderLabels(['id', 'city name'])
        self.__table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.__scrolling_area.setWidget(self.__table)

        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__go_back_button)
        self.__main_layout.addWidget(self.__search_bar)
        self.__main_layout.addWidget(self.__search_button)
        self.__main_layout.addWidget(self.__scrolling_area)
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)

        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)

        self.setCentralWidget(self.__main_widget)

    def __search_button_is_clicked(self):
        text = self.__search_bar.text()
        self.__search_bar.clear()
        if text.isdigit():
            text = int(text)
            self.__database_cursor.execute(f"SELECT id, name FROM city WHERE id = {text}")
            result = self.__database_cursor.fetchall()
            if len(result) > 0:
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        item = QTableWidgetItem(str(result[i][j]).capitalize())
                        self.__table.setItem(i, j, item)
                self.__search_bar.setPlaceholderText("enter the id")
            else:
                self.__search_bar.setPlaceholderText(f"{text} is not found")
        else:
            self.__search_bar.setPlaceholderText("enter a valid id")

    def __go_back_button_is_clicked(self):
        self.__database_cursor.close()
        self.__database.close()
        self.__cities_menu.resize(self.width(), self.height())
        self.__cities_menu.move(self.pos())
        self.hide()
        self.__cities_menu.show()
