from add_new_note import add_new_note
from get_note import get_note
from delete_note import delete_note


def user_choice(connection):
    try:
        input_or_output = int(input("1 - Записать заметку, 2 - Вывести заметку. 3 - Удалить заметку. Ваш ввод - "))
    except ValueError:
        print("Неправильно введен выбор. Попробуйте еще раз.")
        user_choice(connection)
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
        print("Выберете между добавлением, выводом в терминал или удалением.")
        user_choice(connection)
    one_more_time = int(input("Введите 1, если хотите ввести или вывести что-то еще. Введите любой другой символ, чтобы закончить действие программы. Ваш ввод - "))
    if one_more_time == 1:
        user_choice(connection)
    else:
        return