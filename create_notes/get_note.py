from execute_read_query import execute_read_query

def get_note(connection, title):
    select_users = f"""SELECT * FROM users WHERE title = "{title}";"""
    notes = execute_read_query(connection, select_users)
    print(f"Заголовок заметки - {notes[0][1]}")
    print(f"Текст заметки - {notes[0][2]}")