import pdfplumber
from pathlib import Path
from gtts import gTTS
import art
#Функция, преобразующая .pdf в mp3
#Function that converts .pdf to mp3
def pdf_to_mp3(file_path = "test.pdf", language = "en"):
    # Если файл существует и имеет расширение .docx то выполняем тело функции иначе return
    #If the file exists and has the extension .docx, then execute the body of the function, else return
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        #Открываем .pdf файл и сохраняем весь его текст в массив
        #Open a .pdf file and save all its text in an array
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        #С помощью метода join конкатируем все элементы в строку
        #Use the join method to concatenate all elements into a string
        text_from_file = ''.join(pages)
        #Заменяем переносы строк на пробелы
        #Replace line breaks with spaces
        text_from_file = text_from_file.replace("\n", ' ')
        #Преобразуем текст в речь с помощью Google Text-to-Speech
        #Convert text to speech with Google Text-to-Speech
        converted_pdf_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Получаем путь у пользователя куда нужно сохранить файл
        #Get the path from the user where you want to save the file
        save_path = str(input("[+] Enter the path where you want to save the file - "))
        #Сохранение файла в формате .mp3
        # Saving a file in .mp3 format
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        converted_pdf_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return