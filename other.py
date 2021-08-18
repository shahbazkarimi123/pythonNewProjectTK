from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter import ttk
import csv


class NewWindow:

    def __init__(self,master):
        self.i=0
        f2 = Frame(master)
        f2.place(x=0, y=0,width=500,height=600)


    def firstfram(self):
        self.f1 = Frame()
        self.f1.place(x=0, y=0, width=500, height=600)
        self.b1 = Button(self.f1, text="New Entry", command=self.newEntry)
        self.b1.grid(column=0, row=0)

        b2 = Button(self.f1, text="list of student", command=self.ListOfStudent)
        b2.grid(column=0, row=1)


    def seeFile(self):
        self.f3 = Frame()
        self.f3.place(x=0, y=0, width=500, height=600)
        print("Save")
        self.l1 = Label(self.f3, text="Saved")
        self.l1.grid(padx=0,pady=0,stick=tkinter.W)
        n1 = self.e1.get()
        n2 = self.e2.get()
        n3 = self.e3.get()
        self.l1.config(text="Name: {0}\nClass: {1}\nDate: {2}".format(n1, n2, n3))

    def newEntry(self):
        self.f2 = Frame()
        self.f2.place(x=0, y=0, width=500, height=600)
        self.l1 = Label(self.f2, text="Name: ", font=("Arial", 20, "bold"))
        self.l1.grid(column=0, row=0)
        self.l2 = Label(self.f2, text="Date:", font=("Arial", 20, "bold"))
        self.l2.grid(column=0, row=1, stick=tkinter.W)
        self.l3 = Label(self.f2, text="Class:", font=("Arial", 20, "bold"))
        self.l3.grid(column=0, row=2, stick=tkinter.W)

        self.e1 = Entry(self.f2)
        self.e1.grid(column=1, row=0)
        self.e2 = Entry(self.f2)
        self.e2.grid(column=1, row=1)
        self.e3 = Entry(self.f2)
        self.e3.grid(column=1, row=2)
        self.b2 = Button(self.f2, text="Save", command=self.savefile)
        self.b2.grid(column=1,row=3)
        self.b3 = Button(self.f2, text="Back", command=self.backNewEntry)
        self.b3.grid(column=1,row=4)


    def savefile(self):
        self.i += 1
        self.seeFile()
        #filename = filedialog.asksaveasfilename(initialdir='/', title='Save File', filetypes=(('Text Files', 'txt.*'), ('All Files', '*.*')))
        myfile = open("game1.txt", "a")
        name = self.e1.get()
        date = self.e2.get()
        Class = self.e3.get()
        myfile.write("{0}\nName: {1}\nDate: {2}\nClass: {3}\n".format(self.i,name,date,Class))
        print(name+date+Class)
        myfile.close()

    def ListOfStudent(self):
        self.newf=Frame()
        self.newf.place(x=0,y=0,width=500,height=600)
        self.lab = Label(self.newf,text="name")
        self.lab.grid(column=0,row=0)
        #table
        tv = ttk.Treeview(self.newf, columns=(1, 2, 3),show="headings")
        tv.grid(column=0,row=1)
        tv.heading(1, text="Name")
        tv.heading(2, text="Class")
        tv.heading(3, text="Date")
        file = open("Data.csv")
        Reader = csv.DictReader(file)
        for x in Reader:
            print(x['Name'])
            tv.insert("",END,value=x['Name'])
            tv.insert("",END,value=x['Class'])

        self.backb = Button(self.newf, text="Back", command=self.backListofStudent)
        self.backb.grid(column=1, row=4)

    def backNewEntry(self):
        self.f2.destroy()
        self.firstfram()


    def backListofStudent(self):
        self.newf.destroy()
        self.firstfram()






