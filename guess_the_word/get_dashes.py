from tkinter import *

def get_dashes(window, dash_word, rnd_word):
    shift = 0
    for i in range(len(rnd_word)):
        dash = Label(window, text='__', bg="white", height=2, width=5)
        dash.place(x=600/1.8/2 + shift, y= 200)
        shift += 40
        dash_word.append(dash)
    