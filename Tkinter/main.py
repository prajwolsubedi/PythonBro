from tkinter import *

window  = Tk()

window.title("My first GUI Program")

window.minsize(width=500, height=300)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.place(x=50,y=0)
# my_label.pack()
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="new text")

#Button
def button_clicked():
    my_label["text"] = input.get()

button = Button(text = "Click me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=20)
input.grid(column=2, row=2)



window.mainloop()