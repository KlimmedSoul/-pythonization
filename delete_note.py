from execute_read_query import execute_read_query

def delete_note(connection, title): 
    note_to_delete = f"""DELETE FROM users WHERE title = "{title}";"""
    execute_read_query(connection, note_to_delete)
    print("Заметка успешно удалена")