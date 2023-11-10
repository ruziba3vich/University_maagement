from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget,
                            QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt
import mysql.connector

class AddNewUniversity(QMainWindow):
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

        self.setWindowTitle("Add new university")
        self.__cursor.execute("""
                              SELECT city.name, University.name, city.id FROM University
                              INNER JOIN City ON University.city = City.id;"""
                              )
        information = self.__cursor.fetchall()
        self.__universities = set()
        self.__cities = dict()
        for row in information:
            self.__universities.add(row[1])
            self.__cities[row[0]] = row[2]

        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setFixedWidth(40)
        self.__city_requirer_line = QLineEdit()
        self.__opening_label = QLabel("<html><b><font size='20'>enter the city and university name</html></b></font>")
        self.__city_requirer_line.setPlaceholderText("enter the city name")
        self.__university_name_requirer_line = QLineEdit()
        self.__university_name_requirer_line.setPlaceholderText("enter the university name")
        self.__add_button = QPushButton("ADD")
        self.__add_button.setMinimumHeight(80)
        self.__add_button.clicked.connect(self.__add_button_clicked)
        self.__text_edit = QTextEdit()
        self.__text_edit.setReadOnly(True)

        self.__main_layout = self.__layout_maker(
                      True,
                      self.__go_back_button,
                      self.__opening_label,
                      self.__city_requirer_line,
                      self.__university_name_requirer_line,
                      self.__add_button,
                      self.__text_edit
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
        self.__admin_window.resize(self.width(), self.height())
        self.__admin_window.move(self.pos())
        self.hide()
        self.__admin_window.show()

    def __add_button_clicked(self):
        city = self.__city_requirer_line.text()
        city = city.capitalize()
        if len(city):
            university = self.__university_name_requirer_line.text()
            university = university.upper()
            if len(university):
                self.__university_name_requirer_line.clear()
                self.__city_requirer_line.clear()
                if university in self.__universities:
                    self.__university_name_requirer_line.setPlaceholderText(f"{university} already exists !")
                    self.__text_edit.setText(f"{university} already exists !")
                else:
                    if self.__cities.get(city) == None:
                        self.__cursor.execute(f"INSERT INTO CITY (name) VALUES ('{city}');")
                    self.__cursor.execute(f"SELECT id FROM CITY WHERE name = '{city}';")
                    id = self.__cursor.fetchall()[0][0]
                    self.__cities[university] = id
                    self.__universities.add(university)
                    self.__cursor.execute(
                          f"INSERT INTO University (city, name) VALUES ({id}, '{university}');"
                        )
                    self.__database_connection.commit()
                    self.__text_edit.setText(f"{university} has successfully been added ✅")
            else:
                self.__university_name_requirer_line.setPlaceholderText(
                      "you cannot leave empty this field"
                    )
        else:
            self.__city_requirer_line.setPlaceholderText(
                      "you cannot leave empty this field"
                    )
