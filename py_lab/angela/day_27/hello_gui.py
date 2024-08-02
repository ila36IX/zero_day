from tkinter import *

window=Tk()
window.title("First GUI")
window.minsize(width=700,height=300)
window.maxsize(width=800,height=600)

label=Label(text="Hello world",font=("Arial","20","bold"))
label.pack()


def clicked():
    input_val=entry.get()
    label.config(text="Hello, "+input_val.title())
    
button=Button(text="Click me", command=clicked)
button.pack()

entry=Entry()
entry.pack()

window.mainloop()
