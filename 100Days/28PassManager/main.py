from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os

window = Tk()
window.config(padx=20,pady=20)
window.title("Password Manager")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_text_box.delete("1.0", "end-1c")

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password_generated = ''.join(password_list)
    password_text_box.insert("end", password_generated)
    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_text_box.get("1.0",  "end-1c")
    username = username_text_box.get("1.0",  "end-1c")
    password = password_text_box.get("1.0",  "end-1c")
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Password Confirmation", message=f" These are the details entered: \n Username: {username} \n Password: {password} \n Is it ok to save?")
        if is_ok:
            filename="data.txt"
            try:
                with open(filename, "a") as file:
                    file.write(f"{website} | {username} | {password} \n")
                print(f"File '{filename}' has been saved successfully.")
                website_text_box.delete("1.0", "end")
                password_text_box.delete("1.0", "end")
                messagebox.Message("Password Saved Successfully.")
                website_text_box.focus()
            except Exception as e:
                print(f"An error occurred: {e}")



canvas = Canvas(width=200,height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=mypass_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)

website_text_box = Text(window,height=1, width=39)
website_text_box.grid(row=1,column=1, columnspan=2)
website_text_box.focus()

username_label = Label(text = "Email/Username: ")
username_label.grid(row=2,column=0)

username_text_box = Text(window,height=1, width=39)
username_text_box.grid(row=2,column=1, columnspan=2)
username_text_box.insert("1.0","prajwolsubedizzz@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3,column=0)

password_text_box = Text(window, height=1, width=21)
password_text_box.grid(row=3,column=1, sticky="w")

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3,column=2)

add_password_btn = Button(text="Add", width=39, command=save_password)
add_password_btn.grid(row=4,column=1, columnspan=2, sticky="ew")



# ---------------------------- UI SETUP ------------------------------- #



window.mainloop()