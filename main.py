import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="skyblue")

#button function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#label for entering user url
Label(win,text="Enter Your URL",font="impack 17 bold",bg="black",fg="white").pack(fill="x")

#entery box
entry1=Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)

#button
Button(win,text="Click me",font="impack 10 bold",bg="blue",fg="white",width=14,command=short).pack()

#Short link
entry2=Entry(win,font="impack 16 bold",bg="white",width=24)
entry2.pack(pady=30)

mainloop()
