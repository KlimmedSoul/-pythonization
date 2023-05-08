from execute_query import execute_query

def add_new_note(connection, title, text_note):
    new_note =  f"""
INSERT INTO
  users (title, text_note)
VALUES
  ('{title}', '{text_note}');
"""
    execute_query(connection, new_note)