import docx
from pathlib import Path
from gtts import gTTS
import art
#Функция, преобразующая .docx в mp3
#Function that converts .docx to mp3
def docx_to_mp3(file_path="test.docx", language="en"):
    #Проверка на существование файла и на его расширение
    #Checking for the existence of a file and its extension
    if Path(file_path).is_file() and Path(file_path).suffix == ".docx":
        #Сохранение в переменную файла .docx
        #Saving a .docx file into a variable
        docx_document = docx.Document(file_path)   
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        full_text = []
        #Чтение файла и добавление всего текста в массив full_text
        #Reading a file and adding all text to the full_text array
        for parag in docx_document.paragraphs:
            full_text.append(parag.text)
        print("[+] File read successfully.")
        #С помощью метода join конкатируем все элементы в строку
        #Use the join method to concatenate all elements into a string
        text_from_file = ''.join(full_text)
        #Заменяем переносы строк на пробелы
        #Replace line breaks with spaces
        text_from_file = text_from_file.replace('\n', ' ')
        #Преобразуем текст в речь с помощью Google Text-to-Speech
        #Convert text to speech with Google Text-to-Speech
        converted_docx_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Получаем путь у пользователя куда нужно сохранить файл
        #Get the path from the user where you want to save the file
        save_path = str(input("[+] Enter the path where you want to save the file - "))
        #Сохранение файла в формате .mp3
        #Saving a file in .mp3 format
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        converted_docx_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return