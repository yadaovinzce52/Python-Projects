from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
current_card: {}
card_dict = {}

# ------------------------- Accessing csv/Variables ------------------------- #
# French to english dictionary
try:
    data = read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = read_csv('data/french_words.csv')
    card_dict = original_data.to_dict(orient='records')
else:
    card_dict = data.to_dict(orient='records')


# ------------------------- Save/remove ------------------------- #
def right():
    card_dict.remove(current_card)

    to_learn = DataFrame(card_dict)
    to_learn.to_csv('data/words_to_learn.csv', index=False)

    generate_new_word()


# ------------------------- Getting new word ------------------------- #
def generate_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(card_dict)
    card.itemconfig(language, fill='black')
    card.itemconfig(word, fill='black')
    card.itemconfig(language, text='French')
    card.itemconfig(word, text=current_card['French'])
    card.itemconfig(card_image, image=front_image)

    flip_timer = window.after(3000, flip)


# ------------------------- Flip the card ------------------------- #
def flip():
    card.itemconfig(language, fill='white')
    card.itemconfig(word, fill='white')
    card.itemconfig(language, text='English')
    translation = current_card['English']
    card.itemconfig(word, text=translation)
    card.itemconfig(card_image, image=back_image)


# ------------------------- Creating GUI ------------------------- #

# Main Window
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip)

# FlashCard
card = Canvas(width=800, height=526, highlightthickness=0)
card.config(bg=BACKGROUND_COLOR)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
card_image = card.create_image(400, 263, image=front_image)
language = card.create_text(400, 150, text='French', font=(FONT_NAME, 40, 'italic'))
word = card.create_text(400, 263, text='word', font=(FONT_NAME, 60, 'bold'))
card.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file='images/wrong.png')
right_image = PhotoImage(file='images/right.png')

wrong = Button(image=wrong_image, highlightthickness=0, command=generate_new_word)
right = Button(image=right_image, highlightthickness=0, command=right)

wrong.grid(row=2, column=0)
right.grid(row=2, column=1)

generate_new_word()

window.mainloop()
