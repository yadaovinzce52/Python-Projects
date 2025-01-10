import random

from flask import Flask

app = Flask(__name__)
random_number = random.randint(1,100)

@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://mathspig.wordpress.com/wp-content/uploads/2021/06/spinning-wheel-2.gif'>")

@app.route('/<int:number>')
def guess(number):
    print(random_number)
    if number == random_number:
        return ('<h1 style="color:#48f542">You guessed correctly!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDAwbXVxajJ0YXptN3BiMXM3cGxybHZnZWJjbHJ4aDhpb3E4cW9saiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IwAZ6dvvvaTtdI8SD5/giphy.gif">')
    elif number < random_number:
        return ('<h1 style="color:red">Too low, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnlxem45cDV1ZXg1cHFweTNhbzJpZ3U1a3p0ZjlnNncwYXZyYXk1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif">')
    else:
        return ('<h1 style="color:blue">Too high, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG94bXQ3M25lMm50NTNqd2Zud3R0dXFkNjI4Zzd6MmVnbHZha3dweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d8EN0mls2eoAFLRiX8/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)