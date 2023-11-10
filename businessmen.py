from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                            QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class Businessmen(QMainWindow):
    def __init__(self, users_window):
        super().__init__()
        self.__users_window = users_window

        self.setWindowTitle("Businessmen")
        self.__go_back_button = QPushButton("←")
        self.__go_back_button.clicked.connect(self.__go_back_button_clicked)
        self.__go_back_button.setMaximumWidth(40)
        self.__selection_label = QLabel(
            "<html><b><font size='25'>SELECT NEEDED OPTION</html></b></font>"
                                        )
        self.__search_by_id_button = QPushButton("search businessman by ID")
        self.__search_by_id_button.setMinimumHeight(80)
        self.__search_by_name_button = QPushButton("search businessmen by NAME")
        self.__search_by_name_button.setMinimumHeight(80)
        self.__search_by_city_button = QPushButton("search businessmen by CITY")
        self.__search_by_city_button.setMinimumHeight(80)
        self.__search_by_net_worth_button = QPushButton("search businessman by NET-WORTH")
        self.__search_by_net_worth_button.setMinimumHeight(80)
        self.__search_by_university_button = QPushButton("search businessman by UNIVERSITY")
        self.__search_by_university_button.setMinimumHeight(80)

        self.__main_layout = self.__layout_maker(
                                        True,
                                        self.__go_back_button,
                                        self.__selection_label,
                                        self.__search_by_id_button,
                                        self.__search_by_name_button,
                                        self.__search_by_city_button,
                                        self.__search_by_net_worth_button,
                                        self.__search_by_university_button
                                    )
        self.__main_layout.setAlignment(self.__go_back_button, Qt.AlignLeft)
        self.__main_layout.setAlignment(self.__selection_label, Qt.AlignCenter)
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
        self.__users_window.resize(self.width(), self.height())
        self.__users_window.move(self.pos())
        self.hide()
        self.__users_window.show()
