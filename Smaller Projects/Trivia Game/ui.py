from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.score = 0
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Trivia Game')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text',
            fill=THEME_COLOR,
            font=('Ariel', 20, 'italic')
        )
        self.canvas.config()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file='images/true.png')
        self.false_image = PhotoImage(file='images/false.png')

        self.true = Button(image=self.true_image, highlightthickness=0, command=self.true_button)
        self.false = Button(image=self.false_image, highlightthickness=0, command=self.false_button)

        self.true.grid(row=2, column=0)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def true_button(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='You have reached the end of the Trivia game.')
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.score_label.config(text=f'score: {self.score}')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

