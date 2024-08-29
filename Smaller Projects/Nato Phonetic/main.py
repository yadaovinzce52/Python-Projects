import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)


def generate_phonetic():
    message = input('Enter a word: ').upper()
    try:
        res = [nato_dict[c] for c in message if c != ' ']
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(res)


generate_phonetic()