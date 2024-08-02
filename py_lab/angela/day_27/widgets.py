from tkinter import *

window=Tk()
window.minsize(width=500, height=300)
window.title("Widgets")

def get_text():
    print("The text :",text.get("1.0",END).strip())
    print("The entry :",entry.get())
    print("The spinbox :", spinbox.get())
    print("The scale :", scale.get())
    print("Checkbutton State :", (checkbutton_state.get() and "Checked!") or "Not checked!", checkbutton_state.get())
    print("checked Radio :", checked_radio.get())

button=Button(text="Get text",command=get_text)
button.pack()

label=Label(text="I will change")
label.pack()

entry=Entry()
entry.pack()
entry.insert(END, "Hello")

text=Text(width=40,height=6)
text.insert(END,"Yeah bitch!")
text.pack()

spinbox=Spinbox(from_=0,to=100)
spinbox.pack()

scale=Scale(from_=0, to=100)
scale.pack()

checkbutton_state=IntVar()
checkbutton=Checkbutton(text="Check-button", variable=checkbutton_state)
checkbutton.pack()

checked_radio=IntVar()
radio1=Radiobutton(text="Male", value=1, variable=checked_radio)
radio2=Radiobutton(text="Female", value=0, variable=checked_radio)
radio1.pack()
radio2.pack()



window.mainloop()
