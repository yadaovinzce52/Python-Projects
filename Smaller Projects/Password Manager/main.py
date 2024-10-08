from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ------------------------------- SEARCH ENTRY ---------------------------------- #
def search():
    site_search = web_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        user = data[site_search]['email']
        password = data[site_search]['password']
    except FileNotFoundError:
        messagebox.showinfo(title='File not Found', message='No Data File Found')
    except KeyError:
        messagebox.showinfo(title='No login for Website', message='No details for the website exists.')
    else:
        messagebox.showinfo(title=f'{site_search}', message=f'Email: {user}\nPassword: {password}!')


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
    new_data = {
        web: {
           'email': user,
           'password': password,
        }
    }

    if not web or not password:
        messagebox.showinfo(title='Missing Information', message='Please fill in website or password')
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
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
web_entry = Entry(width=30)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(width=50)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'yadaovinzce@gmail.com')
pass_entry = Entry(width=30)
pass_entry.grid(row=3, column=1)

# Buttons
search = Button(text='Search', command=search, width=15)
search.grid(row=1, column=2)
generate = Button(text='Generate Password', command=generate)
generate.grid(row=3, column=2)
add = Button(text='Add', command=add, width=40)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
