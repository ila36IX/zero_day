from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    chars=[chr(r.choice([r.randint(65,90), r.randint(97,122)])) for _ in range(6)]+["@","#"]
    password="".join(r.sample(chars,8))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    print(pyperclip.paste())
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add(w, u, p):
    if w=="" or u=="" or p=="":
        return messagebox.showerror(title="Required infos", message="Please be sure to fill all the fields :)")
    data=w + " | " + u + " | " + p + "\n"
    check=messagebox.askokcancel(title="Check", message="Are you sure to save those infos?")
    if check:
        with open("passwords.txt","a") as file :
            file.write(data)
            reset()

def find_paasword(website_input):
    try:
        with open("passwords.txt","r") as file :
            lines = file.readlines()
            lines = [l.strip().split("|") for l in lines]
            result = [l.strip() for l in lines if l[0].strip() == website_input]
            print(result)
    except Exception as e:
        print(e)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("My Pass")
window.config(padx=30, pady=30)
canvas=Canvas(width=200,height=200)

logo=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#___labels___#

website_label=Label(text="Website")
website_label.grid(column=0,row=1, pady=6)

username_label=Label(text="Email/Username")
username_label.grid(column=0, row=2, pady=6)

password_label=Label(text="Password")
password_label.grid(column=0, row=3, pady=6)

#__entries___#

website_entry=Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry=Entry(width=51)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END,"jbariali002@gmail.com")


password_entry=Entry(width=33)
password_entry.grid(column=1, row=3)

#___button___ #

search_button=Button(text="search", width=13, command=lambda: find_paasword("faceboo.com"))
search_button.grid(column=2, row=1)

generete_button=Button(text="Generate Password", command=generate_pass, width=13)
generete_button.grid(column=2, row=3)

def reset(w=website_entry, p=password_entry):
    w.delete(0, END)
    p.delete(0, END)
def add_short():
    a = website_entry.get()
    b = username_entry.get()
    c = password_entry.get()
    add(a, b, c)
add_button=Button(text="Add", width=43, command=add_short)
add_button.grid(column=1, columnspan=2, row=4)


window.mainloop()
