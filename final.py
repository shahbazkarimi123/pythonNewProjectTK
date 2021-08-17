from tkinter import *
from other import NewWindow

tk = Tk()
tk.geometry("500x600")
c = NewWindow(tk)

f1 = Frame()
f1.place(x=0, y=0, width=500, height=600)
b1 = Button(f1, text="New Entry", command=c.newEntry)
b1.grid(column=0,row=0)

b2 = Button(f1,text="list of student",command=c.ListOfStudent)
b2.grid(column=0,row=1)



tk.mainloop()
