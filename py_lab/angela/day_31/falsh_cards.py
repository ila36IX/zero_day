from tkinter import *
from tkinter import ttk
import csv
import random

with open("./data/french_to_english.csv", "r", encoding='utf-8') as f:
    dictionary = csv.DictReader(f)
    words = {}
    for row in dictionary:
        words[row["French"]] = row["Englsh"]


unknown_words = filter(lambda x: len(x) >= 3, list(words.keys()))
unknown_words = list(map(lambda x: x.capitalize(), unknown_words))


def next_word():
    global timer
    root.after_cancel(timer)
    card.config(image=img_card_back)
    word_english.set("Click the red button\n If you didn't recognize it")
    timer = root.after(3000, flip_card)
    word_english.set(random.choice(unknown_words))


def flip_card(app_opening=False):
    root.after_cancel(timer)
    if app_opening:
        next_word()
        return

    card.config(image=img_card_front)
    meaning = words.get(word_french.get().lower(), "I don't know this word either").capitalize()
    word_english.set(meaning)


root = Tk()
root.title("Flashy")
root.geometry("900x800")
root.resizable(False, False)
root.configure(bg="#B1DDC6")

timer = root.after(3000, func=lambda :flip_card(app_opening=True))

word_english = StringVar(value="Click the green button to")
word_french = StringVar(value="Start")


img_card_front = PhotoImage(file="./images/card_back.png")
img_card_back = PhotoImage(file="./images/card_front.png")
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")

card = Label(root, image=img_card_front, bg="#B1DDC6")
card.grid(row=0, column=0, columnspan=2, rowspan=6, padx=50, pady=50)

lang_label = Label(root, textvariable=word_english, font="Ariel 30", bg="#98c4ac")
lang_label.grid(row=2, column=0, columnspan=2)
lang_word = Label(root, textvariable=word_french, font="Ariel 50 bold", bg="#98c4ac")
lang_word.grid(row=3, column=0, columnspan=2)

btn_membered = Button(root, image=img_right, command=next_word)
btn_membered.grid(row=6, column=0)
btn_not_yet = Button(root, image=img_wrong, command=flip_card)
btn_not_yet.grid(row=6, column=1)

root.mainloop()