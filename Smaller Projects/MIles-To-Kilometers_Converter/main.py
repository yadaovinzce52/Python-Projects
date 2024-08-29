import tkinter as tk

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(300, 100)
window.config(padx=50, pady=50)

# Equal Label
equal_label = tk.Label(text='is equal to')
equal_label.grid(column=0, row=1)

# Speed Label (Will be changed)
speed_label = tk.Label(text='0')
speed_label.grid(column=1, row=1)


def calculate():
    mph = int(entry.get())
    kmh = mph * 1.609
    speed_label.config(text=kmh)


# Convert Button
convert = tk.Button(text='Calculate', command=calculate)
convert.grid(column=1, row=2)

# Entry
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

# Miles Label
miles = tk.Label(text='Miles')
miles.grid(column=2, row=0)

# Km Label
km = tk.Label(text='Km')
km.grid(column=2, row=1)

window.mainloop()