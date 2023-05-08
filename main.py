from create_connection import create_connection
from create_database import create_database
from execute_query import execute_query
from add_new_note import add_new_note
from get_note import get_note
from delete_note import delete_note


# создание связи с бд
connection = create_connection("localhost", "root", "klimmed", "notes")

create_database_query = "CREATE DATABASE notes"
create_database(connection, create_database_query)


create_notes_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  title TEXT,
  text_note TEXT,
  PRIMARY KEY (id)
)ENGINE = InnoDB
"""

execute_query(connection,create_notes_table)


def user_choice():
    input_or_output = int(input("1 - Записать заметку, 2 - Вывести заметку. 3 - Удалить заметку. Ваш ввод - "))
    if input_or_output == 1:
        title = str(input("Введите заголовок заметки - "))
        text_note = str(input("Введите текст заметки - "))
        add_new_note(connection, title, text_note)
    elif input_or_output == 2: 
        title = str(input("Введите заголовок заметки - "))
        get_note(connection, title)
    elif input_or_output == 3:
        title = str(input("Введите заголовок заметки - "))
        delete_note(connection, title)
    else: 
        print("Выберете между 1 или 2.")
        user_choice()
    one_more_time = int(input("Введите 1, если хотите ввести или вывести что-то еще. Введите любой другой символ, чтобы закончить действие программы."))
    if one_more_time == 1:
        user_choice()
    else:
        return

if __name__ == '__main__':
    user_choice()
