from pathlib import Path
from gtts import gTTS
import art
#Функция, преобразующая .txt в mp3
#Function that converts .txt to mp3
def txt_to_mp3(file_path="text.txt", language="en"):
    if Path(file_path).is_file() and Path(file_path).suffix == ".txt":
        #Открываем текстовый файл для чтения
        #Open a text file for reading
        txt_file = open(f"{file_path}", mode = 'r')
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        #Записываем весь текст в переменную и заменяем переносы строк на пробелы
        #Write all text into a variable and replace line breaks with spaces
        text_from_file = txt_file.read()
        text_from_file = text_from_file.replace('\n', ' ')
        #Преобразуем текст в речь с помощью Google Text-to-Speech
        #Convert text to speech with Google Text-to-Speech
        converted_txt_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Получаем путь у пользователя куда нужно сохранить файл
        #Get the path from the user where you want to save the file
        save_path = str(input("[+] Enter the path where you want to save the file - "))
        #Сохранение файла в формате .mp3
        #Saving a file to .mp3 format
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        converted_txt_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return