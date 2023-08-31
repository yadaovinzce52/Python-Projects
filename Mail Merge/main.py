# Read the letter and save it into a local variable
with open("Input/Letters/starting_letter.txt") as letter:
    message = letter.read()

# Read the list of names and replace the [name] in the message with the name and
# create a new letter for each name
with open("Input/Names/invited_names.txt") as file:
    names = file.read()
    for name in names.split():
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
            letter.write(message.replace("[name]", name))
