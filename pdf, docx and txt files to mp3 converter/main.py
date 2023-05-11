from art import tprint
from docx_to_mp3 import docx_to_mp3
from txt_to_mp3 import txt_to_mp3
from pdf_to_mp3 import pdf_to_mp3
tprint("<<TXT||DOCX||PDF>>\n                                          |      |\n                                          \/\n                             <<MP3>>")


def main():
    try:
        user_choice = int(input("Make a choice of what you want to convert: \n1).pdf=>.mp3\n2).docx=>.mp3\n3).txt=>.mp3\nWrite the number that corresponds to one of the choices - "))
        if user_choice == 1 or user_choice == 2 or user_choice == 3:
            user_lang = str(input("Enter the language in which the text in your file is written. Example - 'ru'\nWrite here ==> "))
            if user_lang != "ru" and user_lang != 'en':
                print("The language is not entered correctly. Reloading the script")
                main()
            #Запрашиваем у пользователя путь к файлу и перед строкой пишем r, 
            #т.к. здесь, \U в "C:\Users..." начинается восьмисимвольный символ Unicode, такой как \U00014321. 
            #После следует символ 's', который является недопустимым. Поэтому мы добавляем r, чтобы получить необработанную строку
            #We ask the user for the path to the file and write r before the line, because here, 
            #\U in "C:\Users..." starts with an eight-character Unicode character, such as \U00014321. 
            #It is followed by the 's' character, which is invalid. So we add r to produce a raw string
            user_file_path= str(input(r"Enter the full path of the file including the file itself. Example - 'C:\Users\example.pdf'  Write here ==> "))
            user_file_path = user_file_path.replace("\\","\\\\")
            if user_choice == 1:
                pdf_to_mp3(file_path=user_file_path, language=user_lang)
            elif user_choice == 2:
                docx_to_mp3(file_path=user_file_path, language=user_lang)
            elif user_choice == 3:
                txt_to_mp3(file_path=user_file_path, language=user_lang)
            restart = str(input("Would you like to use the script again? (Y/N) - "))
            if restart == "Y" or restart == "y":
                main()
        else:
            print("There are no such choices as you wrote... (￣ ￣|||)")
            main() 
    except ValueError:
        print("Write the number that corresponds to one of the choices! (；⌣̀_⌣́)")
        main()



    
if __name__ == "__main__":
    main()