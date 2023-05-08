from tkinter import *
from get_dashes import get_dashes
from random_word import random_word

def guess_the_word():
    rnd_word = random_word()

    window = Tk()
    window.title("game")
    window.resizable(0, 0)
    window.geometry("600x800")

    win = PhotoImage(file=r'C:\\Users\\User1\\Desktop\\guess_the_word\\gifs\\win.gif')
    lose = PhotoImage(file=r'C:\\Users\\User1\\Desktop\\guess_the_word\\gifs\\gameover.gif')


    lifes = 5

    lifes_txt = Label(window, text="Количество жизней: ", font="Times 20")
    lifes_txt.place(x = 0, y = 0)
    lifes_cnt = Label(window, text = "{}".format(lifes), font="Time 18")
    lifes_cnt.place(x = 240, y = 4)
    canvas = Canvas(window, bg='white', height=600, width=800)

    dash_word = []
    btn_pressed = []


    def create_word_btns(word, btn_pressed):
        shift_x = shift_y = 0
        cnt = 0
        cnt1 = 0
        for i in range(ord("А"), ord("Я")+1):
            btn = Button(text=chr(i),bg="white", foreground="black", height=2, width=5, font="Times 12", relief="raised")
            btn.place(x=130 + shift_x, y= 400 - shift_y)
            btn.bind('<Button-1>', lambda event: check_word(event, word, dash_word, btn_pressed, rnd_word, lifes, lifes_cnt))
            btn_pressed.append(btn)
            shift_x += 60
            cnt += 1

            if cnt == 6:
                cnt1 += 1
                shift_x = cnt = 0
                shift_y -= 60
            if cnt1 == 5:
                shift_x += 80


    def check_word(event, word, dash_word, btn_pressed, rnd_word, lifes, lifes_cnt):
        pressed_btn = event.widget['text']
        pos = []

        for i in range(len(word)):
            if word[i] == pressed_btn:
                pos.append(i)

        if pos:
            for i in pos:
                dash_word[i].config(text='{}'.format(word[i]))
            cnt_pressed_btn = 0

            for i in dash_word:
                if i['text'].isalpha():
                    cnt_pressed_btn += 1
                    
            if cnt_pressed_btn == len(rnd_word):
                print("DA")
                game_over("win")
        else:
            lifes = int(lifes_cnt.cget('text'))
            lifes_cnt.config(text=' {}'.format(lifes-1))
            
            if lifes == 1:
                game_over("lose")

    def restart():
        window.destroy()
        guess_the_word()

    def game_over(status):
        for btn in btn_pressed:
            btn.destroy()

        if status == "win":
            Label(window, image=win, height=400, width=800).pack()
            button = Button(window, text="Начать заново", command=restart, bg="white", foreground="black", height=30, width=100, font="Times 50")
            button.place(x = 200, y = 500)
            button.pack()

        elif status == "lose":
            Label(window, image=lose, height=400, width=800).pack()
            button = Button(window, text="Начать заново", command=restart, bg="white", foreground="black", height=30, width=100, font="Times 50")
            button.place(x = 200, y = 500)
            button.pack()



    create_word_btns(rnd_word, btn_pressed)
    get_dashes(window, dash_word, rnd_word)
    window.mainloop()


if __name__ == '__main__':
    guess_the_word()