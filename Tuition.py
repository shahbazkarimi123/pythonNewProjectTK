import tkinter
from other import save_data
window = tkinter.Tk()

window.title("Karimi Institute")

window.geometry("500x600")

name = tkinter.Label(text="Name", font=("Arial",20,"bold"))
name.grid(column=0,row=0)
#text
name_text = tkinter.Entry(window)
name_text.grid(column=1,row=0)

date = tkinter.Label(text="Date  ",font=("Arial",20,"bold"))
date.grid(column=0,row=2,padx=0)
date_text = tkinter.Entry(window)
date_text.grid(column=1,row=2)
s_class = tkinter.Label(text="Class",font=("Arial",20,"bold"))
s_class.grid(column=0,row=3)
s_class_text = tkinter.Entry(window)
s_class_text.grid(column=1,row=3)

#button

button = tkinter.Button(text="Save",command=save_data)

button.grid(column=4,row=4)
#collect


window.mainloop()

