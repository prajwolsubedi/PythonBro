from tkinter import *


window = Tk()
window.config(padx=40,pady=40)
window.title("Password Manager")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
canvas = Canvas(width=200,height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=mypass_img)
canvas.grid(row=0, column=0)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #



window.mainloop()