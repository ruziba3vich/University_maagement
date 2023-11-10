import mysql.connector
from PyQt5.QtWidgets import QApplication
from first_window import FirstWindow

temporary_connection = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Dost0n1k'
)
original_database_name = "users_project_prodonik_unique_db_name"
# delete_query = f"DROP DATABASE {original_database_name};"
cursor = temporary_connection.cursor()
query = f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{original_database_name}';"
# cursor.execute(delete_query)
cursor.execute(query)
result = cursor.fetchone()
if not result:
    create_database = f"CREATE DATABASE {original_database_name};"
    tables = ["City", "University", "Student", "Businessmen"]
    cursor.execute(create_database)
    
    city = f"""CREATE TABLE {tables[0]}
                    (
                        id INTEGER auto_increment,
                        name VARCHAR(100),
                        PRIMARY KEY (id)
                    )"""
    university = f"""CREATE TABLE {tables[1]}
                    (
                        id INTEGER auto_increment,
                        name VARCHAR(100),
                        city INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (city) REFERENCES City(id)
                    )"""
    student = f"""CREATE TABLE {tables[2]}
                    (
                        id INTEGER auto_increment,
                        name VARCHAR(100),
                        city INTEGER,
                        university INTEGER,
                        age INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (city) REFERENCES City(id),
                        FOREIGN KEY (university) REFERENCES University(id)
                    )"""
    businessmen = f"""CREATE TABLE {tables[3]}
                        (
                        id INTEGER auto_increment,
                        name VARCHAR(100),
                        net_worth INTEGER,
                        city INTEGER,
                        university INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (city) REFERENCES City(id),
                        FOREIGN KEY (University) REFERENCES University(id)
                        )"""
    tables = [city, university, student, businessmen]
    use_query = f"USE {original_database_name};"
    cursor.execute(use_query)
    for table in tables:
        cursor.execute(table)

cursor.close()
temporary_connection.close()

app = QApplication([])

main_window = FirstWindow()
main_window.resize(1200, 600)
main_window.show()

app.exec()
