from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_entry.delete(0, END)

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)

    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()

    if not web or not password:
        messagebox.showinfo(title='Missing Information', message='Please fill in website or password')
    else:
        ok = messagebox.askokcancel(title=web_entry.get(), message=f'These are the details entered: \nEmail: '
                                                                   f'{user}\nPassword: {password}\nIs it ok to save?')

        if ok:
            with open('data.txt', 'a') as file:
                file.writelines(f'{web} | {user} | {password}\n')

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)
pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=43)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
user_entry = Entry(width=43)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'yadaovinzce@gmail.com')
pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

# Buttons
generate = Button(text='Generate Password', command=generate)
generate.grid(row=3, column=2)
add = Button(text='Add', command=add, width=36)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
