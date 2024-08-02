from tkinter import *

window=Tk()
window.minsize(width=150,height=70)
window.title("Convert mile to KM")
window.config(padx=30, pady=30)



label_equal=Label(text="Equal to :")
label_equal.grid(column=0, row=1)

entry_miles=Entry(width=15)
entry_miles.grid(column=1,row=0)

label_result=Label(text=0)
label_result.grid(column=1, row=1)

label_miles=Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km=Label(text="KM")
label_km.grid(column=2, row=1)

def converter():
    miles=int(entry_miles.get())
    km=miles*1.609
    label_result.config(text=km)


button_convert=Button(text="Convert", command=converter)
button_convert.grid(column=1, row=2)







window.mainloop()
