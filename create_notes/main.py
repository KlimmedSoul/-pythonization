from create_connection import create_connection
from create_database import create_database
from execute_query import execute_query
from user_choise import user_choice
from art import *


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


if __name__ == '__main__':
    tprint("          <<Notes>>")
    user_choice(connection)
