from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow,
                            QPushButton, QVBoxLayout, QWidget,
                            QTableWidget, QTableWidgetItem, QHeaderView, QScrollArea)
from PyQt5.QtCore import Qt
import mysql.connector

class ShowAll(QMainWindow):
    def __init__(self, cities_menu):
        super().__init__()
        self.__cities_menu = cities_menu

    def refresh_table(self):
        self.__database_name = "users_project_prodonik_unique_db_name"
        self.__connection = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = 'Dost0n1k',
            database = self.__database_name
        )
        self.__cursor_db = self.__connection.cursor()
        use_query = f"USE {self.__database_name}"
        self.__cursor_db.execute(use_query)

        select_query = f"SELECT id, name FROM City;"
        self.__cursor_db.execute(select_query)
        self.__label_information = self.__cursor_db.fetchall()

        self.__table = QTableWidget(self)
        self.__table.setRowCount(len(self.__label_information))
        self.__table.setColumnCount(2)

        self.__table.setHorizontalHeaderLabels(['id', 'city name'])
        self.__table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowTitle("Cities")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.setMaximumWidth(40)
        self.__go_back_button.clicked.connect(self.__go_back_button_is_clicked)

        self.__layout_for_go_back_button = QHBoxLayout()
        self.__layout_for_go_back_button.addWidget(self.__go_back_button)
        self.__layout_for_go_back_button.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__widget_for_go_back_button = QWidget()
        self.__widget_for_go_back_button.setLayout(self.__layout_for_go_back_button)

        for row in range(len(self.__label_information)):
            for data in range(len(self.__label_information[row])):
                item = QTableWidgetItem(str(self.__label_information[row][data]).capitalize())
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.__table.setItem(row, data, item)

        self.__table_area = QScrollArea(self)
        self.__table_area.setWidget(self.__table)
        self.__table_area.setWidgetResizable(True)

        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__widget_for_go_back_button)
        self.__main_layout.addWidget(self.__table_area)
        self.__main_widget = QWidget()
        self.__main_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main_widget)

    def __go_back_button_is_clicked(self):
        self.__cursor_db.close()
        self.__connection.close()
        self.__cities_menu.resize(self.width(), self.height())
        self.__cities_menu.move(self.pos())
        self.hide()
        self.__cities_menu.show()
