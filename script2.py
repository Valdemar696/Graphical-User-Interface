from tkinter import *

window = Tk()

def kg_to_other():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)

    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)

    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)

t1=Label(window,text="Kg")
t1.grid(row=0,column=0)

b1=Button(window, text= "Convert", command=kg_to_other)
b1.grid(row=0, column=2, columnspan=10)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0, rowspan=2, columnspan=10)

t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)

window.mainloop()