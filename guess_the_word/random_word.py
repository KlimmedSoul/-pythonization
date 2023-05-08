import random
from tkinter import *

def random_word():
    file = open('words.txt', encoding="utf-8")
    cnt = 0
    for s in file:
        cnt += 1
    
    num_word = random.randint(1, cnt)
    rnd_word = ''
    cnt = 0

    file = open('words.txt', encoding="utf-8")

    for s in file:
        cnt += 1
        if cnt == num_word:
            rnd_word = s[:len(s):]

    rnd_word = rnd_word.strip().upper()
    return rnd_word  